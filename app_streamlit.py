import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
st.markdown("""
<h1 style='text-align:center; color:white;'>
📊 Twitter Sentiment Analysis Dashboard
</h1>

<h4 style='text-align:center; color:#B0B0B0;'>
Analyze Trends • Track Sentiment • Discover Insights
</h4>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown("""
<h1 style='text-align:center; color:#00BFFF;'>
🌐Social Media Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

# ---------------- THEME ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #050505;
}

/* Neon icons scattered in background */
.neon-bg {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
}

.neon-icon {
    position: fixed;
    opacity: 0.40;
    font-size: 45px;
    font-weight: bold;
}

</style>

<div class="neon-bg">

<div class="neon-icon" style="top:5%;left:5%;color:#00BFFF;">#</div>
<div class="neon-icon" style="top:10%;left:20%;color:#8A2BE2;">💬</div>
<div class="neon-icon" style="top:8%;left:40%;color:#00BFFF;">📊</div>
<div class="neon-icon" style="top:12%;left:60%;color:#FF1493;">❤️</div>
<div class="neon-icon" style="top:6%;left:80%;color:#00BFFF;">🌐</div>

<div class="neon-icon" style="top:25%;left:10%;color:#8A2BE2;">📱</div>
<div class="neon-icon" style="top:30%;left:30%;color:#00BFFF;">💬</div>
<div class="neon-icon" style="top:35%;left:50%;color:#FF1493;">📊</div>
<div class="neon-icon" style="top:28%;left:70%;color:#00BFFF;">📈</div>
<div class="neon-icon" style="top:32%;left:90%;color:#8A2BE2;">#</div>

<div class="neon-icon" style="top:50%;left:5%;color:#00BFFF;">🌐</div>
<div class="neon-icon" style="top:55%;left:25%;color:#FF1493;">❤️</div>
<div class="neon-icon" style="top:48%;left:45%;color:#8A2BE2;">💬</div>
<div class="neon-icon" style="top:58%;left:65%;color:#00BFFF;">📊</div>
<div class="neon-icon" style="top:52%;left:85%;color:#FF1493;">📈</div>

<div class="neon-icon" style="top:72%;left:10%;color:#8A2BE2;">📱</div>
<div class="neon-icon" style="top:80%;left:30%;color:#00BFFF;">💬</div>
<div class="neon-icon" style="top:75%;left:50%;color:#FF1493;">❤️</div>
<div class="neon-icon" style="top:85%;left:70%;color:#00BFFF;">📈</div>
<div class="neon-icon" style="top:78%;left:90%;color:#8A2BE2;">#</div>
            <!-- Graph -->
<div class="neon-icon" style="top:18%;left:50%;color:#00BFFF;">📈</div>

<!-- Social Media -->
<div class="neon-icon" style="top:70%;left:40%;color:#8A2BE2;">📱</div>

<!-- Chat Bubble 1 -->
<div class="neon-icon" style="top:22%;left:75%;color:#00BFFF;">💬</div>

<!-- Chat Bubble 2 -->
<div class="neon-icon" style="top:82%;left:20%;color:#00BFFF;">💬</div>

<!-- Love Symbol -->
<div class="neon-icon" style="top:40%;left:88%;color:#FF1493;">❤️</div>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Dashboard Metrics Heading */
.metrics-title {
    color: #00BFFF;
    font-size: 28px;
    font-weight: bold;
}

