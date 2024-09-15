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
  region      = "europe-west1"
  zone        = "europe-west1-a"
}

variable "bucket_name" {
  description = "The name of the storage bucket"
  type        = string
  default = "shawkot-bucket"
}

variable "folder_name" {
  description = "The name of the folder within the bucket"
  type        = string
  default = "my-folder"
}

resource "google_storage_bucket" "static" {
  name          = var.bucket_name
  location = "europe-west1"
  storage_class = "STANDARD"
  uniform_bucket_level_access = true
}

resource "google_storage_bucket_object" "folder" {
  name   = "${var.folder_name}" 
  bucket = google_storage_bucket.static.name
  content = " "  
}

