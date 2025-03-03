import streamlit as st  # Import Streamlit

# Title & Subheader
st.title("Welcome to Matt's App!")
st.subheader("This is a simple UI demo.")

# Paragraph Text
st.write("This will help get us started with the Redemption Master program to move it to a more futuristic version that will work faster and smarter.")


import streamlit as st

# Title
st.title("📊 Product & PAR Management Tool")

# How to Use Section
st.markdown("""
## 🛠 How to Use This Tool

### **1️⃣ Upload Your Product Data**
- Click on the **"Upload Excel File"** button.
- Select your **Google Sheets file** (or sync directly from the cloud).
- The data will be displayed in an interactive table.

### **2️⃣ View & Manage Products**
- Use the dropdowns to **filter products** by location.
- Check **Min/Max PAR levels** and product details.

### **3️⃣ Edit & Save Data**
- Update PAR levels or product categories inside the tool.
- Click the **"Save Changes"** button to push updates to Google Sheets.

### **4️⃣ Export Data for CrunchTime**
- Click **"Export Tab-Delimited File"** to download the validated file.
- This file can be **directly uploaded into CrunchTime**.

### **🔹 Additional Features**
- Live updates from Google Sheets.
- Prevents **duplicate entries** and **missing values**.
- Ensures CrunchTime **file format compliance**.

💡 *For any issues, check error messages below or refresh the page.*
""")

# Adding Markdown-style Text
st.markdown("### This is Markdown Text 🔥")
st.markdown("*You can use **bold**, _italic_, or `code` formatting!*")
# Button Example
if st.button("Click Me!"):
    st.success("Thank you for clicking!")
    

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







