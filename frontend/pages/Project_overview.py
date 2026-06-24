import streamlit as st
import pandas as pd


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Project Overview",
    page_icon="🤖",
    layout="wide"
)


# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.big-title {
    font-size: 50px;
    font-weight: bold;
    color: #4FC3F7;
    text-align: center;
    margin-bottom: 10px;
}

.sub-title {
    font-size: 22px;
    color: #D1D5DB;
    text-align: center;
    margin-bottom: 40px;
}

.section-title {
    font-size: 30px;
    font-weight: bold;
    color: #4FC3F7;
    margin-top: 35px;
    margin-bottom: 20px;
}

.card {
    background-color: #161B22;
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #30363D;
    margin-bottom: 25px;
}

.metric-card {
    background: linear-gradient(
        135deg,
        #1E3A5F,
        #16213E
    );

    padding: 30px;

    border-radius: 20px;

    text-align: center;

    border: 1px solid #4FC3F7;
}

.metric-title {
    color: #D1D5DB;
    font-size: 20px;
}

.metric-value {
    color: #4FC3F7;
    font-size: 34px;
    font-weight: bold;
}

.metric-score {
    color: white;
    font-size: 20px;
    margin-top: 10px;
}

.tech-badge {
    display: inline-block;
    padding: 10px 18px;
    margin: 6px;
    border-radius: 30px;
    background-color: #1F2937;
    color: white;
    font-size: 15px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 60px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# =========================================
# HERO SECTION
# =========================================

st.markdown(
    """
    <div class="big-title">
    🤖 AI Powered Customer Support Automation
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
    Intelligent Multi-Stage Ticket Routing System
    using NLP, Transformers & Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# PROJECT OVERVIEW
# =========================================

st.markdown(
    '<div class="section-title">📌 Project Overview</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

This project is an end-to-end AI-powered customer support automation system
designed to automatically classify customer support tickets.

The system predicts:

<ul>

<li><b>Queue Prediction</b> → Which department/team should handle the issue</li>

<li><b>Type Prediction</b> → Nature/category of customer issue</li>

<li><b>Priority Prediction</b> → Severity level of ticket</li>

</ul>

The project combines:

<ul>

<li>Transformer-based Deep Learning</li>

<li>Traditional Machine Learning</li>

<li>Natural Language Processing (NLP)</li>

<li>Feature Engineering</li>

<li>Multi-Stage Prediction Pipeline</li>

</ul>

This architecture is inspired by real-world enterprise customer support systems.

</div>
""", unsafe_allow_html=True)


# =========================================
# SYSTEM ARCHITECTURE
# =========================================

st.markdown(
    '<div class="section-title">⚙️ System Architecture</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

<div style="text-align:center; line-height:2.2; font-size:18px;">

📥 <b>Customer Input</b><br>
(Subject + Description)

⬇️

🧹 <b>Text Cleaning & Preprocessing</b>

⬇️

🤖 <b>DistilBERT Transformer</b><br>
Queue Prediction

⬇️

📊 <b>TF-IDF + XGBoost</b><br>
Type Prediction

⬇️

⚡ <b>TF-IDF + Queue + Type Features</b><br>
Priority Prediction using XGBoost

⬇️

✅ <b>Final Intelligent Ticket Routing</b>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================
# MODEL PERFORMANCE
# =========================================

st.markdown(
    '<div class="section-title">📊 Model Performance</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="metric-card">

    <h3 style="color:white;">
    Queue Prediction
    </h3>

    <h2 style="color:#4FC3F7;">
    DistilBERT
    </h2>

    <p style="font-size:20px;">
    Accuracy: 72%
    </p>

    <p style="font-size:20px;">
    F1 Score: 0.70
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="metric-card">

    <h3 style="color:white;">
    Type Prediction
    </h3>

    <h2 style="color:#4FC3F7;">
    TF-IDF + XGBoost
    </h2>

    <p style="font-size:20px;">
    Accuracy: 89%
    </p>

    <p style="font-size:20px;">
    F1 Score: 0.85
    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="metric-card">

    <h3 style="color:white;">
    Priority Prediction
    </h3>

    <h2 style="color:#4FC3F7;">
    XGBoost
    </h2>

    <p style="font-size:20px;">
    Accuracy: 79%
    </p>

    <p style="font-size:20px;">
    F1 Score: 0.77
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================
# TECHNOLOGIES USED
# =========================================

st.markdown(
    '<div class="section-title">🛠️ Technologies Used</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

<span class="tech-badge">Python</span>

<span class="tech-badge">Streamlit</span>

<span class="tech-badge">FastAPI</span>

<span class="tech-badge">DistilBERT</span>

<span class="tech-badge">Transformers</span>

<span class="tech-badge">XGBoost</span>

<span class="tech-badge">TF-IDF</span>

<span class="tech-badge">Scikit-Learn</span>

<span class="tech-badge">PyTorch</span>

<span class="tech-badge">Docker</span>

<span class="tech-badge">Render Deployment</span>

<span class="tech-badge">Hugging Face Spaces</span>

</div>
""", unsafe_allow_html=True)


# =========================================
# KEY FEATURES
# =========================================

st.markdown(
    '<div class="section-title">🚀 Key Features</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

    ✅ Multi-Stage Prediction Pipeline

    ✅ Real-Time AI Predictions

    ✅ Transformer-Based NLP

    ✅ Automated Ticket Routing

    ✅ Intelligent Priority Detection

    ✅ Enterprise-Level Workflow

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">

    ✅ FastAPI Production Backend

    ✅ Docker Containerization

    ✅ Streamlit Interactive UI

    ✅ Scalable Deployment Architecture

    ✅ Modular Code Structure

    ✅ Production Ready System

    </div>
    """, unsafe_allow_html=True)


# =========================================
# BUSINESS IMPACT
# =========================================

st.markdown(
    '<div class="section-title">💼 Business Impact</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

This AI system can help organizations:

<ul>

<li>Reduce manual ticket triaging effort</li>

<li>Improve response time</li>

<li>Automatically route tickets to correct teams</li>

<li>Reduce operational costs</li>

<li>Improve customer satisfaction</li>

<li>Enable scalable AI-powered customer support</li>

</ul>

</div>
""", unsafe_allow_html=True)


# =========================================
# FOOTER
# =========================================

st.markdown("""
<div class="footer">

Built with NLP, Transformers, FastAPI & Machine Learning

</div>
""", unsafe_allow_html=True)