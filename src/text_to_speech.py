from gtts import gTTS
import os

def convert_to_audio(story_text, filename="static/story_audio.mp3"):
    """
    Converts AI-generated story text into speech and saves it as an MP3 file.
    """
    if not story_text.strip():  # Prevent empty input issues
        print("Error: No valid text provided for speech conversion!")
        return None

    tts = gTTS(text=story_text, lang='en')
    
    # Ensure the 'static' folder exists
    if not os.path.exists("static"):
        os.makedirs("static")

    tts.save(filename)
    print(f"Audio saved successfully at: {filename}")  # Debugging step

    return filename  # Return file path for Flask
