import os

source_dir = "/Users/sauravmanitripathi/Desktop/content upsc/Audio HTML Page/01Text To Speech"
target_dir = "/Users/sauravmanitripathi/Desktop/content upsc/Audio HTML Page"

for filename in os.listdir(source_dir):
    if filename.endswith(".mp3"):
        file_path = os.path.join("01Text To Speech", filename)
        title = filename.replace(".mp3", "")
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Free UPSC Podcast</title>
        </head>
        <body>
          <h1>{title}</h1>

          <audio id="audioPlayer" controls>
            <source id="audioSource" src="" type="audio/mpeg">
            Your browser does not support the audio element.
          </audio>

          <button id="playButton" onclick="playAudio()">Play</button>
          <button id="pauseButton" onclick="pauseAudio()" disabled>Pause</button>

          <script>
            var audioPlayer = document.getElementById("audioPlayer");
            var audioSource = document.getElementById("audioSource");
            var playButton = document.getElementById("playButton");
            var pauseButton = document.getElementById("pauseButton");

            var audioFilePath = "{file_path}";

            audioSource.src = audioFilePath;

            function playAudio() {{
              audioPlayer.play();
              playButton.disabled = true;
              pauseButton.disabled = false;
            }}

            function pauseAudio() {{
              audioPlayer.pause();
              playButton.disabled = false;
              pauseButton.disabled = true;
            }}
          </script>
        </body>
        </html>
        """

        target_file_path = os.path.join(target_dir, filename.replace(".mp3", ".html"))
        with open(target_file_path, 'w') as f:
            f.write(html_content)
