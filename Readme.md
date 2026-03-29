# ANN Churn Classifier

A machine learning application that predicts customer churn using an Artificial Neural Network (ANN) model. Built with Streamlit for easy web-based predictions.

## 🎯 Overview

This application uses a trained ANN model to predict whether a customer is likely to churn (leave the bank). It provides an interactive web interface where users can input customer information and get real-time churn predictions.

## 📋 Features

- **Customer Churn Prediction**: Predict if a customer will leave based on their profile
- **Interactive Web Interface**: User-friendly Streamlit app
- **Real-time Predictions**: Instant results with churn probability
- **Pre-trained Model**: Uses an optimized ANN trained on customer data
- **Data Preprocessing**: Automatic encoding and scaling of inputs

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Dhrubshaw760/ANN_Churn_Classifier.git
cd ANN_Churn_Classifier
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or using pyproject.toml:
```bash
pip install .
```

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 💻 How to Use

1. **Enter Customer Details**:
   - Credit Score
   - Geography (France, Germany, Spain)
   - Gender (Male, Female)
   - Age (18-92)
   - Account Balance
   - Estimated Salary
   - Tenure (years with bank)
   - Number of Products
   - Credit Card Status
   - Active Member Status

2. **Get Prediction**:
   - The model outputs a **churn probability** (0-1)
   - Probability > 0.5: Customer is **likely to churn**
   - Probability ≤ 0.5: Customer is **unlikely to churn**

## 📊 Model Details

- **Architecture**: Artificial Neural Network (ANN)
- **Framework**: TensorFlow/Keras
- **Model File**: `model.h5`
- **Input Features**: 10 customer attributes
- **Output**: Binary churn prediction (0 = No Churn, 1 = Churn)

## 🔧 Encoders & Preprocessors

The model uses pre-trained encoders for data preprocessing:

- **scaler.pkl**: StandardScaler for feature scaling
- **onehot_encoder_geo.pkl**: OneHotEncoder for Geography feature
- **label_encoder_gender.pkl**: LabelEncoder for Gender feature

## 📦 Project Structure

```
ANN_Churn_Classifier/
├── app.py                          # Streamlit application
├── model.h5                        # Trained ANN model
├── scaler.pkl                      # Feature scaler
├── onehot_encoder_geo.pkl          # Geography encoder
├── label_encoder_gender.pkl        # Gender encoder
├── requirements.txt                # Dependencies
├── pyproject.toml                  # Project configuration
└── README.md                       # This file
```

## 📋 Requirements

```
numpy
pandas
scikit-learn
streamlit
tensorflow-cpu
```

**Python Version**: ≥ 3.10

## 🎓 Model Performance

The model is trained on customer banking data and optimized for predicting churn patterns based on customer demographics and account behavior.

## 📝 Notes

- All input data is automatically preprocessed using the pre-trained encoders
- The model runs on CPU (tensorflow-cpu) for compatibility
- Predictions are probabilistic - use 0.5 as the threshold

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Dhrub** - Machine Learning Enthusiast

## 🔗 Links

- **GitHub**: [ANN_Churn_Classifier](https://github.com/Dhrubshaw760/ANN_Churn_Classifier)

---