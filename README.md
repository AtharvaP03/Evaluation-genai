### README.md

```markdown
# Technical Interview Question Generator

The Technical Interview Question Generator is a Flask application designed to assist users in preparing for technical interviews by generating questions related to various computer science topics. The application utilizes the OpenAI API to dynamically create questions and provides a rubric-based evaluation system for assessing user-submitted answers.

## Features

- **Dynamic Question Generation:** The application generates technical questions randomly from predefined topics such as Arrays, Linked Lists, Stacks and Queues, and Trees.
- **OpenAI Integration:** Utilizes the OpenAI API to create questions based on specified instructions and topic descriptions.
- **Rubric-Based Evaluation:** Provides a systematic evaluation system based on a predefined rubric to assess the quality of user-provided answers.
- **User-Friendly Interface:** Offers an intuitive web interface for generating questions and evaluating answers, making it easy for users to practice and improve their skills.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/technical-interview-question-generator.git
   ```
   
2. **Navigate to the Project Directory:**
   ```bash
   cd technical-interview-question-generator
   ```
   
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**
   ```bash
   python app.py
   ```

2. **Access the Application:**
   - Open your web browser and go to `http://localhost:5000`.
   
3. **Generate a Question:**
   - Click on the "Generate Question" button to receive a randomly generated technical question.
   
4. **Evaluate Your Answer:**
   - Enter your answer in the provided text field and click on the "Evaluate" button to assess your response based on the rubric.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

### requirements.txt

```
Flask==2.1.2
openai==0.10.2
```

This README file provides comprehensive information about the Technical Interview Question Generator, including its features, installation instructions, usage guidelines, contribution guidelines, and licensing information. The `requirements.txt` file lists the dependencies required to run the Flask application.
