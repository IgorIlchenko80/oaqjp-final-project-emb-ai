import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I'm glad this happened.")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_1 = emotion_detector("I'm really angry about this")
        self.assertEqual(result_1['dominant_emotion'], 'anger')

        result_1 = emotion_detector("I feel disgusted just hearing about it.")
        self.assertEqual(result_1['dominant_emotion'], 'disgust')

        result_1 = emotion_detector("I feel very sad about this")
        self.assertEqual(result_1['dominant_emotion'], 'sadness')

        result_1 = emotion_detector("I'm really scared that this will happen.")
        self.assertEqual(result_1['dominant_emotion'], 'fear')

unittest.main()