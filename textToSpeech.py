import os
from gtts import gTTS
from tqdm import tqdm

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
input_folder = 'Fetched Article'
output_folder = 'Audio HTML Page/01Text To Speech'

# Get the list of text files
text_files = [filename for filename in os.listdir(input_folder) if filename.endswith('.txt')]

# Iterate over files in the input folder
for filename in text_files:
    file_path = os.path.join(input_folder, filename)
    with tqdm(total=1, desc=f'Converting {filename}', unit='file') as pbar:
        convert_to_audio(file_path, output_folder)
        pbar.update(1)
