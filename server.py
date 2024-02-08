from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/emotionDetector")
def emot_detect():
    text_to_analyse = request.args.get('textToAnalyze')

    detector_output = emotion_detector(text_to_analyse)

    if detector_output['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'

    response = "For the given statement, the system response is "

    for emotion, score in detector_output.items():
        if emotion != 'dominant_emotion':
            response = response+"'"+emotion+"': "+str(score)+", "

    response = response+". The dominant emotion is "+detector_output['dominant_emotion']

    return response, 200

@app.route('/')
def render_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000)
