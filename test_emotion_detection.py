import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I'm glad this happened.")
        self.assertEqual(result_1['dominant_emotion'], 'anger')
