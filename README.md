# Answer Evaluation Web Application

This web application evaluates answers to given questions based on various criteria and provides a final score along with a breakdown of the evaluation.

## Setup Instructions

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain the API key for the Google Generative AI and replace `"-----------------------"` with your actual API key in the `genai.py` file.
4. Run the Flask application by executing `python genai.py` in your terminal.
5. Access the web application in your browser by navigating to `http://localhost:5000`.

## Usage

1. Enter the question in the provided input field.
2. Enter the answer in the textarea.
3. Click the "Evaluate" button to get the evaluation result.

## Evaluation Criteria

The evaluation is based on the following criteria:
- Accuracy
- Completeness
- Relevance
- Clarity
- Depth
- Organization
- Use of Evidence
- Grammar and Spelling
- Sentiment

## Sentiment Interpretation

- **0**: Neutral sentiment
- **1**: Strong positive sentiment
- **-1**: Strong negative sentiment

## Credits

- This application uses Google Generative AI for evaluating answers.
- TextBlob library is used for sentiment analysis.
