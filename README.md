## Used Car Price Prediction App

This project is a machine learning web application that predicts the selling price of a used car based on its details. The model is trained using a car dataset and deployed using Streamlit.
K)

### Project Overview

The goal of this project is to predict the selling price of a used car using features such as year, present price, kilometers driven, fuel type, seller type, transmission type, and number of previous owners.

The machine learning model is trained in `main.ipynb`, and the Streamlit app is created separately to allow users to enter car details and get a predicted selling price.

### Features

* Data cleaning and duplicate removal
* Handling categorical features using Label Encoding
* Feature scaling using MinMaxScaler
* Model training using:

  * Linear Regression
  * Lasso Regression
* Model evaluation using:

  * R² Score
  * Mean Absolute Error
  * Root Mean Squared Error
* Streamlit web app for price prediction

### Dataset

The dataset used in this project is `cars_data.csv`.

Input features used for prediction:

* Year
* Present_Price
* Kms_Driven
* Fuel_Type
* Seller_Type
* Transmission
* Owner

Target variable:

* Selling_Price

### Model Training

The dataset is first loaded and cleaned by removing duplicate records. The categorical columns `Fuel_Type`, `Seller_Type`, and `Transmission` are converted into numerical values using `LabelEncoder`.

The data is split into training and testing sets using an 80:20 ratio. Feature values are scaled using `MinMaxScaler`.

Two regression models are trained:

1. Linear Regression
2. Lasso Regression

After comparing the models, the Lasso Regression model is used in the Streamlit app for prediction.

### Saved Model Files

The Streamlit app uses the following saved files:

```text
lasso_model.pkl
scaler.pkl
fuel_encoder.pkl
seller_encoder.pkl
transmission_encoder.pkl
```

These files must be saved after training the model so that the app can load them for prediction.

Example code to save the model and preprocessing objects:

```python
import joblib

joblib.dump(lasso_model, "lasso_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(fuel_encoder, "fuel_encoder.pkl")
joblib.dump(seller_encoder, "seller_encoder.pkl")
joblib.dump(transmission_encoder, "transmission_encoder.pkl")
```

### Streamlit App

The app allows the user to enter the following car details:

* Year
* Present Price
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission Type
* Number of Owners

After clicking the **Predict Selling Price** button, the app displays the predicted selling price in lakhs.

### How to Run the Project

Install the required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn streamlit joblib
```

Run the Streamlit app:

```bash
streamlit run app.py
```

### Project Structure

```text
Used-Car-Price-Prediction/
│
├── cars_data.csv
├── main.ipynb
├── app.py
├── lasso_model.pkl
├── scaler.pkl
├── fuel_encoder.pkl
├── seller_encoder.pkl
├── transmission_encoder.pkl
└── README.md
```

### Output

The app predicts the selling price of a used car based on the entered details and displays the result in lakhs.

Example:

```text
Predicted Selling Price: 4.75 lakhs
```

### Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit

### Conclusion

This project demonstrates how machine learning can be used to predict used car prices. It includes the complete workflow from data preprocessing and model training to deployment using a Streamlit web application.
