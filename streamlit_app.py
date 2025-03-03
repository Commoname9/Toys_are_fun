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
import streamlit as st

# Title
st.title("📦 Adding a New Product Guide")

# Instructions Section
st.markdown("""
## 🛠 How to Add a New Product

Follow these steps to properly add a new product and process it for CrunchTime.

---

### **1️⃣ Update Master Data**
- Open the **Master Data file** and fill in all required fields **except for RCP-####**.
- Ensure the data is correct before proceeding.

---

### **2️⃣ Create the Recipe File (090_RECIPE)**
- Copy the **lines associated with the new item** into a **090_RECIPE file**.
- Save as **`090_itemnamecustom.txt`** and send it to CrunchTime for processing.

---

### **3️⃣ Create the Product File (080_PRODUCT)**
- Copy the **lines associated with the new item** into a **080_PRODUCT file**.
- Save as **`080_itemnamecustom.txt`** and send it to CrunchTime.

---

### **4️⃣ Assign Product to Locations**
- Verify that **Y/N values** in **Store Location Products** are correct.
- This determines **where the item will be available**.

---

### **5️⃣ Update & Download RM File**
- After assigning locations, **download a copy of the RM file**.
- **Delete all rows that are NOT new products** in Excel.
- Save the updated file.

---

### **6️⃣ Create & Process Location Data**
- Generate the **266_Location Product data file** to define **storage locations** for the new item.
- Save as **`266_storagecustom.txt`** and send it to CrunchTime.

---

### **7️⃣ Set Minimum & Maximum PAR Levels**
- Create the **266_Min_Max file** to define **Min/Max PAR levels, VO, and Pricing**.
- Save as **`266_Min_Maxcustom.txt`** and send it to CrunchTime.

---

### **8️⃣ Create NSO Order Min/Max File (If Needed)**
- If the product is for an NSO (New Store Opening), create a **266NSO ORDER MIN MAX file**.
- Save as **`266_Min_Maxcustom.txt`** and send it to CrunchTime.

---

### **9️⃣ Create the Vendor BID File**
- Generate a **200_BID file** to hold vendor product information.
- Save as **`200_custom.txt`** and send it to CrunchTime.

- **Final Step**: **Process the BID file in CrunchTime**  
  - Select **"Accept All"** and **"Contract All"** to finalize the product setup.

---

### ✅ **Your Product is Now Added!**
- Ensure that all **files were processed correctly in CrunchTime**.
- The product is now **available for ordering & inventory tracking**.

💡 *For any issues, check error messages or verify file formatting before re-uploading.*
""")







