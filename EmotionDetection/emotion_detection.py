import requests  
import json

def emotion_detector(text_to_analyze):  
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  

    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    result = json.loads(response.text)

    predictions = result.get("emotionPredictions", [])
    if predictions and "emotion" in predictions[0]:
        emotions = predictions[0]["emotion"]
    else:
        emotions = {"anger": 0, "disgust": 0, "fear": 0, "joy": 0, "sadness": 0}

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(scores, key=scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }