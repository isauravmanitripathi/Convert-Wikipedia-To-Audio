import os
from gtts import gTTS

# Function to convert text file to audio
def convert_to_audio(file_path, output_folder):
    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read().replace('\n', ' ')

    # Convert text to audio with American English voice
    tts = gTTS(text, lang='en-us')
    audio_file_path = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + '.mp3')
    tts.save(audio_file_path)
    print(f"Converted {file_path} to {audio_file_path}")

# Folder paths
input_folder = '/Users/sauravmanitripathi/Desktop/content upsc/Fetched Article'
output_folder = '/Users/sauravmanitripathi/Desktop/content upsc/Text To Speech'

# Iterate over files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_folder, filename)
        convert_to_audio(file_path, output_folder)
