import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

st.title("📊 Social Media Analytics Dashboard")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:

    df = pd.read_csv(file, encoding="latin-1")

    st.success("Dataset loaded successfully!")

    st.write("### Preview")
    st.write(df.head())

    # correct text column (your dataset)
    text_column = df.columns[3]

    # sentiment function
    def get_sentiment(text):
        analysis = TextBlob(str(text))
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"

    df["Sentiment"] = df[text_column].apply(get_sentiment)

    # show counts
    st.write("### Sentiment Counts")
    st.write(df["Sentiment"].value_counts())

    # ---------------- PIE CHART ----------------
    st.write("### Pie Chart")

    fig1, ax1 = plt.subplots()
    df["Sentiment"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax1
    )
    ax1.set_ylabel("")
    st.pyplot(fig1)

    # ---------------- BAR CHART ----------------
    st.write("### Bar Chart")

    fig2, ax2 = plt.subplots()
    df["Sentiment"].value_counts().plot(
        kind="bar",
        ax=ax2
    )
    st.pyplot(fig2)