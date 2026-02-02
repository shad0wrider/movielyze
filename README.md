# Demo

![Demo Gif](https://raw.githubusercontent.com/shad0wrider/movielyze/refs/heads/main/movielyze.gif)

## Images
- ### Ai Page
![AI Page](https://raw.githubusercontent.com/shad0wrider/movielyze/refs/heads/main/assets/ai.png)
- ### Bar Graph
![Bar Graph](https://raw.githubusercontent.com/shad0wrider/movielyze/refs/heads/main/assets/bar.png)
- ### Pie Chart
![Pie Chart](https://raw.githubusercontent.com/shad0wrider/movielyze/refs/heads/main/assets/pie.png)

---
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
---
## How to Run it?
1. ``git clone https://github.com/shad0wrider/movielyze.git``
2. ``cd movielyze``
3. ``python3 -m pip install -r requirements.txt``
4. ``python3 -m streamlit run main.py``