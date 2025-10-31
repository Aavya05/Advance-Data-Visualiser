import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Advanced Data Visualizer")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # 🔥 Important Fix
    df.columns = df.columns.astype(str)

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
            plt.pie(counts, labels=counts.index, autopct="%1.1f%%")

        st.pyplot(fig)

else:
    st.info("Please upload a CSV file to begin.")
