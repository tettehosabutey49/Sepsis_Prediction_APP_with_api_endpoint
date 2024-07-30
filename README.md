### Overview
This project is made up of two parts. An API for Sepsis Prediction and a Streamlit Sepsis prediction app that leverages the use of an API endpoint for its predictions. This gives stakeholders the opportunity to select a machine learning models to predict the likelihood of sepsis in patients based on various health metrics. This project provides a docker image which is accessible to stakeholders and non-technical stuff irrespective of type of operating system or platform just by following the steps below. 

### Features
- Model Selection: Users can choose between XGBoost and Linear Regressor models for prediction.
- Input Fields: Interface to input relevant features for prediction.
- Prediction Output: Displays the prediction result (Positive/Negative for sepsis) with an associated probability score.
- Data Features

The model utilizes the following features for prediction:

##### Feature	Description
- PRG	Plasma glucose (mu U/ml)
- PL	Blood Work Result-1 (mu U/ml)
- PR	Blood Pressure (mm Hg)
- SK	Blood Work Result-2 (mm)
- TS	Blood Work Result-3 (mu U/ml)
- M11	Body mass index (weight in kg/(height in m)^2)
- BD2	Blood Work Result-4 (mu U/ml)
- Age	Patient's age (years)
- Insurance	If a patient holds a valid insurance card
- Sepsis	Target: Positive if a patient in ICU will develop sepsis, and Negative otherwise
Getting Started
Prerequisites
- Ensure you have Docker installed on your system. You can download and install Docker from here.

Running the Docker Container
Pull the Docker image in powershell:
- docker pull tettehosabutey49/Sepsis_Machine_Learning_API_with_FASTAPI

Run the Docker container in powershell:

- docker run -p 8501:8501 tettehosabutey49/Sepsis_Machine_Learning_API_with_FASTAPI

Access the Streamlit app:

Open your web browser and go to http://localhost:8501.

Usage
- Input Patient Data: Enter the required health metrics in the provided input fields.
- Select Model: Choose between XGBoost and Linear Regressor for prediction.
- Submit: Click the 'Predict' button to get the prediction result.
- View Results: The app will display whether the patient is likely to develop sepsis along with the probability score.

Model Explanation
- XGBoost
An advanced implementation of gradient boosting designed for speed and performance.
Suitable for complex datasets and provides robust predictions.
- Linear Regressor
A basic linear model that predicts the target variable based on a linear combination of input features.
Simpler and faster but may not capture complex patterns as effectively as XGBoost.
Contributing
Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.

License
- This project is licensed under the MIT License - see the LICENSE file for details.

Contact
- For any questions or inquiries, please contact tettehosabutey49@gmail.com
