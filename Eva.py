from flask import Flask, request, jsonify, render_template
import openai
import random

openai.api_key = "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"

app = Flask(__name__)

# Define technical topics
technical_topics = {
    "Arrays": [
        "technical questions related to arrays.",
        "Sorting algorithms for arrays.",
        "Search algorithms for arrays."
    ],
    "Linked Lists": [
        "technical questions related to linked lists.",
        "Insertion and deletion operations in linked lists.",
        "Cyclic detection and removal in linked lists."
    ],
    "Stacks and Queues": [
        "Implementing stacks and queues using arrays or linked lists.",
        "Applications of stacks and queues in algorithm design.",
        "Optimizing stack and queue operations for efficiency."
    ],
    "Trees": [
        "technical questions related to trees.",
        "Traversal algorithms for trees (e.g., inorder, preorder, postorder).",
        "Balancing techniques for binary search trees."
    ]
}

# Define rubrics and criteria for evaluation
rubric = {
    "Excellent": {
        "min_score": 90,
        "description": "Excellent understanding and comprehensive response."
    },
    "Good": {
        "min_score": 70,
        "description": "Good understanding with minor errors or omissions."
    },
    "Fair": {
        "min_score": 50,
        "description": "Basic understanding with significant errors or omissions."
    },
    "Poor": {
        "min_score": 0,
        "description": "Poor understanding with major errors or lack of response."
    }
}

def generate_technical_question():
    topic = random.choice(list(technical_topics.keys()))
    topic_description = random.choice(technical_topics[topic])
    prompt = f"""
Generate a technical question related to {topic}.

Instructions:
- The question should assess the candidate's knowledge and understanding of fundamental concepts, principles, and best practices related to {topic}.
- Ensure that the question is clear, concise, and relevant to the topic.
- Focus on assessing the candidate's problem-solving abilities, critical thinking skills, and domain expertise.
- Avoid overly complex or obscure topics, and prioritize questions that are practical and applicable in real-world scenarios.
- Consider including scenarios or case studies to provide context and enhance the relevance of the question.
- Aim for questions that require thoughtful analysis and demonstrate the candidate's ability to apply theoretical knowledge to practical situations.

Topic Description:
{topic_description}
"""

    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=120,
        temperature=0.5,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip(), topic

def evaluate_answer(question, answer):
    try:
        # Placeholder evaluation (simulating a random score)
        score = random.randint(0, 100)

        # Determine the grade based on the rubric
        grade = None
        for level, criteria in rubric.items():
            if score >= criteria["min_score"]:
                grade = level
                break

        return score, grade

    except Exception as e:
        print(f"Error evaluating answer: {e}")
        return None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_question', methods=['GET'])
def generate_question():
    question, topic = generate_technical_question()
    return jsonify({"question": question, "topic": topic})

@app.route('/evaluate_answer', methods=['POST'])
def evaluate_answer_endpoint():
    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')
    if question and answer:
        score, grade = evaluate_answer(question, answer)
        return jsonify({"score": score, "grade": grade})
    else:
        return jsonify({"error": "Both question and answer are required."}), 400

if __name__ == '__main__':
    app.run(debug=True)
