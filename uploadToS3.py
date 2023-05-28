from boto3 import Session
import os

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="default")

# Create an S3 resource object using the session
s3 = session.resource('s3')

# Specify your bucket
bucket = s3.Bucket('free-upsc-material')

# Ask user for confirmation
user_input = input("Do you want to push the files to S3? (yes/no): ")

if user_input.lower() == 'yes':
    directory_path = '/Users/sauravmanitripathi/Desktop/content upsc'  # directory from which to upload
    html_files_directory = os.path.join(directory_path, 'HTML_Files')

    # Upload index.html file
    index_file_path = os.path.join(directory_path, 'index.html')
    if os.path.isfile(index_file_path):
        print(f'Uploading {index_file_path} to S3...')
        bucket.upload_file(index_file_path, 'index.html')

    # Upload files from HTML_Files directory
    for file_name in os.listdir(html_files_directory):
        file_path = os.path.join(html_files_directory, file_name)
        if os.path.isfile(file_path):
            existing_objects = list(bucket.objects.filter(Prefix=file_name))
            if not existing_objects:  # Only upload if the file doesn't exist on S3
                print(f'Uploading {file_name} to S3...')
                bucket.upload_file(file_path, f'HTML_Files/{file_name}')
else:
    print("Operation cancelled.")
