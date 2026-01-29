import streamlit as st


st.markdown("""

## Problem Statement
- ### To build an App to visualize movie data in real-time
---
## Libraries Used

- #### **`streamlit`**  -  **Front-End UI / Webiste**
- #### **`sqlite3`**  -  **File-Based Local Database**
- #### **`pandas`**  -  **Generating DataFrames and Data Manupilation**
- #### **`requests`** - **AI model API requests**
---
## How it Works?
- #### This works by using an external AI API , when the user enters a query , its automatically added to a custom prompt
- #### AI model returns the exact SQL query needed to display the data
- #### Data is finally is formated using `st.dataframe()`

""")