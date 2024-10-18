import os
from google.cloud import storage
from flask import jsonify, request
import functions_framework

@functions_framework.http
def create_text_file_http(request):
    """HTTP Cloud Function that creates a text file in a Google Cloud Storage bucket."""
    
    # Get the bucket name from the environment variable
    bucket_name = os.environ.get('BUCKET_ENV_VAR')
    if not bucket_name:
        return jsonify({"error": "Bucket name not found in environment variables"}), 500

    # Parse the incoming JSON request
    request_json = request.get_json(silent=True)
    
    if not request_json:
        return jsonify({"error": "Invalid JSON payload."}), 400

    # Ensure both 'fileName' and 'fileContent' are in the JSON request
    if 'fileName' not in request_json or 'fileContent' not in request_json:
        return jsonify({"error": "Invalid request. Must contain 'fileName' and 'fileContent' in JSON."}), 400
    
    file_name = request_json['fileName']
    file_content = request_json['fileContent']

    # Initialize the Google Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Create a new blob (file) in the specified bucket
    blob = bucket.blob(file_name)
    blob.upload_from_string(file_content)

    # Return the fileName in the response
    return jsonify({"fileName": file_name}), 200
