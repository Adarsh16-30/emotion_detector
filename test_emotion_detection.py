from EmotionDetection import emotion_detector

def run_unit_tests():
    test_data = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for statement, expected_emotion in test_data:
        result = emotion_detector(statement)
        print(f"Statement: '{statement}'")
        print(f"Expected Dominant Emotion: {expected_emotion}")
        print(f"Actual Dominant Emotion: {result.get('dominant_emotion')}")
        print("PASS" if result.get('dominant_emotion') == expected_emotion else "FAIL")
        print("-" * 40)

if __name__ == "__main__":
    run_unit_tests()
