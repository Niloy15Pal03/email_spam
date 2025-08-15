# email_spam
# 🚀 Retro Spam Detector

A retro-themed machine learning web application that classifies SMS/Email messages as spam or legitimate using Natural Language Processing techniques.

## 🎯 Features

- **Real-time Spam Detection**: Instantly classify messages as spam or legitimate
- **Retro UI Design**: Classic terminal-inspired interface with VT323 font
- **Advanced NLP Processing**: Uses NLTK for text preprocessing and TF-IDF vectorization
- **Machine Learning Classification**: Trained model for accurate spam detection
- **Interactive Web Interface**: Built with Streamlit for easy deployment

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS styling
- **Machine Learning**: Scikit-learn (Naive Bayes Classifier)
- **Text Processing**: NLTK (Natural Language Toolkit)
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Preprocessing**: Porter Stemmer for word normalization

## 📋 Prerequisites

```bash
pip install streamlit
pip install nltk
pip install scikit-learn
pip install pickle
```

## 🚀 Installation & Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd retro-spam-detector
```

2. **Install required dependencies**
```bash
pip install -r requirements.txt
```

3. **Download NLTK data**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

4. **Ensure model files are present**
   - `vectorizer.pkl` - TF-IDF vectorizer
   - `model.pkl` - Trained classification model

5. **Run the application**
```bash
streamlit run app.py
```

## 🎮 How to Use

1. Open the application in your web browser
2. Enter your message in the "Message Input Terminal"
3. Click "ANALYZE MESSAGE" button
4. View the classification result:
   - **🚨 SPAM DETECTED** - Message classified as spam
   - **✅ MESSAGE SAFE** - Message classified as legitimate

## 📊 Example Classifications

### SPAM Messages ❌

**Prize/Contest Scams:**
```
congratulations you won 1000 call on this number to get your prize
```
*Result: SPAM DETECTED*

**Financial Compensation:**
```
You could be entitled up to £3,160 in compensation from mis-sold PPI on a credit card or Loan. Please reply PPI for info or STOP to opt out.
```
*Result: SPAM DETECTED*

**Loan Offers:**
```
A [redacted] Loan for £950 is approved for you if you receive this SMS. 1 min verification & cash in 1 hr at www.[redacted].co.uk to opt out reply stop
```
*Result: SPAM DETECTED*

**Insurance/Compensation Claims:**
```
Accident compensation
```
*Result: SPAM DETECTED*

### LEGITIMATE Messages ✅

**Personal Communication:**
```
I am free today, lets go out for a movie. What do you say?
```
*Result: MESSAGE SAFE*

**Casual Conversation:**
```
Did you see the match? It was insane
```
*Result: MESSAGE SAFE*

## 🔬 Model Architecture

### Processing Pipeline

1. **Text Normalization**: Convert to lowercase
2. **Tokenization**: Split text into individual words
3. **Alphanumeric Filtering**: Remove non-alphanumeric characters
4. **Stop Word Removal**: Filter common English stop words
5. **Stemming**: Apply Porter Stemmer algorithm
6. **Vectorization**: Convert to TF-IDF feature vectors
7. **Classification**: Predict using trained model

### Technical Specifications

| Component | Technology |
|-----------|------------|
| Algorithm | Naive Bayes Classifier |
| Vectorization | TF-IDF (Term Frequency-Inverse Document Frequency) |
| Text Processing | NLTK Natural Language Toolkit |
| Stemming | Porter Stemmer Algorithm |
| Framework | Streamlit Web Framework |

## 📁 Project Structure

```
retro-spam-detector/
├── app.py                 # Main Streamlit application
├── model.pkl             # Trained classification model
├── vectorizer.pkl        # TF-IDF vectorizer
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── assets/              # Images and static files
```

## 🎨 UI Features

- **Retro Theme**: Dark background with neon green/cyan colors
- **VT323 Font**: Classic terminal-style typography
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Elements**: Hover effects and smooth transitions
- **Real-time Results**: Instant classification feedback

## 🔧 Customization

### Changing Color Scheme
Modify the CSS variables in the `st.markdown()` style section:
```css
:root {
    --primary-color: #00ff41;
    --secondary-color: #00ccff;
    --accent-color: #ff6b35;
}
```

### Adding New Features
1. Extend the `transform_text()` function for additional preprocessing
2. Modify the model loading section to use different algorithms
3. Add confidence scores or probability distributions

## 📈 Performance

- **Accuracy**: High precision on spam detection
- **Speed**: Real-time processing (< 1 second)
- **Memory**: Lightweight model suitable for web deployment
- **Scalability**: Can handle multiple concurrent users

## 🛡️ Security Considerations

- No user data is stored or transmitted
- All processing happens locally within the session
- Model files should be kept secure and version controlled

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created with ❤️ by [Your Name]

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

---

**⭐ Don't forget to star this repository if you found it helpful!**
