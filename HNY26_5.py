import streamlit as st
import requests
import datetime
import pytz
from streamlit_lottie import st_lottie
from streamlit_confetti import confetti
import time

# Page setup
st.set_page_config(page_title="2026 Celebration Showcase", page_icon="🎆", layout="wide")

# Styling for metrics, background, and top-right icons
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
.stApp {
    background: linear-gradient(to bottom, #000428, #004e92);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stMetricLabel"] {
    color: #FFFFFF !important;
    font-size: 1.2rem !important;
    font-weight: bold !important;
}
[data-testid="stMetricValue"] {
    color: #00d4ff !important;
    font-size: 2.5rem !important;
}
div[data-testid="stMetric"] {
    background-color: rgba(255, 255, 255, 0.15) !important;
    border-radius: 15px;
    padding: 20px;
    border: 1px solid rgba(0, 212, 255, 0.4);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
.top-right-bar {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-bottom: 20px;
    gap: 5px;
}
.top-right-bar a {
    color: white;
    text-decoration: none;
    margin-left: 10px;
    font-size: 24px;
}
.top-right-bar a:hover {
    color: #00d4ff;
}
.top-right-bar .name {
    font-weight: bold;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

# Top-right social links with name below
st.markdown("""
<div class="top-right-bar">
    <div>
        <a href="https://www.linkedin.com/in/ankonbanik/" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/AnkonBanik" target="_blank"><i class="fab fa-github"></i></a>
        <a href="mailto:ankonbnk@gmail.com" target="_blank"><i class="fas fa-envelope"></i></a>
    </div>
    <div class="name">Ankon Banik</div>
</div>
""", unsafe_allow_html=True)

# Function to load Lottie animations
@st.cache_data
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()
    except:
        return None

lottie_fireworks = load_lottieurl(
    "https://lottie.host/8695847e-8984-44a3-9036-613346d506d8/S1Wv7h5H6A.json"
)

st.title("🎆 Happy New Year 2026!")
st.write("Welcome to the interactive 2026 Celebration!")

# Celebration effects
confetti(emojis=["✨", "🎊", "🥂", "🎆", "⭐"])
st.balloons()

col1, col2 = st.columns([1, 1])

with col1:
    if lottie_fireworks:
        st_lottie(lottie_fireworks, height=400, key="fireworks")
    else:
        st.header("✨ Cheers to 2026! ✨")

with col2:
    st.subheader("Mission Status")
    st.success("## 🎉 THE FUTURE IS HERE: 2026!")
    st.divider()
    # Celebration music
    st.markdown("""
    <audio autoplay loop controls style="width:100%">
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)

st.divider()
st.subheader("🌎 Global Arrival Tracker")

cities = {
    "Dhaka 🇧🇩": "Asia/Dhaka",
    "London 🇬🇧": "Europe/London",
    "New York 🇺🇸": "America/New_York",
    "Tokyo 🇯🇵": "Asia/Tokyo"
}

placeholder = st.empty()

while True:
    with placeholder.container():
        cols = st.columns(len(cities))
        for i, (city, tz_name) in enumerate(cities.items()):
            tz = pytz.timezone(tz_name)
            city_time = datetime.datetime.now(tz)
            status = "✨ Arrived" if city_time.year >= 2026 else "⏳ Pending"
            with cols[i]:
                st.metric(
                    label=city,
                    value=city_time.strftime("%I:%M:%S %p"),
                    delta=""
                )
                st.markdown(
                    f"<p style='color:white; font-weight:bold; font-size:16px; text-align:center'>{status}</p>",
                    unsafe_allow_html=True
                )
    time.sleep(1)
