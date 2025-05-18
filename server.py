from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetection")

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    return ("For this statement, the system responds with 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}}. "
            "The dominant emotion is {}.").format(
        response['anger'],
        response['disgust'],
        response['fear'],
        response['joy'],
        response['sadness'],
        response['dominant_emotion'],
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')