import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header, timeout = 5.000)
    
    if response.status_code == 400:
        return{ 
                'anger': None, 
                'disgust': None,
                'fear': None,
                'Joy': None,
                'sadness': None,
                'dominant_emotion': None,
            }
    
    formatted = json.loads(response.text)

    emotions = formatted['emotionPredictions'][0]['emotion']
    
    dominant_emotion = 'default'
    dominant_value = 0

    for emotion, score in emotions.items():
        if dominant_value < score:
            dominant_emotion = emotion
            dominant_value = score

    response = {}

    print('{')
    i=0
    for emotion in emotions:
        print("'",emotion,"': ",emotions[emotion],",", sep='')
        i = i+1
        response[emotion] = emotions[emotion]
    print("'dominant_emotion': '",dominant_emotion,"'",sep='')
    print("}")

    response['dominant_emotion'] = dominant_emotion
    return response
