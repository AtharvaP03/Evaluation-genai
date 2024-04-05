"""
_________________________________________________________________
This is the code for the Evaluation
_________________________________________________________________
"""


from flask import Flask, request, jsonify, render_template
import re
from textblob import TextBlob
import google.generativeai as genai
from dotenv import load_dotenv
import os


app = Flask(__name__)

rubric = {
    "Excellent": {"min_score": 90, "criteria": {"Accuracy": {"weight": 0.175}, "Completeness": {"weight": 0.175}, "Relevance": {"weight": 0.1}, "Clarity": {"weight": 0.175}, "Depth": {"weight": 0.1}, "Organization": {"weight": 0.1}, "Use of Evidence": {"weight": 0.1}, "Grammar and Spelling": {"weight": 0.1}, "Sentiment": {"weight": 0.075}}},
    "Good": {"min_score": 75, "criteria": {"Accuracy": {"weight": 0.175}, "Completeness": {"weight": 0.175}, "Relevance": {"weight": 0.1}, "Clarity": {"weight": 0.175}, "Depth": {"weight": 0.1}, "Organization": {"weight": 0.1}, "Use of Evidence": {"weight": 0.1}, "Grammar and Spelling": {"weight": 0.1}, "Sentiment": {"weight": 0.075}}},
    "Satisfactory": {"min_score": 55, "criteria": {"Accuracy": {"weight": 0.175}, "Completeness": {"weight": 0.175}, "Relevance": {"weight": 0.1}, "Clarity": {"weight": 0.175}, "Depth": {"weight": 0.1}, "Organization": {"weight": 0.1}, "Use of Evidence": {"weight": 0.1}, "Grammar and Spelling": {"weight": 0.1}, "Sentiment": {"weight": 0.075}}},
    "Fair": {"min_score": 40, "criteria": {"Accuracy": {"weight": 0.175}, "Completeness": {"weight": 0.175}, "Relevance": {"weight": 0.1}, "Clarity": {"weight": 0.175}, "Depth": {"weight": 0.1}, "Organization": {"weight": 0.1}, "Use of Evidence": {"weight": 0.1}, "Grammar and Spelling": {"weight": 0.1}, "Sentiment": {"weight": 0.075}}},
    "Poor": {"min_score": 0, "criteria": {"Accuracy": {"weight": 0.175}, "Completeness": {"weight": 0.175}, "Relevance": {"weight": 0.1}, "Clarity": {"weight": 0.175}, "Depth": {"weight": 0.1}, "Organization": {"weight": 0.1}, "Use of Evidence": {"weight": 0.1}, "Grammar and Spelling": {"weight": 0.1}, "Sentiment": {"weight": 0.075}}}
}

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')

    prompt = f"""
    Evaluate the following answer to the question: '{question}'.
    The answer should be evaluated based on the following criteria:
    1. Accuracy: Is the answer factually correct and accurate?
    2. Completeness: Does the answer cover all aspects of the question?
    3. Relevance: Is the answer relevant to the question asked?
    4. Clarity: Is the answer clear and easy to understand?
    5. Depth: Does the answer demonstrate a deep understanding of the topic?
    6. Organization: Is the answer well-organized and structured?
    7. Use of Evidence: Does the answer provide evidence to support its claims?
    8. Grammar and Spelling: Is the answer grammatically correct and free of spelling errors?
    9. Sentiment: What is the overall tone and emotion of the answer?

    Evaluate the answer using a 0-100 score for each criterion, with 100 being the highest score.

    Question: {question}
    Answer: {answer}
    """

    genai.configure(api_key = os.getenv("gemini_api_key" ))# add api key
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)

    evaluation = response.text.strip()
    scores = [float(value) for value in re.findall(r'-?\d+', evaluation)]

    breakdown = {criterion: score * rubric["Satisfactory"]["criteria"][criterion]["weight"] for criterion, score in zip(rubric["Excellent"]["criteria"].keys(), scores)}

    final_score = sum(breakdown.values())

    sentiment = TextBlob(answer).sentiment.polarity

    grade = None
    for level, level_criteria in rubric.items():
        if final_score >= level_criteria["min_score"]:
            grade = level
            break

    return jsonify({
        "final_score": final_score,
        "grade": grade,
        "breakdown": breakdown,
        "sentiment": sentiment
    })

@app.route('/')
def index():
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
