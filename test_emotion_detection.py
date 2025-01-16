from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy sentiment
        result_1 = emotion_detector('I am glad this happened')
        emotions = result_1['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        self.assertEqual(dominant_emotion, 'joy')

        # Test case for anger sentiment
        result_1 = emotion_detector('I am really mad about this')
        emotions = result_1['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        self.assertEqual(dominant_emotion, 'anger')
        
        # Test case for disgust sentiment
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        emotions = result_1['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        self.assertEqual(dominant_emotion, 'disgust')
        
        # Test case for sadness sentiment
        result_1 = emotion_detector('I am so sad about this')
        emotions = result_1['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        self.assertEqual(dominant_emotion, 'sadness')
        
        # Test case for fear sentiment
        result_1 = emotion_detector('I am really afraid that this will happen')
        emotions = result_1['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        self.assertEqual(dominant_emotion, 'fear')

unittest.main()
