# 🤖 AI Customer Support Ticket Classification System

An intelligent customer support automation system that uses **Machine Learning** and **Natural Language Processing (NLP)** to automatically classify customer support tickets into the appropriate **Queue**, **Ticket Type**, and **Priority**.

The project combines traditional Machine Learning with Transformer-based Deep Learning (DistilBERT) to build an explainable and production-ready AI solution.

---

# 📌 Features

✅ Predict Ticket Queue

- Technical Support
- Billing
- Sales
- Account Management
- Customer Service
- etc.

---

✅ Predict Ticket Type

- Problem
- Incident
- Request
- Question
- Complaint

---

✅ Predict Ticket Priority

- Low
- Medium
- High
- Critical

---

✅ DistilBERT NLP Model

Uses a pretrained **DistilBERT Transformer** to understand the ticket subject and description.

---

✅ Explainable AI (XAI)

Traditional ML Models

- SHAP Summary Plot
- SHAP Waterfall Plot
- SHAP Dependence Plot

Deep Learning Model

- Token-level Attention Visualization
- Shows which words influenced DistilBERT predictions

---

✅ Beautiful Streamlit Dashboard

Includes

- Home Page
- Prediction Page
- Explainability Page
- Model Information
- Dataset Insights

---

# 🏗️ Project Architecture

```
                    Customer Ticket
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
   Subject                          Description
        │                                     │
        └──────────────┬──────────────────────┘
                       │
               Text Preprocessing
                       │
              DistilBERT Embeddings
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
 Queue Model     Type Model     Priority Model
        │              │               │
        └──────────────┼───────────────┘
                       │
                 Predictions
                       │
              SHAP Explainability
                       │
          Streamlit Interactive Dashboard
```

---

# 📂 Project Structure

```
AI-Customer-Support-System/

│
├── app.py
├── requirements.txt
├── README.md
│
├── backend/
│   ├── main.py
│   ├── predict.py
│   ├── schemas.py
│   └── utils.py
│
├── frontend/
│   ├── Home.py
│   ├── pages/
│   │     ├── Prediction.py
│   │     ├── Explainability.py
│   │     ├── Dataset.py
│   │     └── About.py
│
├── models/
│   ├── queue_model.pkl
│   ├── type_model.pkl
│   ├── priority_model.pkl
│   ├── vectorizer.pkl
│   └── distilbert_model/
│
├── explainability/
│   ├── shap_utils.py
│   ├── attention.py
│   └── plots.py
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── processed.csv
│
└── notebooks/
    ├── EDA.ipynb
    ├── Training.ipynb
    └── SHAP.ipynb
```

---

# ⚙️ Tech Stack

## Programming Language

- Python 3.11+

---

## Backend

- FastAPI
- Uvicorn
- Pydantic

---

## Frontend

- Streamlit

---

## Machine Learning

- Scikit-learn
- XGBoost
- Random Forest
- Logistic Regression

---

## NLP

- HuggingFace Transformers
- DistilBERT
- Tokenizer

---

## Explainable AI

- SHAP
- Attention Visualization

---

## Visualization

- Matplotlib
- Plotly
- Seaborn

---

# 📊 Dataset

Each support ticket contains:

| Feature | Description |
|----------|-------------|
| Subject | Ticket title |
| Description | Customer issue |
| Queue | Target queue |
| Type | Ticket type |
| Priority | Ticket urgency |

Example

| Subject | Description | Queue | Type | Priority |
|----------|-------------|-------|------|----------|
| Unable to login | Password reset not working | Account | Incident | High |

---

# 🧠 Models Used

## Traditional Machine Learning

- Logistic Regression
- Random Forest
- XGBoost

Used for tabular classification.

---

## Transformer Model

DistilBERT

Used for understanding ticket text.

Advantages

- Better contextual understanding
- Handles long descriptions
- Learns semantic meaning
- Higher accuracy

---

# 🔍 Explainable AI

The project includes Explainable AI techniques to understand model predictions.

---

## SHAP Summary Plot

Shows

- Most important features
- Positive influence
- Negative influence

Useful for explaining the global behavior of ML models.

---

## SHAP Waterfall Plot

Explains

Why one specific prediction was made.

Displays

Base Value

↓

Feature Contributions

↓

Final Prediction

---

## SHAP Dependence Plot

Shows

How changing one feature affects predictions.

---

## DistilBERT Attention Visualization

Displays

```
Unable to login after password reset

Unable     ███████
login      ███████████████
password   ██████████
reset      ████████████
after      ██
to         █
```

This helps identify which words the model focused on while making predictions.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Customer-Support-System.git
```

Move into the project

```bash
cd AI-Customer-Support-System
```

Create virtual environment

Windows

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Backend

```bash
cd backend
uvicorn main:app --reload
```

API runs on

```
http://127.0.0.1:8000
```

---

# ▶️ Running the Frontend

```bash
streamlit run app.py
```

Dashboard opens at

```
http://localhost:8501
```

---

# 📡 API Endpoint

## POST

```
/predict
```

Request

```json
{
    "subject":"Unable to login",
    "description":"Password reset is not working"
}
```

Response

```json
{
    "queue_prediction":"Technical Support",
    "type_prediction":"Incident",
    "priority_prediction":"High"
}
```

---

# 📈 Future Improvements

- Multi-language Support
- Voice Ticket Classification
- LLM-based Ticket Summarization
- Email Integration
- Automatic Ticket Routing
- Ticket Similarity Search
- Chatbot Integration
- Real-time Monitoring Dashboard

---

# 🎯 Applications

- Help Desk Automation
- IT Service Management
- CRM Systems
- Customer Support Centers
- SaaS Platforms
- Enterprise Ticket Routing

---

# 👨‍💻 Author

**Your Name**

AI & Machine Learning Project

Built using

- Python
- FastAPI
- Streamlit
- DistilBERT
- Scikit-learn
- SHAP
- HuggingFace Transformers

---

# 📄 License

This project is developed for educational and research purposes.