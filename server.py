"""
server.py

Flask application that serves an emotion detection service using a pre-trained Watson NLP model.
It exposes endpoints for analyzing user-provided text and returning emotion scores
and dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze emotions in the text provided via the 'textToAnalyze' query parameter.

    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_output = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_output

@app.route("/")
def render_index_page():
    """
    Render the index (homepage) for the emotion detection application.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
