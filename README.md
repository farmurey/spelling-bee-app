# 🐝 Spelling Bee Practice App

An interactive Streamlit app that helps users practice spelling by uploading a custom word list. Built with text-to-speech and visual progress tracking for a smooth spelling experience.

---
## 💡 Why I Built This

As a parent and a non-native English speaker, I often found it challenging to confidently pronounce certain words while helping my child with spelling. I built this app to give my child a fun, independent way to practice spelling with accurate, AI-generated pronunciation and an interactive interface they can use at their own pace.

## ✨ Features

- 📁 Upload your own word list (CSV format)
- 🔊 Hear each word using text-to-speech (macOS `say` command)
- 👁️ Click to reveal spelling
- ⬅️➡️ Navigate between words with buttons or arrow keys
- 📊 Visual progress indicator
- 📥 Downloadable sample word list

---

## 📂 How to Use

1. Launch the app locally or in the cloud
2. Upload a CSV file with one word per line (first column only is used)
3. Click **Show Spelling** to reveal the word
4. Use **Previous**, **Next**, or keyboard arrow keys to navigate
5. The word is auto-pronounced when shown or navigated

---

## 🛠 Local Installation

#### 1. Clone the Repo

```bash
git clone https://github.com/farmurey/spelling-bee-app.git
cd spelling-bee-app
```
### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```
## 📦 Requirements

Python 3.8+

macOS or Linux (for os.system("say") to work)

Chrome or modern browser for Streamlit app

## 🧠 Future Improvements

Score tracking or timed quiz mode

Word difficulty levels

Support for voice input or spelling validation
