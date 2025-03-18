import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Built-in Data Analyzer")

# Creating a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 70000, 80000, 55000]
}
df = pd.DataFrame(data)

st.write("### Sample Data:")
st.write(df)

st.write("### Summary Statistics:")
st.write(df.describe())

numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
if numerical_cols:
    st.write("### Data Visualization")
    column = st.selectbox("Select a numerical column to plot:", numerical_cols)
    fig, ax = plt.subplots()
    df[column].hist(bins=10, edgecolor='black', ax=ax)
    ax.set_title(f'Histogram of {column}')
    st.pyplot(fig)
else:
    st.write("No numerical columns available for plotting.")