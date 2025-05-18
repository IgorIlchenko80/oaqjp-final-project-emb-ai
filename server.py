"""Flask server for emotion detection web app."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emo_detector():
    """Analyzes text and returns detected emotions and the dominant one."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For this statement, the system responds with "
        "'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        "'joy': {joy} and 'sadness': {sadness}. "
        "The dominant emotion is {dominant_emotion}.".format(**response)
    )


@app.route("/")
def render_index_page():
    """Renders the main index HTML page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
