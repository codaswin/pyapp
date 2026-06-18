import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #111827
    );
}

/* Hide Streamlit Branding */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Title */
.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    background: linear-gradient(
        90deg,
        #4285F4,
        #8E44FF,
        #FF4FD8,
        #00D4FF
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Result Card */
.result-card {
    background: linear-gradient(
        135deg,
        #4285F4,
        #8E44FF,
        #FF4FD8
    );
    border-radius: 25px;
    padding: 30px;
    text-align: center;
    color: white;
    margin-top: 25px;
    box-shadow: 0px 12px 35px rgba(142,68,255,0.5);
}

/* Grade Text */
.grade {
    font-size: 90px;
    font-weight: bold;
}

/* Slider Styling */
.stSlider {
    padding-top: 20px;
    padding-bottom: 20px;
}

/* Gemini Style Button */
.stButton > button {
    width: 100%;
    height: 60px;
    border: none;
    border-radius: 15px;

    background: linear-gradient(
        270deg,
        #4285F4,
        #8E44FF,
        #FF4FD8,
        #00D4FF
    );

    background-size: 600% 600%;
    animation: gradientMove 6s ease infinite;

    color: white;
    font-size: 20px;
    font-weight: bold;

    box-shadow: 0px 8px 25px rgba(142,68,255,0.5);

    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0px 12px 35px rgba(255,79,216,0.7);
}

.stButton > button:active {
    transform: scale(0.98);
}

@keyframes gradientMove {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    "<h1 class='title'>🎓 Student Grade Calculator</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Transform Marks into Beautiful Grades</p>",
    unsafe_allow_html=True
)

# -------------------------
# MARKS INPUT (SLIDER)
# -------------------------
marks = st.slider(
    "📚 Select Student Marks",
    0,
    100,
    85
)

# -------------------------
# BUTTON
# -------------------------
calculate = st.button("✨ Generate Grade")

# -------------------------
# GRADE LOGIC
# -------------------------
if calculate:

    if marks >= 90:
        grade = "A"
        emoji = "🏆"
        message = "Outstanding Performance!"
    elif marks >= 80:
        grade = "B"
        emoji = "🚀"
        message = "Excellent Work!"
    elif marks >= 70:
        grade = "C"
        emoji = "👍"
        message = "Good Job!"
    elif marks >= 60:
        grade = "D"
        emoji = "📚"
        message = "Needs Improvement!"
    else:
        grade = "E"
        emoji = "⚠️"
        message = "Keep Practicing!"

    st.markdown(
        f"""
        <div class="result-card">
            <h2>{emoji}</h2>
            <h3>Marks: {marks}</h3>
            <div class="grade">{grade}</div>
            <h3>{message}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Balloons for Grade A
    if grade == "A":
        st.balloons()

# -------------------------
# GRADE TABLE
# -------------------------
st.markdown("---")

st.subheader("📊 Grading Scale")

st.table({
    "Marks Range": [
        "90 - 100",
        "80 - 89",
        "70 - 79",
        "60 - 69",
        "Below 60"
    ],
    "Grade": [
        "A",
        "B",
        "C",
        "D",
        "E"
    ]
})

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")