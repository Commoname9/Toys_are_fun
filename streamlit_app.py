import streamlit as st  # Import Streamlit

# Title & Subheader
st.title("Welcome to Matt's App!")
st.subheader("This is a simple UI demo.")

# Paragraph Text
st.write("This will help get us started with the Redemption Master program to move it to a more futuristic version that will work faster and smarter.")

# Adding Markdown-style Text
st.markdown("### This is Markdown Text 🔥")
st.markdown("*You can use **bold**, _italic_, or `code` formatting!*")
# Button Example
if st.button("Click Me!"):
    st.success("Thank you for clicking! 🎉")
    
import pandas as pd  # Import Pandas

# Upload Excel File
uploaded_file = st.file_uploader("Upload an Excel File", type=["xlsx"])

if uploaded_file:
    # Read Excel File
    df = pd.read_excel(uploaded_file)

    # Show the DataFrame as a table
    st.write("### Data Preview:")
    st.dataframe(df)  # This displays an interactive table!

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Dropdown for selecting a column value
    column_name = "Location Code"  # Change this to match your actual column
    if column_name in df.columns:
        options = df[column_name].unique()
        selected_option = st.selectbox(f"Select a {column_name}:", options)

        # Show filtered data
        filtered_df = df[df[column_name] == selected_option]
        st.write("### Filtered Data:")
        st.dataframe(filtered_df)
        
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Filter data before exporting
    if "Product Active Flag" in df.columns:
        filtered_data = df[df["Product Active Flag"] == "Y"]

        # Button to export as a tab-delimited file
        if st.button("Export as Tab-Delimited File"):
            filtered_data.to_csv("output.txt", sep="\t", index=False)
            st.success("File exported successfully!")






