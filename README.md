# AI-Based Candidate Screening System

An intelligent candidate screening solution powered by GPT-3.5, Langchain, and Streamlit. This system automates the initial interview process by evaluating candidate responses based on technical knowledge, problem-solving skills, and communication ability.

![download (1)](https://github.com/user-attachments/assets/10ac7391-a63a-4729-9ef3-0ffce38894ae)



## 🚀 Features

- **Interactive Interview Interface**: Streamlit-based UI for seamless candidate response collection
- **AI-Powered Evaluation**: Leverages GPT-3.5 through Langchain for comprehensive response analysis
- **Multi-criteria Assessment**: Evaluates candidates on:
  - Technical Knowledge
  - Problem-solving Skills
  - Communication Ability
- **Automated Ranking**: Generates candidate rankings based on performance metrics
- **Real-time Feedback**: Instant evaluation results and insights

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **AI Engine**: GPT-3.5
- **Framework**: Langchain
- **Language**: Python 3.8+

## 📋 Prerequisites

Before running the system, ensure you have:

- Python 3.8 or higher installed
- OpenAI API key
- Basic understanding of terminal/command line operations

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/csoren66/AI-Based-Candidate-Screening-System.git
cd AI-Based-Candidate-Screening-System
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
# Create a .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Access the application in your web browser (typically http://localhost:8501)

3. Follow the on-screen instructions to:
   - Input candidate responses
   - Review evaluation results
   - Access candidate rankings

## 📊 Evaluation Criteria

The system evaluates candidates based on the following parameters:

### Technical Knowledge (40%)
- Understanding of core concepts
- Technical accuracy
- Depth of knowledge

### Problem-solving Skills (35%)
- Analytical thinking
- Solution approach
- Innovation and creativity

### Communication Ability (25%)
- Clarity of expression
- Structure and organization
- Professional language use
