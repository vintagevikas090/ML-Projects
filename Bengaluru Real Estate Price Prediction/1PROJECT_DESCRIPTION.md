# 🏡 Bengaluru Real Estate Price Prediction

This project is an end-to-end data science application that predicts real estate prices in Bengaluru, India. It features a complete workflow from data cleaning and feature engineering to model training and deployment using a user-friendly web interface built with **Streamlit**. The core of the prediction is a **Linear Regression** model which achieved an **R-squared score of \~83%** on the test data.

---

## 🚀 Project Demo

<img width="1026" height="774" alt="final_web_view" src="https://github.com/user-attachments/assets/c639d0b0-815c-4fe3-9a1d-645b08df4876" />

---

## ✨ Features

* **Real-time Price Prediction:** Get instant price estimates based on property attributes.
* **Interactive UI:** A simple and intuitive web interface for easy user interaction.
* **Comprehensive Feature Set:** Predictions are based on key real estate parameters:

  * Location (from a dropdown of over 240 areas in Bengaluru)
  * BHK (Number of Bedrooms, Hall, Kitchen)
  * Total Square Feet Area
  * Number of Bathrooms
  * Number of Balconies

---

## 🛠️ Tech Stack & Libraries

* **Programming Language:** Python
* **Data Analysis & Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Web Framework:** Streamlit
* **Development Environment:** Jupyter Notebook
* **Data Profiling:** ydata-profiling (for generating the data report)

---

## 📂 File Structure

The project is organized as follows:
* Real Estate Price Prediction Project.ipynb — Jupyter notebook with the full model building process
* Bengaluru Real Estate Price Prediction.py — Streamlit app script for the web UI
* run.py — Helper script to run the Streamlit app
* artifacts/ — Folder for model artifacts

  * Real\_Estate\_Price\_Prediction\_model.pkl — The trained and saved linear regression model
  * columns\_data.json — JSON file with column names for prediction
  * location\_data.json — JSON file with location names for the UI dropdown


---

## ⚙️ How to Run Locally

1. **Create a `requirements.txt` file** in the root of your project and include the following libraries:
   * numpy
   * pandas
   * scikit-learn
   * streamlit
   * ydata-profiling

2. **Clone the repository** to your local machine using Git:
   * Run `git clone https://github.com/your-username/your-repo-name.git`
   * Navigate into the project folder using `cd your-repo-name`

3. **Install the required dependencies** by running:
   * `pip install -r requirements.txt`

4. **Run the Streamlit application**:
   * Option 1 (using the helper script): Run `python run.py`
   * Option 2 (direct Streamlit command): Run `streamlit run "Bengaluru Real Estate Price Prediction.py"`

5. **Open your web browser** and navigate to `http://localhost:8501` to access the application.
---


## 🧠 Model Building Lifecycle
1. **Data Loading & Cleaning**
   * Loaded the `bengaluru_house_prices.csv` dataset.
   * Dropped irrelevant columns like `area_type`, `availability`, and `society`.
   * Handled missing values by dropping rows with NaN in essential columns and filling `balcony` NaNs with the mode.
   * Standardized the `bhk` column from string values (e.g., "2 BHK") to numeric integers.

2. **Feature Engineering**
   * Created the `price_per_sqft` feature, a critical metric in real estate.
   * Cleaned the `area` column by removing rows with non-numeric or range values (e.g., "1133 - 1384").

3. **Outlier Removal**
   * **Domain-based Filtering:** Removed properties with less than 300 sq. ft. per bedroom.
   * **Statistical Outlier Removal:** Removed data points beyond one standard deviation of `price_per_sqft` for each location.
   * **BHK-Price Anomaly Removal:** Removed cases where smaller BHKs were more expensive than larger ones in the same location.
   * **Bathroom Outlier Removal:** Removed properties where bathrooms > bedrooms + 2.

4. **Dimensionality Reduction**
   * Grouped locations with 10 or fewer data points into a single 'other' category.

5. **Model Training & Evaluation**
   * One-Hot Encoded the `location` feature.
   * Split data into training (80%) and testing (20%) sets.
   * Trained a **Linear Regression** model.
   * Achieved an **R-squared score of \~83%**.

6. **Exporting Artifacts**
   * Saved the trained model as a `.pkl` file.
   * Exported column names and locations as `.json` files for use in the Streamlit app.

