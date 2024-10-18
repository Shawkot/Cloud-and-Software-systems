""" import os
import io # To read from saved file
from google.cloud import storage, vision
import functions_framework
# Add any imports that you may need, but make sure to update requirements.txt

@functions_framework.cloud_event
def image_to_text_storage(cloud_event):
    # TODO: Add logic here
    return
 """

import os
import io
from google.cloud import storage, vision
import functions_framework

@functions_framework.cloud_event
def image_to_text_storage(cloud_event):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
        cloud_event (functions_framework.CloudEvent): The event payload.
    """
    # Extract the bucket and file information from the event
    event_data = cloud_event.data
    bucket_name = event_data['bucket']
    file_name = event_data['name']
    
    # Ignore files that end with .txt
    if file_name.endswith('.txt'):
        return
    
    # Initialize the Google Cloud clients
    storage_client = storage.Client()
    vision_client = vision.ImageAnnotatorClient()

    # Download the image file from the bucket to /tmp
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    temp_file_path = f'/tmp/{file_name}'

    # Ensure /tmp directory is used for storage as Cloud Functions only allow writing to /tmp
    blob.download_to_filename(temp_file_path)

    # Open the image and use the Vision API to detect text
    with io.open(temp_file_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = vision_client.text_detection(image=image)
    text_annotations = response.text_annotations

    # Get the detected text (the full description from the first annotation)
    detected_text = text_annotations[0].description if text_annotations else ""

    # Create a .txt file name based on the image name
    text_file_name = f"{os.path.splitext(file_name)[0]}.txt"
    
    # Save the detected text to a new file in the same bucket
    text_blob = bucket.blob(text_file_name)
    text_blob.upload_from_string(detected_text)

    return
