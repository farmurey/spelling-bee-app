# 🐝 Spelling Bee Practice App

An interactive Streamlit app that helps users practice spelling by uploading a custom word list. Built with text-to-speech and visual progress tracking for a smooth spelling experience.

---

## ✨ Features

- 📁 Upload your own word list (CSV format)
- 🔊 Hear each word using text-to-speech (gTTS)
- 👁️ Click to reveal spelling
- ⬅️➡️ Navigate between words with buttons or arrow keys
- 📊 Visual progress indicator
- 📥 Downloadable sample word list

---

## 📂 How to Use

1. Launch the app locally or in the cloud
2. Upload a CSV file with one word per line (first column only is used). A sample spellingbee.csv is provided for downloading.
3. Click **Show Spelling** to reveal the word
4. Use **Previous**, **Next** to navigate
5. The word is auto-pronounced when shown or navigated

---

## 🔧 Tech Stack

- [Streamlit](https://streamlit.io/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- Python + Pandas

---

## 🛠 Local Installation

### 1. Clone the Repo

```bash
git clone https://github.com/farmurey/spelling-bee-app.git
cd spelling-bee-app

**2. Install Requirements**
pip install -r requirements.txt

**3. Run the App**
streamlit run app.py


