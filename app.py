import streamlit as st

# ================= CSS THEME ==================
neon_css = """
<style>

/* FULL BLACK BACKGROUND */
.stApp {
    background-color: #000000 !important;
}

/* Remove default padding */
.block-container {
    padding-top: 2rem;
}

/* Neon Title */
.neon-title {
    color: #0affff;
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    text-shadow:
        0 0 5px #0affff,
        0 0 10px #0affff,
        0 0 20px #0affff,
        0 0 40px #0affff;
}

/* Neon subtitle */
.neon-sub {
    color: #ff00e1;
    text-align: center;
    font-size: 22px;
    text-shadow:
        0 0 5px #ff00e1,
        0 0 15px #ff00e1,
        0 0 25px #ff00e1;
}

/* Labels neon */
label, .stTextInput label {
    color: #00ff9d !important;
    font-weight: 600;
    text-shadow:
        0 0 5px #00ff9d,
        0 0 10px #00ff9d;
}

/* Button styling */
.stButton>button {
    background-color: #111111;
    color: #00ffff;
    border: 2px solid #00ffff;
    border-radius: 8px;
    padding: 8px 20px;
    font-weight: bold;
    box-shadow:
        0 0 10px #00ffff,
        inset 0 0 10px #00ffff;
}
.stButton>button:hover {
    cursor: pointer;
    box-shadow:
        0 0 20px #00ffff,
        inset 0 0 20px #00ffff;
}

</style>
"""

# Apply CSS
st.markdown(neon_css, unsafe_allow_html=True)

# ================= UI CONTENT ==================
st.markdown("<h1 class='neon-title'>Mind Guard AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='neon-sub'>Submit feedback below</p>", unsafe_allow_html=True)

feedback = st.text_area("Enter your Feedback")

if st.button("Submit"):
    if feedback.strip() == "":
        st.warning("Please enter something...")
    else:
        st.success("✅ Feedback submitted successfully!")