/* KPI Labels */
[data-testid="stMetricLabel"] {
    color: #00BFFF !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* KPI Values */
[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 34px !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "dataset.csv"

df = pd.read_csv(CSV_FILE)

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "dataset.csv"

df = pd.read_csv(DATA_FILE)
#st.write(df.columns)
# Create Tweet Length column
df["length"] = df["post_text"].astype(str).apply(len)

st.success("Dataset Loaded Successfully!")

# ---------------- DATASET PREVIEW ----------------

# ---------------- DATASET PREVIEW ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>📄 Dataset Preview</h4>
</div>
""", unsafe_allow_html=True)

st.dataframe(
    df[["platform", "username", "post_text", "sentiment_label"]].head(5),
    use_container_width=True
)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)

# ---------------- SIDEBAR FILTER ----------------

st.sidebar.header("📊 Filter Options")

sentiments = ["All"] + list(df["sentiment_label"].dropna().unique())

option = st.sidebar.selectbox(
    "Choose Sentiment",
    sentiments
)

if option != "All":
    filtered_df = df[df["sentiment_label"] == option]
else:
    filtered_df = df.copy()

# ---------------- KPI CARDS ----------------

st.markdown(
    '<p class="metrics-title">📊 Dashboard Metrics </p>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "📢 Total Posts",
    len(filtered_df)
)

col2.metric(
    "💚 Positive Posts",
    (filtered_df["sentiment_label"] == "Positive").sum()
)

col3.metric(
    "❤️ Negative Posts",
    (filtered_df["sentiment_label"] == "Negative").sum()
)

# ---------------- SENTIMENT COUNTS ----------------
st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
">
<h4 style='color:white;'>
📈 Twitter Sentiment Analysis</h4>
</div>
""", unsafe_allow_html=True)

sentiment_counts = filtered_df["sentiment_label"].value_counts()

st.dataframe(
    sentiment_counts.reset_index().rename(
        columns={"index": "😊 Sentiment", "sentiment_label": "📊 Count"}
    )
)
st.markdown(f"""
<div style="color:#39FF14;font-size:20px;">
💚 Positive : {sentiment_counts.get('Positive',0)}
</div>

<div style="color:#FF3131;font-size:20px;">
❤️ Negative : {sentiment_counts.get('Negative',0)}
</div>

<div style="color:#00BFFF;font-size:20px;">
📊 Total : {len(filtered_df)}
</div>
""", unsafe_allow_html=True)
# ---------------- SENTIMENT BAR CHART ----------------

# ---------------- SENTIMENT ANALYSIS ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>📊 Sentiment Analysis</h4>
</div>
""", unsafe_allow_html=True)

sentiment_counts = filtered_df["sentiment_label"].value_counts()

fig_sent, ax_sent = plt.subplots(figsize=(10,5))

# Black Background
fig_sent.patch.set_facecolor("black")
ax_sent.set_facecolor("black")

ax_sent.bar(
    sentiment_counts.index,
    sentiment_counts.values,
    color="#E5E5E5",      # White Bars
    edgecolor="#B4B4B4"   # Grey Border
)

ax_sent.set_title(
    "📊 Sentiment Analysis",
    color="#E5E5E5",
    fontsize=16,
    fontweight="bold"
)

ax_sent.set_xlabel(
    "Sentiment",
    color="#E5E5E5"
)

ax_sent.set_ylabel(
    "Count",
    color="#E5E5E5"
)

ax_sent.tick_params(colors="#E5E5E5")

for spine in ax_sent.spines.values():
    spine.set_color("#B4B4B4")

st.pyplot(fig_sent)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)
# ---------------- PIE CHART ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>🥧 Sentiment Distribution</h4>
</div>
""", unsafe_allow_html=True)

sentiment_counts = filtered_df["sentiment_label"].value_counts()

# Positive = White
# Negative = Grey
# Neutral = Off White
colors = [
    "#E5E5E5",  # White
    "#B4B4B4",  # Grey
    "#464444"   # Off White
]

fig_pie, ax_pie = plt.subplots(figsize=(7,7))

# Black Background
fig_pie.patch.set_facecolor("black")
ax_pie.set_facecolor("black")

ax_pie.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    colors=colors[:len(sentiment_counts)],
    textprops={
        "color": "white",
        "fontsize": 12,
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "#0E1117",
        "linewidth": 2
    }
)

ax_pie.set_title(
    "🥧 Sentiment Distribution",
    color="#E5E5E5",
    fontsize=16,
    fontweight="bold"
)

st.pyplot(fig_pie)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)
# ---------------- TWEET LENGTH DISTRIBUTION ----------------
# ---------------- TWEET LENGTH DISTRIBUTION ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>📏 Tweet Length Distribution</h4>
</div>
""", unsafe_allow_html=True)

# Create tweet length column
filtered_df["length"] = filtered_df["post_text"].astype(str).apply(len)

fig_len, ax_len = plt.subplots(figsize=(10,5))

# Black Background
fig_len.patch.set_facecolor("black")
ax_len.set_facecolor("black")

ax_len.hist(
    filtered_df["length"],
    bins=30,
    color="#E5E5E5",      # White
    edgecolor="#B4B4B4"   # Grey
)

ax_len.set_title(
    "📏 Tweet Length Distribution",
    color="#E5E5E5",
    fontsize=16,
    fontweight="bold"
)

ax_len.set_xlabel(
    "Tweet Length",
    color="#E5E5E5"
)

ax_len.set_ylabel(
    "Frequency",
    color="#E5E5E5"
)

ax_len.tick_params(colors="#E5E5E5")

for spine in ax_len.spines.values():
    spine.set_color("#B4B4B4")

st.pyplot(fig_len)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)

# ---------------- AVERAGE POST LENGTH BY SENTIMENT ----------------

# ---------------- AVERAGE POSTS BY SENTIMENT ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>📈 Average Posts by Sentiment</h4>
</div>
""", unsafe_allow_html=True)

