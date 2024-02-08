import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    return response.text

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
