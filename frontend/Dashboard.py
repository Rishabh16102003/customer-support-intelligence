import os
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


BACKEND_URL = st.secrets["BACKEND_URL"]

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="AI Customer Support System",
    page_icon="🎫",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.title("🎫 Support Intelligence")
    st.markdown("---")
    st.caption(f"Backend: {BACKEND_URL}")
    st.markdown("""
    ### Features
    ✅ Queue Prediction  
    ✅ Ticket Type Prediction  
    ✅ Priority Prediction  
    ✅ Attention Visualization
    """)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 AI Customer Support System")
st.caption(
    "Predict Ticket Queue, Type, Priority and Visualize DistilBERT Attention Scores"
)

st.divider()

# --------------------------------------------------
# Input Section
# --------------------------------------------------
st.subheader("📝 Ticket Information")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input(
        "Subject",
        placeholder="Enter ticket subject..."
    )

with col2:
    st.empty()

description = st.text_area(
    "Description",
    height=180,
    placeholder="Enter ticket description..."
)

st.divider()

# --------------------------------------------------
# Buttons
# --------------------------------------------------
col1, col2, col3 = st.columns([1, 1, 5])

with col1:
    predict_btn = st.button(
        "🚀 Predict",
        use_container_width=True
    )

with col2:
    attention_btn = st.button(
        "📈 Attention",
        use_container_width=True
    )

# --------------------------------------------------
# Prediction Section
# --------------------------------------------------
if predict_btn:

    if not subject.strip() or not description.strip():
        st.warning("Please enter Subject and Description.")
        st.stop()

    payload = {
        "subject": subject,
        "description": description
    }

    with st.spinner("Predicting..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/predict",
                json=payload,
                timeout=60
            )

            if response.status_code != 200:
                st.error(f"Backend Error: {response.status_code}")
                st.write(response.text)
                st.stop()

            result = response.json()

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to FastAPI backend.")
            st.stop()

        except requests.exceptions.Timeout:
            st.error("Backend request timed out.")
            st.stop()

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
            st.stop()

        except ValueError:
            st.error("Backend returned invalid JSON.")
            st.stop()

        except Exception as e:
            st.error(f"Unexpected error: {e}")
            st.stop()

    st.subheader("🎯 Predictions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Queue",
            value=result.get("queue_prediction", "N/A")
        )

    with col2:
        st.metric(
            label="Type",
            value=result.get("type_prediction", "N/A")
        )

    with col3:
        st.metric(
            label="Priority",
            value=result.get("priority_prediction", "N/A")
        )

# --------------------------------------------------
# Attention Scores Section
# --------------------------------------------------
if attention_btn:

    if not subject.strip() or not description.strip():
        st.warning("Please enter Subject and Description.")
        st.stop()

    payload = {
        "subject": subject,
        "description": description
    }

    with st.spinner("Fetching Attention Scores..."):
        try:
            response1 = requests.post(
                f"{BACKEND_URL}/attention",
                json=payload,
                timeout=60
            )

            if response1.status_code != 200:
                st.error(f"Backend Error: {response1.status_code}")
                st.write(response1.text)
                st.stop()

            data = response1.json()

            prediction = data.get("pred", "N/A")
            df = pd.DataFrame(data.get("df", []))
            df_exclusive = pd.DataFrame(data.get("df_exclusive", []))

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to FastAPI backend.")
            st.stop()

        except requests.exceptions.Timeout:
            st.error("Backend request timed out.")
            st.stop()

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
            st.stop()

        except ValueError:
            st.error("Backend returned invalid JSON.")
            st.stop()

        except Exception as e:
            st.error(f"Unexpected error: {e}")
            st.stop()

    st.divider()
    st.subheader("📈 Attention Analysis")
    st.info(f"Predicted Label: **{prediction}**")

    tab1, tab2, tab3 = st.tabs(
        ["Top Tokens", "Filtered Tokens", "Data"]
    )

    # -----------------------------------
    # Tab 1 - Top Tokens
    # -----------------------------------
    with tab1:
        if not df.empty and "token" in df.columns and "attention" in df.columns:
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            ax1.barh(df["token"], df["attention"])
            ax1.invert_yaxis()
            ax1.set_title("Top Attention Tokens")
            ax1.set_xlabel("Attention Score")
            st.pyplot(fig1)
            plt.close(fig1)
        else:
            st.warning("No attention token data available.")

    # -----------------------------------
    # Tab 2 - Filtered Tokens
    # -----------------------------------
    with tab2:
        if not df_exclusive.empty and "token" in df_exclusive.columns and "attention" in df_exclusive.columns:
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            ax2.barh(df_exclusive["token"], df_exclusive["attention"])
            ax2.invert_yaxis()
            ax2.set_title("Attention Tokens (Without Special Tokens)")
            ax2.set_xlabel("Attention Score")
            st.pyplot(fig2)
            plt.close(fig2)
        else:
            st.warning("No filtered attention token data available.")

    # -----------------------------------
    # Tab 3 - Raw Data
    # -----------------------------------
    with tab3:
        st.write("Raw Attention Scores")
        if not df.empty:
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No raw attention data available.")

        st.write("Filtered Attention Scores")
        if not df_exclusive.empty:
            st.dataframe(df_exclusive, use_container_width=True)
        else:
            st.info("No filtered attention data available.")