avg_posts = filtered_df.groupby("sentiment_label").size()

fig_avg, ax_avg = plt.subplots(figsize=(10,5))

# Black Background
fig_avg.patch.set_facecolor("black")
ax_avg.set_facecolor("black")

ax_avg.bar(
    avg_posts.index,
    avg_posts.values,
    color="#E5E5E5",      # White Bars
    edgecolor="#B4B4B4"   # Grey Border
)

ax_avg.set_title(
    "📈 Average Posts by Sentiment",
    color="#E5E5E5",
    fontsize=16,
    fontweight="bold"
)

ax_avg.set_xlabel(
    "Sentiment",
    color="#E5E5E5"
)

ax_avg.set_ylabel(
    "Average Posts",
    color="#E5E5E5"
)

ax_avg.tick_params(colors="#E5E5E5")

for spine in ax_avg.spines.values():
    spine.set_color("#B4B4B4")

st.pyplot(fig_avg)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)


# ---------------- WORD CLOUD ----------------
# ---------------- GENERAL WORD CLOUD ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>☁️ General Word Cloud</h4>
</div>
""", unsafe_allow_html=True)

all_text = " ".join(
    filtered_df["post_text"]
    .fillna("")
    .astype(str)
)

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="black",
    colormap="Greys"
).generate(all_text)

fig_wc, ax_wc = plt.subplots(figsize=(10,5))

# Black Background
fig_wc.patch.set_facecolor("black")
ax_wc.set_facecolor("black")

ax_wc.imshow(wordcloud, interpolation="bilinear")
ax_wc.axis("off")

st.pyplot(fig_wc)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)

# ---------------- POSITIVE WORD CLOUD ----------------
# ---------------- POSITIVE WORD CLOUD ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>💚 Positive Word Cloud</h4>
</div>
""", unsafe_allow_html=True)

positive_df = filtered_df[
    filtered_df["sentiment_label"] == "Positive"
]

if len(positive_df) > 0:

    positive_text = " ".join(
        positive_df["post_text"]
        .fillna("")
        .astype(str)
    )

    positive_wc = WordCloud(
        width=800,
        height=400,
        background_color="black",
        colormap="Greens"
    ).generate(positive_text)

    fig_pos, ax_pos = plt.subplots(figsize=(10,5))

    fig_pos.patch.set_facecolor("black")
    ax_pos.set_facecolor("black")

    ax_pos.imshow(positive_wc, interpolation="bilinear")
    ax_pos.axis("off")

    st.pyplot(fig_pos)

else:
    st.warning("⚠️ No positive tweets available.")

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)
# ---------------- NEGATIVE WORD CLOUD ----------------
# ---------------- NEGATIVE WORD CLOUD ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>❤️ Negative Word Cloud</h4>
</div>
""", unsafe_allow_html=True)

negative_df = filtered_df[
    filtered_df["sentiment_label"] == "Negative"
]

if len(negative_df) > 0:

    negative_text = " ".join(
        negative_df["post_text"]
        .fillna("")
        .astype(str)
    )

    negative_wc = WordCloud(
        width=800,
        height=400,
        background_color="black",
        colormap="Reds"
    ).generate(negative_text)

    fig_neg, ax_neg = plt.subplots(figsize=(10,5))

    fig_neg.patch.set_facecolor("black")
    ax_neg.set_facecolor("black")

    ax_neg.imshow(negative_wc, interpolation="bilinear")
    ax_neg.axis("off")

    st.pyplot(fig_neg)

else:
    st.warning("⚠️ No negative tweets available.")

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)
# ---------------- TOP 10 MOST FREQUENT WORDS ----------------
# ---------------- TOP 10 MOST FREQUENT WORDS ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>🔤 Top 10 Most Frequent Words</h4>
</div>
""", unsafe_allow_html=True)

from collections import Counter

all_words = " ".join(
    filtered_df["post_text"]
    .fillna("")
    .astype(str)
).split()

word_freq = Counter(all_words).most_common(10)

words = [word for word, count in word_freq]
counts = [count for word, count in word_freq]

fig_words, ax_words = plt.subplots(figsize=(10,5))

# Black Background
fig_words.patch.set_facecolor("black")
ax_words.set_facecolor("black")

ax_words.bar(
    words,
    counts,
    color="#E5E5E5",      # White Bars
    edgecolor="#B4B4B4"   # Grey Border
)

