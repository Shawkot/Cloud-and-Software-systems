terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = "shawkot-scs-2024"
  region      = "europe-central2"
  zone        = "europe-central2-a"
}

variable "vm_name_input" {
  description = "The name of the vm instance"
  type        = string
  default = "shawkot-vm"
}

output "vm_name" {
  value       = google_compute_instance.default.name
  description = "The name of the web server"
}

output "public_ip" {
  value       = google_compute_instance.default.network_interface[0].access_config[0].nat_ip
  description = "The public IP address of the web server"
}

resource "google_compute_network" "vpc_network" {
  name                    = "vpc-1"
  auto_create_subnetworks = true
}

resource "google_compute_firewall" "default" {
  name    = "allow-http"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-server"]
}

resource "google_compute_instance" "default" {
  name = var.vm_name_input
  machine_type = "f1-micro"
  zone        = "europe-central2-a"
  
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size = 10 
    }
  }

  labels = {
    course = "css-gcp"
  }

  network_interface {
    network = google_compute_network.vpc_network.self_link

    access_config {
      // Ephemeral public IP
    }
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2
  EOF

  tags = ["http-server"]
}
