**# 🏡 Bengaluru Real Estate Price Prediction**



**This project is an end-to-end data science application that predicts real estate prices in Bengaluru, India. It features a complete workflow from data cleaning and feature engineering to model training and deployment using a user-friendly web interface built with \*\*Streamlit\*\*. The core of the prediction is a \*\*Linear Regression\*\* model which achieved an \*\*R-squared score of \\~83%\*\* on the test data.**



**-----**



**## 🚀 Project Demo**





**-----**



**## ✨ Features**



  **\* \*\*Real-time Price Prediction:\*\* Get instant price estimates based on property attributes.**

  **\* \*\*Interactive UI:\*\* A simple and intuitive web interface for easy user interaction.**

  **\* \*\*Comprehensive Feature Set:\*\* Predictions are based on key real estate parameters:**

      **\* Location (from a dropdown of over 240 areas in Bengaluru)**

      **\* BHK (Number of Bedrooms, Hall, Kitchen)**

      **\* Total Square Feet Area**

      **\* Number of Bathrooms**

      **\* Number of Balconies**



**-----**



**## 🛠️ Tech Stack \& Libraries**



  **\* \*\*Programming Language:\*\* Python**

  **\* \*\*Data Analysis \& Manipulation:\*\* Pandas, NumPy**

  **\* \*\*Machine Learning:\*\* Scikit-learn**

  **\* \*\*Web Framework:\*\* Streamlit**

  **\* \*\*Development Environment:\*\* Jupyter Notebook**

  **\* \*\*Data Profiling:\*\* ydata-profiling (for generating the data report)**



**-----**



**## 📂 File Structure**



**The project is organized as follows:**



**```**

**.**

**├── Real Estate Price Prediction Project.ipynb   # Jupyter notebook with the full model building process**

**├── Bengaluru Real Estate Price Prediction.py    # Streamlit app script for the web UI**

**├── run.py                                       # Helper script to run the Streamlit app**

**|**

**├── artifacts/                                   # Folder for model artifacts**

**│   ├── Real\_Estate\_Price\_Prediction\_model.pkl   # The trained and saved linear regression model**

**│   ├── columns\_data.json                        # JSON file with column names for prediction**

**│   └── location\_data.json                       # JSON file with location names for the UI dropdown**

**```**



**\*(\*\*Note:\*\* It is recommended to create an `artifacts` folder and move your `.pkl` and `.json` files into it for better organization.)\***



**-----**



**## ⚙️ How to Run Locally**



**Follow these steps to set up and run the project on your local machine.**



**\*\*1. Create `requirements.txt`:\*\***



**Before proceeding, create a `requirements.txt` file in the root of your project with the following content:**



**```**

**numpy**

**pandas**

**scikit-learn**

**streamlit**

**ydata-profiling**

**```**



**\*\*2. Clone the repository:\*\***



**```bash**

**git clone https://github.com/your-username/your-repo-name.git**

**cd your-repo-name**

**```**



**\*\*3. Install the required dependencies:\*\***



**```bash**

**pip install -r requirements.txt**

**```**



**\*\*4. Run the Streamlit application:\*\***

**You can run the application using either the helper script or the direct Streamlit command.**



**\*Using the helper script:\***



**```bash**

**python run.py**

**```**



**\*Or using the direct command:\***



**```bash**

**streamlit run "Bengaluru Real Estate Price Prediction.py"**

**```**



**Now, open your web browser and navigate to `http://localhost:8501`.**



**-----**



**## 🧠 Model Building Lifecycle**



**The machine learning model was built following a systematic approach as detailed in the Jupyter Notebook:**



**1.  \*\*Data Loading \& Cleaning:\*\***



      **\* Loaded the `bengaluru\_house\_prices.csv` dataset.**

      **\* Dropped irrelevant columns like `area\_type`, `availability`, and `society`.**

      **\* Handled missing values by dropping rows with `NaN` in essential columns and filling `balcony` `NaN`s with the mode.**

      **\* Standardized the `bhk` column from string values (e.g., "2 BHK") to numeric integers.**



**2.  \*\*Feature Engineering:\*\***



      **\* Created the `price\_per\_sqft` feature, which is a critical metric in real estate and essential for outlier detection.**

      **\* Cleaned the `area` column by removing rows with non-numeric or range values (e.g., "1133 - 1384").**



**3.  \*\*Outlier Removal:\*\***



      **\* A multi-step outlier removal process was implemented to ensure data quality:**

          **\* \*\*Domain-based Filtering:\*\* Removed properties with less than 300 sq. ft. per bedroom.**

          **\* \*\*Statistical Outlier Removal:\*\* For each location, calculated the mean and standard deviation of `price\_per\_sqft` and removed data points beyond one standard deviation. This preserves price variations between locations.**

          **\* \*\*BHK-Price Anomaly Removal:\*\* Removed instances where, for the same location, a property with a smaller BHK count was more expensive than one with a higher BHK count.**

          **\* \*\*Bathroom Outlier Removal:\*\* Removed properties where the number of bathrooms was greater than the number of bedrooms + 2.**



**4.  \*\*Dimensionality Reduction:\*\***



      **\* The `location` column had over 1200 unique values. To reduce dimensionality, locations with 10 or fewer data points were grouped into a single 'other' category.**



**5.  \*\*Model Training \& Evaluation:\*\***



      **\* The categorical `location` feature was converted into numerical data using \*\*One-Hot Encoding\*\*.**

      **\* The data was split into training (80%) and testing (20%) sets.**

      **\* A \*\*Linear Regression\*\* model from Scikit-learn was trained on the data.**

      **\* The model achieved an \*\*R-squared score of approximately 83%\*\*, indicating a good fit for the data.**



**6.  \*\*Exporting Artifacts:\*\***



      **\* The trained model was saved as a `.pkl` file.**

      **\* The list of encoded column names and locations were exported as `.json` files to be used by the Streamlit application for prediction.**



**-----**



