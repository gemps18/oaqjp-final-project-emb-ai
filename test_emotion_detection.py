from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        input1 = emotion_detector('I am glad this happened')
        result1 = 'joy'
        self.assertEqual(input1['dominant_emotion'], result1)

        input2 = emotion_detector('I am really mad about this')
        result2 = 'anger'
        self.assertEqual(input2['dominant_emotion'], result2)

        input3 = emotion_detector('I feel disgusted just hearing about this')
        result3 = 'disgust'
        self.assertEqual(input3['dominant_emotion'], result3)

        input4 = emotion_detector('I am so sad about this')
        result4 = 'sadness'
        self.assertEqual(input4['dominant_emotion'], result4)

        input5 = emotion_detector('I am really afraid that this will happen')
        result5 = 'fear'
        self.assertEqual(input5['dominant_emotion'], result5)

unittest.main()
