# 📈 Zomato Stock Price Prediction using Stacked LSTM
## Overview
This project aims to predict Zomato's stock prices using a Stacked LSTM (Long Short-Term Memory) model. LSTM networks are powerful for sequential data prediction, making them a great choice for stock price forecasting. By using Keras for building the model and essential libraries like Pandas, NumPy, and Matplotlib, we preprocess the data, train the model, and visualize the predictions.

## 🛠 Key Features
- Time-Series Forecasting: Predicting Zomato stock prices based on historical data.
- Stacked LSTM Model: Utilizing multiple LSTM layers to capture temporal dependencies in stock price data.
- Evaluation: Model performance measured using Mean Squared Error (MSE).
- Visualization: Matplotlib is used to visualize the predicted vs actual stock prices for better understanding.

## 📊 Data
The dataset contains historical stock prices for Zomato, including:

- Open
- Close
- High
- Low
- Volume
**Data has been preprocessed to:**

- Normalize the stock prices to improve model accuracy.
- Reshape the data to a format compatible with the LSTM model.

## 🧠 Technologies Used
- Keras for building and training the Stacked LSTM model.
- Pandas for data manipulation and analysis.
- NumPy for numerical computations.
- Matplotlib for visualizing stock price trends and predictions.
- Mean Squared Error (MSE) for performance evaluation.
  
## ✨ Future Improvements
- Include more features: Incorporate additional features like technical indicators (e.g., moving averages) to improve model accuracy.
- Optimize model: Experiment with different LSTM architectures and hyperparameters.
- Deploy the model: Create a web app or API for real-time stock price prediction.

