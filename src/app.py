import os
from flask import Flask, request, render_template, send_from_directory, url_for
from emotion_detection import detect_emotion
from story_generator import generate_story
from text_to_speech import convert_to_audio

# Explicitly define Flask’s template and static directories
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"), static_folder=os.path.join(os.getcwd(), "static"))

# Debugging Step
print(f"📂 Flask is searching for templates in: {app.template_folder}")
print(f"📂 Flask is serving static files from: {app.static_folder}")

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None

    if request.method == "POST":
        user_text = request.form["emotion_input"].strip()
        emotion = detect_emotion(user_text)
        story = generate_story(emotion, user_text)

        if not story.strip():  # Prevent empty output
            story = "Oops! I need more details to craft a great story."

        print(f"📖 Story Passed to Speech: {story}")  # Debugging step

        convert_to_audio(story)  # Convert story to speech

        audio_file = f"/static/story_audio.mp3"  # ✅ Directly reference static folder

        return render_template("index.html", emotion=emotion, story=story, audio_file=audio_file)

    return render_template("index.html", emotion=None, story=None, audio_file=None)

# ✅ Fix Static File Route
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(os.getcwd(), "static"), filename)

if __name__ == "__main__":
    app.run(debug=True)
