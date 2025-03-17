# Numerical Programming & Data Analysis

The aim of this tutorial is to expose you to different techniques of analysing & visualising data using: Numpy, Python, and Seaborn & Matplotlib.

**References**:
- [Data Analysis with Pandas](https://www.udemy.com/course/data-analysis-with-pandas/?couponCode=ST11MT170325G1)

# Assignment 1: Synthetic Asset Price Analysis & Database Operations

## Objective

Develop a Python application that generates synthetic asset price data using NumPy, stores the data in a SQLite database, and performs data analysis and visualization using Pandas and Matplotlib/Seaborn. This assignment reinforces numerical programming, CRUD operations, and data visualization techniques.

## Assignment 1

### 1. Generate Synthetic Data Using NumPy
- **Generate Data for 1000 Days:**  
  - **Opening Price:** Generate from a normal distribution centered at 170 with a standard deviation of 10.
  - **Closing Price:** Generate from a normal distribution centered at 175 with a standard deviation of 15.
  - **Activity:** Randomly assign a label (e.g., "Buy" or "Sell") for each day.
- **Hint:** Use functions like `np.random.normal` and `np.random.choice`.

### 2. Store Data in a SQLite Database
- **Database Design:**  
  Create a database (e.g., `asset_prices.db`) with a table named `asset_prices` that has columns for:
  - `day` (INTEGER)
  - `opening_price` (REAL)
  - `closing_price` (REAL)
  - `activity` (TEXT)
- **CRUD Operations:**  
  - **Create:** Insert the generated data.
  - **Read:** Query records (e.g., retrieve all records or filter by activity).
  - **Update:** Allow updates to individual records (e.g., correcting a price).
  - **Delete:** Remove specific records.

### 3. Data Analysis Using Pandas
- **Import Data:**  
  Read the SQLite table into a Pandas DataFrame.
- **Compute Derived Metrics:**  
  - Create a new column for the average price (e.g., average of opening and closing prices).
- **Group Data:**  
  - Calculate the mean price for "Buy" and "Sell" activities using `groupby`.

### 4. Data Visualization
- **Visualize the Data:**  
  - **Line Plot:** Show the trend of opening and closing prices over time.
  - **Histogram:** Plot the distribution of the average closing & opening prices.

## Hints and Resources
- **NumPy Documentation:** [NumPy User Guide](https://numpy.org/doc/stable/user/)
- **SQLite in Python:** [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- **Pandas Documentation:** [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- **Matplotlib Documentation:** [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- **Seaborn Documentation:** [Seaborn Documentation](https://seaborn.pydata.org/)
- Review the "ECO5040S - Financial Software Engineering 5 - Numerical Programming.pdf" for additional context on numerical programming and data operations.

---

# Assignment 2: Data Manipulation and Visualization with Pandas

## Objective

Create a Jupyter notebook (.ipynb) file that performs data manipulation and visualization using Pandas. You an use any dataset, if you are struggling to find some; the (UCL Machine Learning)[https://archive.ics.uci.edu/] Repository is a great place to start!

## Tasks

### 1. Data Import and Cleaning
- **Data Source:**  
  Use a provided CSV file containing financial or market data, or generate a synthetic dataset.
- **Import the Data:**  
  Load the data into a Pandas DataFrame using `pd.read_csv()` (or another relevant function).
- **Clean the Data:**  
  - Handle missing values (e.g., drop or fill them).
  - Convert columns to appropriate data types (e.g., dates to datetime objects).

### 2. Data Transformation and Analysis
- **Data Manipulation:**  
  - Create new columns based on existing data (e.g., calculate daily percentage changes or average prices).
  - Filter the data based on specific conditions (e.g., select records within a certain date range).
- **Aggregation:**  
  - Group the data by a relevant key (e.g., department, asset type) and calculate aggregate statistics such as mean, sum, and count.
  - **Hint:** Use `df.groupby()` for aggregation.

### 3. Data Visualization
- **Create Visualizations:**  
  - **Line Chart:** Plot time series data to observe trends.
  - **Bar Chart:** Compare aggregate values across groups.
  - **Histogram:** Display the distribution of key numerical variables.
  - **Scatter Plot:** Visualize relationships between two numerical variables.
- **Enhance Visuals:**  
  - Add titles, axis labels, legends, and customize styles to improve clarity.
  - Optionally, experiment with both Matplotlib’s and Seaborn’s plotting functions.

### 4. Reporting in a Jupyter Notebook
- **Compile Your Analysis:**  
  - Present your data cleaning, transformation, analysis, and visualizations in a Jupyter Notebook.
  - Include Markdown cells to explain your methodology, findings, and any challenges encountered.


## Hints and Resources
- **Pandas Documentation:** [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- **Matplotlib Documentation:** [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- **Seaborn Documentation:** [Seaborn Documentation](https://seaborn.pydata.org/)
- **Jupyter Notebooks:** [Jupyter Documentation](https://jupyter.org/documentation)
- Refer to the "ECO5040S - Financial Software Engineering 5 - Numerical Programming.pdf" for further insights on numerical programming and data operations.

---