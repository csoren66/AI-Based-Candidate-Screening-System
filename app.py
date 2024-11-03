import streamlit as st
from langchain import OpenAI
import os

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = '##Enter your own key'

# Initialize the LLM (using GPT-3.5 via Langchain)
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Predefined interview questions
questions = [
    "Can you explain the difference between supervised and unsupervised learning, and provide an example of each?",
    "You are given a large dataset with missing values and noise. How would you preprocess the data for training a machine learning model?",
    "Tell us about a project you worked on that involved using deep learning. What challenges did you face, and how did you overcome them?",
    "How would you explain the concept of reinforcement learning to someone without a technical background?",
    "Describe a time when you had to collaborate with a team under a tight deadline. How did you handle it?"
]

# Predefined evaluation criteria
evaluation_criteria = [
    "Technical Knowledge",
    "Problem-Solving Ability",
    "Experience",
    "Communication Skills",
    "Cultural Fit"
]

# Streamlit UI
st.title("AI-Based Candidate Screening System")

# Section for candidate information
st.header("Candidate Information")
name = st.text_input("Candidate Name")
position = st.text_input("Position Applying For")

# Section for interview responses
st.header("Interview Responses")
responses = []
for question in questions:
    response = st.text_area(f"{question}", key=question)
    responses.append(response)

# Button to trigger evaluation
if st.button("Evaluate Candidate"):
    if not all(responses):
        st.error("Please answer all questions.")
    else:
        # Evaluate responses using GPT-3.5 via Langchain
        st.subheader(f"Evaluation for {name} - {position}")
        total_score = 0
        detailed_feedback = ""

        for idx, response in enumerate(responses):
            st.write(f"**Question {idx + 1}:** {questions[idx]}")
            st.write(f"**Response:** {response}")

            # Use GPT-3.5 to evaluate the response based on the corresponding criterion
            prompt = f"""You are a hiring manager evaluating a candidate for an AI-related position.
            The question asked was: "{questions[idx]}".
            The candidate's response was: "{response}".
            Evaluate this response based on the following criterion: "{evaluation_criteria[idx]}".
            Provide a score between 0 and 100, and explain the reasoning behind the score."""

            evaluation = llm(prompt)
            st.write(evaluation)

            # Extract the score from the evaluation
            score = int(evaluation.split("Score:")[-1].strip().split()[0])
            total_score += score

            detailed_feedback += f"**Question {idx + 1} Feedback:** {evaluation}\n\n"

        # Display the final score and detailed feedback
        average_score = total_score / len(questions)
        st.subheader(f"Final Evaluation Score: {average_score:.2f} / 100")
        st.write("**Detailed Feedback:**")
        st.write(detailed_feedback)

        # Rank based on score (basic ranking logic can be enhanced later)
        if average_score > 80:
            st.success("Highly Suitable for the Role")
        elif 60 <= average_score <= 80:
            st.warning("Moderately Suitable for the Role")
        else:
            st.error("Not Suitable for the Role")
