import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Advance Data Visualiser", layout="wide")

st.title("📊 Advance Data Visualiser")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Make sure column names are strings
    df.columns = df.columns.astype(str)

    st.success("✅ File loaded successfully!")

    st.subheader("📌 Dataset Preview")
    st.dataframe(df)

    # Select Columns
    x_axis = st.selectbox("Select X axis column", df.columns)
    y_axis = st.selectbox("Select Y axis column", df.columns)

    # Select chart type
    chart_type = st.selectbox("Select Chart Type", ["Line", "Bar", "Scatter", "Histogram"])

    # Plotting
    if st.button("Generate Graph"):
        if x_axis and y_axis:
            try:
                if chart_type == "Line":
                    fig = px.line(df, x=x_axis, y=y_axis)

                elif chart_type == "Bar":
                    fig = px.bar(df, x=x_axis, y=y_axis)

                elif chart_type == "Scatter":
                    fig = px.scatter(df, x=x_axis, y=y_axis)

                elif chart_type == "Histogram":
                    fig = px.histogram(df, x=x_axis)

                st.subheader("📈 Generated Chart")
                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"❌ Error generating chart:\n{e}")
        else:
            st.warning("⚠️ Please select both X and Y axis columns.")

else:
    st.info("👆 Please upload a CSV file to begin visualization.")