ax_words.set_title(
    "🔤 Top 10 Most Frequent Words",
    color="#E5E5E5",
    fontsize=16,
    fontweight="bold"
)

ax_words.set_xlabel(
    "Words",
    color="#E5E5E5"
)

ax_words.set_ylabel(
    "Frequency",
    color="#E5E5E5"
)

ax_words.tick_params(colors="#E5E5E5")
plt.xticks(rotation=45)

for spine in ax_words.spines.values():
    spine.set_color("#B4B4B4")

st.pyplot(fig_words)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)
# ---------------- TOP POSITIVE WORDS ----------------

# ---------------- TOP POSITIVE WORDS ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>💚 Top Positive Words</h4>
</div>
""", unsafe_allow_html=True)

from collections import Counter

positive_words = " ".join(
    filtered_df[
        filtered_df["sentiment_label"] == "Positive"
    ]["post_text"]
    .fillna("")
    .astype(str)
).split()

positive_freq = Counter(positive_words).most_common(10)

words = [word for word, count in positive_freq]
counts = [count for word, count in positive_freq]

fig_pos_words, ax_pos_words = plt.subplots(figsize=(10,5))

fig_pos_words.patch.set_facecolor("black")
ax_pos_words.set_facecolor("black")

ax_pos_words.bar(
    words,
    counts,
    color="#E5E5E5",
    edgecolor="#B4B4B4"
)

ax_pos_words.set_title(
    "💚 Top Positive Words",
    color="#E5E5E5",
    fontsize=16,
    fontweight="bold"
)

ax_pos_words.tick_params(colors="#E5E5E5")
plt.xticks(rotation=45)

for spine in ax_pos_words.spines.values():
    spine.set_color("#B4B4B4")

st.pyplot(fig_pos_words)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)
# ---------------- TOP NEGATIVE WORDS ----------------
# ---------------- TOP NEGATIVE WORDS ----------------

st.markdown("""
<div style="
border:1px solid #333333;
padding:15px;
border-radius:10px;
background-color:#0E1117;
margin-bottom:20px;
">
<h4 style='color:white;'>❤️ Top Negative Words</h4>
</div>
""", unsafe_allow_html=True)

from collections import Counter

negative_words = " ".join(
    filtered_df[
        filtered_df["sentiment_label"] == "Negative"
    ]["post_text"]
    .fillna("")
    .astype(str)
).split()

negative_freq = Counter(negative_words).most_common(10)

words = [word for word, count in negative_freq]
counts = [count for word, count in negative_freq]

fig_neg_words, ax_neg_words = plt.subplots(figsize=(10,5))

fig_neg_words.patch.set_facecolor("black")
ax_neg_words.set_facecolor("black")

ax_neg_words.bar(
    words,
    counts,
    color="#E5E5E5",
    edgecolor="#B4B4B4"
)

ax_neg_words.set_title(
    "❤️ Top Negative Words",
    color="#E5E5E5",
    fontsize=16,
    fontweight="bold"
)

ax_neg_words.tick_params(colors="#E5E5E5")
plt.xticks(rotation=45)

for spine in ax_neg_words.spines.values():
    spine.set_color("#B4B4B4")

st.pyplot(fig_neg_words)

st.markdown("""
<hr style="border:1px solid #333333;">
""", unsafe_allow_html=True)
# ---------------- CONCLUSION ----------------

st.markdown("""
<h3 style='color:#E5E5E5;'>
📌 Conclusion
</h3>
""", unsafe_allow_html=True)

st.markdown("""
<div style='color:#E5E5E5; font-size:18px;'>

The Twitter Sentiment Analysis Dashboard provides valuable insights into public sentiment by analyzing tweet data.

✅ Positive and negative sentiments were identified successfully.

✅ Frequently used words helped reveal trending topics.

✅ Word clouds highlighted common discussion patterns.

✅ Visualizations such as bar charts, pie charts, and sentiment distributions made the analysis easier to understand.

Overall, this dashboard helps users monitor public opinion, identify trends, and make data-driven decisions using social media analytics.

</div>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<h2 style='text-align:center; color:#00BFFF;'>
 Thank You!
</h2>

<p style='text-align:center; color:#E5E5E5;'>
Thank you for exploring the Twitter Sentiment Analysis Dashboard.
This project demonstrates how social media analytics can be used
to understand public sentiment and identify trending discussions.
</p>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<center>
<h4 style='color:#00BFFF;'>
📊 Twitter Sentiment Analysis Dashboard | Internship Project 2026
</h4>
</center>
""", unsafe_allow_html=True)
