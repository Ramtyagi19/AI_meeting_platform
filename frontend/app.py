import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


# PAGE CONFIG


st.set_page_config(
    page_title="AI Meeting Platform",
    layout="wide"
)


# TITLE

st.title("🧠 AI Meeting Intelligence Platform")


# SIDEBAR MENU


menu = st.sidebar.radio(
    "Navigation",
    [
        "Ingest Meeting",
        "View Meeting",
        "Sentiment Analysis",
        "Ask Questions"
    ]
)


# INGEST MEETING


if menu == "Ingest Meeting":

    st.header("📥 Ingest Meeting Transcript")

    meeting_id = st.text_input("Meeting ID")

    transcript = st.text_area(
        "Enter Meeting Transcript",
        height=250
    )

    if st.button("Submit Transcript"):

        payload = {
            "meeting_id": meeting_id,
            "text": transcript
        }

        response = requests.post(
            f"{BASE_URL}/ingest",
            json=payload
        )

        st.success("Transcript Submitted Successfully")

        st.json(response.json())


# VIEW MEETING


elif menu == "View Meeting":

    st.header("📄 View Meeting Data")

    meeting_id = st.text_input("Enter Meeting ID")

    if st.button("Fetch Meeting"):

        response = requests.get(
            f"{BASE_URL}/meeting/{meeting_id}"
        )

        data = response.json()

        st.subheader("Meeting Transcripts")

        if len(data["transcripts"]) == 0:
            st.warning("No transcripts found")
        else:
            for idx, t in enumerate(data["transcripts"]):
                st.write(f"{idx+1}. {t}")


# SENTIMENT ANALYSIS

elif menu == "Sentiment Analysis":

    st.header("😊 Sentiment Analysis")

    text = st.text_area(
        "Enter Text",
        height=200
    )

    if st.button("Analyze"):

        response = requests.post(
            f"{BASE_URL}/sentiment",
            json={"text": text}
        )

        sentiment = response.json()["sentiment"]

        st.metric(
            "Sentiment Score",
            round(sentiment, 2)
        )

        if sentiment > 0:
            st.success("Positive Sentiment")

        elif sentiment < 0:
            st.error("Negative Sentiment")

        else:
            st.warning("Neutral Sentiment")


# ASK QUESTIONS


elif menu == "Ask Questions":

    st.header("🤖 Ask AI About Meetings")

    question = st.text_input(
        "Enter Your Question"
    )

    if st.button("Ask AI"):

        response = requests.post(
            f"{BASE_URL}/ask",
            json={"query": question}
        )

        result = response.json()

        st.subheader("AI Response")

        st.write(result["answer"])