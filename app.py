from flask import Flask, render_template, request
import re
import string
import pickle

app = Flask(__name__)

# Load model and vectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\\W", " ", text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news = request.form['news']
        processed_news = wordopt(news)
        vectorized_news = vectorizer.transform([processed_news])
        prediction = model.predict(vectorized_news)
        proba = model.predict_proba(vectorized_news)
        confidence = max(proba[0]) * 100
        result = "REAL" if prediction[0] == 0 else "FAKE"
        return render_template('index.html',
                             prediction_text=f'The news is {result} (Confidence: {confidence:.2f}%)',
                             news_text=news)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)