from boto3 import Session
import os

# Create a session using your AWS credentials
session = Session(profile_name="default")

# Create an S3 resource object using the session
s3 = session.resource('s3')

# Ask user for confirmation
user_input = input("Do you want to push the files to S3? (yes/no): ")

if user_input.lower() == 'yes':
    directory_path = '/Users/sauravmanitripathi/Desktop/content upsc'  # directory from which to upload

    for dirpath, dirs, files in os.walk(directory_path):
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            s3_path = os.path.relpath(filepath, directory_path).replace(os.sep, '/')
            print(f'Uploading {s3_path} to S3...')
            s3.meta.client.upload_file(filepath, 'free-upsc-material', s3_path)
else:
    print("Operation cancelled.")
