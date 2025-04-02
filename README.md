# 📰 Fake News Detection

## 📌 Project Overview
This project aims to classify news articles as real or fake using machine learning techniques. It processes text data, applies Natural Language Processing (NLP) techniques, and trains a model to detect fake news.

---
## 🚀 Features
- 📝 **Text Preprocessing**: Tokenization, Stopword Removal, Lemmatization.
- 🔍 **Feature Engineering**: TF-IDF Vectorization.
- 🤖 **Machine Learning Models**: Logistic Regression, Naïve Bayes, Random Forest, etc.
- 📊 **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score.
- 🌐 **Web Application**: Deployed using Flask.

---
## 🛠 Installation Guide
### 1️⃣ Clone the repository:
```bash
git clone https://github.com/safiyashaik123/Fake-News-Detector.git
cd Fake-News-Detector
```

### 2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Web App:
```bash
python app.py
```

---
## 📂 Project Structure
```
📁 Fake-News-Detector
│── .idea/                 # Project settings (IDE-specific)
│── templates/             # HTML templates for the Flask web app
│── .gitignore             # Files to ignore in version control
│── README.md              # Project documentation
│── app.py                 # Flask web application
│── fake news project.ipynb  # Jupyter Notebook with code and analysis
│── model.pkl              # Trained machine learning model
│── vectorizer.pkl         # TF-IDF vectorizer
│── requirements.txt       # Dependencies
```

---
## 🏗 How It Works
1. **Data Loading**: Reads dataset containing labeled real and fake news articles.
2. **Text Preprocessing**: Cleans and tokenizes text, removes stopwords.
3. **Feature Extraction**: Converts text into numerical features using TF-IDF.
4. **Model Training**: Trains machine learning models for classification.
5. **Deployment**: The trained model is integrated into a Flask web application.
6. **Web Interface**: Users can enter a news article and check whether it is real or fake.

---
## ✨ Tech Stack
- **Python** (Pandas, NumPy, Scikit-Learn, NLTK, Flask)
- **Machine Learning** (Logistic Regression, Naïve Bayes, Random Forest)
- **Natural Language Processing** (TF-IDF, Text Preprocessing)
- **Flask** (For Web Application Development)

---
## 🎯 Usage
1. Open the browser and go to `http://127.0.0.1:5000/`
2. Enter the news text in the input field.
3. Click on the **Predict** button to see the classification result.

---
## 🤝 Contributing
Pull requests are welcome! If you want to contribute, feel free to fork the repository and submit a PR.

---
## 📜 License
This project is open-source and available under the **MIT License**.

---
## 📧 Contact
If you have any questions or suggestions, feel free to reach out via **GitHub Issues**.

