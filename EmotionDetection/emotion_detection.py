import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    inputJson = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=inputJson, headers=header)
    
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)

        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
    elif response.status_code == 400:
        dominant_emotion = None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }