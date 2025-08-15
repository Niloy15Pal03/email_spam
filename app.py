import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# Balanced retro styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23, #1a1a2e);
        color: #00ff41;
        font-family: 'VT323', monospace;
    }
    
    .main-header {
        background: #16213e;
        border: 2px solid #00ff41;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem 0 2rem 0;
        box-shadow: 0 0 15px rgba(0,255,65,0.3);
    }
    
    .title {
        font-size: 2.5rem;
        color: #00ff41;
        text-shadow: 0 0 10px #00ff41;
        margin: 0;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #00ccff;
        margin-top: 0.5rem;
    }
    
    .input-section {
        background: rgba(22,33,62,0.8);
        border: 1px solid #00ccff;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .stTextArea textarea {
        background-color: #0a0a0a !important;
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        border-radius: 5px !important;
        font-family: 'VT323', monospace !important;
        font-size: 1.1rem !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #00ccff !important;
        box-shadow: 0 0 10px rgba(0,204,255,0.5) !important;
    }
    
    .stButton button {
        background: linear-gradient(45deg, #ff6b35, #f7931e) !important;
        color: #000 !important;
        border: 2px solid #ff6b35 !important;
        border-radius: 5px !important;
        font-family: 'VT323', monospace !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        padding: 0.5rem 2rem !important;
        box-shadow: 0 0 10px rgba(255,107,53,0.4) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton button:hover {
        background: linear-gradient(45deg, #f7931e, #ff6b35) !important;
        box-shadow: 0 0 20px rgba(255,107,53,0.6) !important;
    }
    
    .result-spam {
        background: rgba(255,0,0,0.1);
        border: 2px solid #ff0040;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        color: #ff0040;
        font-size: 2rem;
        font-weight: bold;
        text-shadow: 0 0 5px #ff0040;
        margin: 1rem 0;
    }
    
    .result-safe {
        background: rgba(0,255,65,0.1);
        border: 2px solid #00ff41;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        color: #00ff41;
        font-size: 2rem;
        font-weight: bold;
        text-shadow: 0 0 5px #00ff41;
        margin: 1rem 0;
    }
    
    .model-section {
        background: rgba(26,26,46,0.9);
        border: 1px solid #888;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 2rem 0;
    }
    
    .section-title {
        color: #00ccff;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        text-shadow: 0 0 5px #00ccff;
    }
    
    .info-box {
        background: rgba(0,0,0,0.4);
        border: 1px solid #555;
        border-radius: 5px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .info-label {
        color: #00ccff;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .info-value {
        color: #00ff41;
        font-size: 1rem;
    }
    
    .process-steps {
        background: rgba(0,0,0,0.3);
        border-left: 3px solid #00ff41;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .step {
        color: #ccc;
        margin: 0.5rem 0;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)
import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

# Header
st.markdown("""
<div class="main-header">
    <div class="title">RETRO SPAM DETECTOR</div>
    <div class="subtitle">Neural Network Message Analysis System</div>
</div>
""", unsafe_allow_html=True)

# Input Section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #00ccff; margin-bottom: 1rem;">Message Input Terminal</h3>', unsafe_allow_html=True)

input_sms = st.text_area("Enter your message for analysis:", height=120)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    predict_btn = st.button('ANALYZE MESSAGE')

st.markdown('</div>', unsafe_allow_html=True)

# Results
if predict_btn and input_sms:
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    
    if result == 1:
        st.markdown('<div class="result-spam">⚠️ SPAM DETECTED ⚠️</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-safe">✅ MESSAGE SAFE ✅</div>', unsafe_allow_html=True)

# Model Information Section
st.markdown('<div class="model-section">', unsafe_allow_html=True)
st.markdown('<h3 class="section-title">🔬 System Specifications</h3>', unsafe_allow_html=True)

# Create two columns for specifications
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-box">
        <div class="info-label">Algorithm Type:</div>
        <div class="info-value">Machine Learning Classifier</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-label">Text Processing:</div>
        <div class="info-value">NLTK Natural Language Toolkit</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <div class="info-label">Text Vectorization:</div>
        <div class="info-value">TF-IDF (Term Frequency-Inverse Document Frequency)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-label">Stemming Algorithm:</div>
        <div class="info-value">Porter Stemmer</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h4 style="color: #00ccff; margin: 1.5rem 0 1rem 0;">Processing Pipeline:</h4>', unsafe_allow_html=True)

st.markdown("""
<div class="process-steps">
    <div class="step">1. Text normalization and tokenization</div>
    <div class="step">2. Remove punctuation and non-alphanumeric characters</div>
    <div class="step">3. Filter stop words and common terms</div>
    <div class="step">4. Apply Porter stemming algorithm</div>
    <div class="step">5. Convert to TF-IDF feature vectors</div>
    <div class="step">6. Classify using trained model</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
