import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# ====================== CYBERPUNK UI ======================
cyberpunk_ui = """
<style>
/* Main app background */
.stApp {
    background-color: #000000;
    color: #00eaff;
    font-family: 'Segoe UI', sans-serif;
}

/* Title glow */
h1, h2, h3 {
    color: #00eaff !important;
    text-shadow: 0 0 15px #00eaff;
}

/* Dataframe background */
.dataframe {
    background: #111;
    color: #00eaff;
    border-radius: 8px;
}

/* Sidebar */
.css-1d391kg {
    background: rgba(0, 0, 0, 0.7) !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff00ff, #00eaff);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 20px;
    font-weight: bold;
    box-shadow: 0 0 15px #00eaff;
}

.stButton>button:hover {
    box-shadow: 0 0 25px #ff00ff;
    transform: scale(1.05);
    transition: 0.2s;
}

/* Inputs */
textarea, input {
    background: #111 !important;
    color: #00eaff !important;
    border: 1px solid #00eaff !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #00eaff;
    border-radius: 10px;
}
</style>
"""
st.markdown(cyberpunk_ui, unsafe_allow_html=True)


# ====================== UI ======================
st.title("📊 Advanced Data Visualizer")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📁 Uploaded Dataset Preview")
    st.dataframe(df)

    columns = df.columns.tolist()

    st.subheader("📈 Choose Chart Type")
    chart_type = st.selectbox("Select:", ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart"])

    x_axis = st.selectbox("X-axis:", columns)
    y_axis = None

    if chart_type != "Pie Chart":
        y_axis = st.selectbox("Y-axis:", columns)

    if st.button("Generate Chart"):
        fig = plt.figure(figsize=(6, 4))

        if chart_type == "Line Chart":
            plt.plot(df[x_axis], df[y_axis])

        elif chart_type == "Bar Chart":
            plt.bar(df[x_axis], df[y_axis])

        elif chart_type == "Scatter Plot":
            plt.scatter(df[x_axis], df[y_axis])

        elif chart_type == "Pie Chart":
            counts = df[x_axis].value_counts()
            labels = counts.index
            plt.pie(counts, labels=labels, autopct="%1.1f%%")

        st.pyplot(fig)

else:
    st.info("Please upload a CSV file to begin.")
