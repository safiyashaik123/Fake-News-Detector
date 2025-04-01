# Fake-News-Detector
# Project Description
A machine learning model that classifies news articles as real or fake using Natural Language Processing (NLP) techniques and various classification algorithms.

# Project Overview
This project demonstrates how to build a fake news classifier using Python and machine learning. The notebook shows the complete workflow from data loading and preprocessing to model training and evaluation.

# Dataset
The project uses the WELFake_Dataset.csv which contains:

Text content of news articles

Labels (1 for fake, 0 for real)
## 📋 Requirements

Essential Python packages:
```text
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
nltk>=3.6.0
jupyter>=1.0.0
```

## 📦 Installation

**Step 1:Clone the repository**
```bash
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection

```

**Step 2: Install dependencies**
```bash
pip install -r requirements.txt
```
# Results
Logistic Regression performed best with 94.7% accuracy

Confusion matrix shows good balance between true positives and true negatives
