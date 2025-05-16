import streamlit as st
import pandas as pd
import io
from gtts import gTTS
import tempfile
import os
import base64

# Set page configuration - must be the first Streamlit command
st.set_page_config(
    page_title="Spelling Bee Practice",
    page_icon="🐝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize text-to-speech functionality
def pronounce_word(word):
    """Function to pronounce the given word using gTTS and auto-play audio"""
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            # Generate speech
            tts = gTTS(text=word, lang='en', slow=False)
            tts.save(fp.name)
            
            # Read and encode audio as base64
            audio_file = open(fp.name, 'rb')
            audio_bytes = audio_file.read()
            b64 = base64.b64encode(audio_bytes).decode()
            audio_html = f'''<audio autoplay="true" style="display:none;">
                                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3" />
                                Your browser does not support the audio element.
                            </audio>'''
            st.markdown(audio_html, unsafe_allow_html=True)
            
            # Clean up
            audio_file.close()
            os.unlink(fp.name)
    except Exception as e:
        st.error(f"Error pronouncing word: {str(e)}")

def get_sample_csv():
    """Read the sample CSV file"""
    try:
        with open('spellingbee.csv', 'rb') as f:
            return f.read()
    except Exception as e:
        st.error(f"Error reading sample file: {str(e)}")
        return None

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        max-width: 800px;
        margin: 0 auto;
    }
    .stButton button {
        width: 100%;
        margin: 0.5rem 0;
        border-radius: 10px;
        height: 3em;
        font-size: 1.1em;
    }
    .word-container {
        padding: 2rem;
        border: 2px solid #e0e0e0;
        border-radius: 15px;
        margin: 1rem 0;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .upload-container {
        padding: 2rem;
        border: 2px dashed #e0e0e0;
        border-radius: 15px;
        margin: 1rem 0;
        background-color: #f8f9fa;
        text-align: center;
    }
    .word-display {
        font-size: 3rem;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
        color: #2c3e50;
    }
    .progress-container {
        margin: 1rem 0;
        padding: 0.5rem;
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    .stProgress > div > div {
        background-color: #4CAF50;
    }
    .stMarkdown {
        text-align: center;
    }
    @media (max-width: 768px) {
        .main {
            padding: 1rem;
        }
        .word-display {
            font-size: 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Title and instructions
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.title("🐝 Spelling Bee Practice")
st.markdown("""
    <div style="margin-bottom: 2rem;">
        Practice your spelling with our interactive tool! Upload your word list and get started.
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state variables
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'words' not in st.session_state:
    st.session_state.words = None
if 'show_spelling' not in st.session_state:
    st.session_state.show_spelling = False
if 'pronounce_flag' not in st.session_state:
    st.session_state.pronounce_flag = False

def load_words(uploaded_file):
    """Function to load and validate the CSV file"""
    try:
        df = pd.read_csv(uploaded_file)
        if df.empty:
            st.error("Error: The CSV file is empty")
            return None
        # Use the first column regardless of its name
        first_column = df.columns[0]
        return df[first_column].tolist()
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

# File upload section
if st.session_state.words is None:
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown("### 📁 Upload Your Word List")
    st.markdown("Upload a CSV file with one word per line. Only the first column will be used.")
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    sample_csv = get_sample_csv()
    if sample_csv:
        st.download_button(
            label="📥 Download Sample CSV",
            data=sample_csv,
            file_name="spellingbee.csv",
            mime="text/csv"
        )
    st.markdown('</div>', unsafe_allow_html=True)
else:
    uploaded_file = None

if uploaded_file is not None:
    # Load words if not already loaded
    if st.session_state.words is None:
        st.session_state.words = load_words(uploaded_file)

if st.session_state.words:
    # Word display container
    st.markdown('<div class="word-container">', unsafe_allow_html=True)
    # Progress indicator
    st.markdown('<div class="progress-container">', unsafe_allow_html=True)
    progress = (st.session_state.current_index + 1) / len(st.session_state.words)
    st.progress(progress)
    st.markdown(f"Word {st.session_state.current_index + 1} of {len(st.session_state.words)}")
    st.markdown('</div>', unsafe_allow_html=True)
    # Word display
    current_word = st.session_state.words[st.session_state.current_index]
    if st.session_state.show_spelling:
        st.markdown(f'<div class="word-display">{current_word}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="word-display" style="font-size:1.1rem; color:#888; font-weight:400;">Click "Show Spelling" to see the word</div>', unsafe_allow_html=True)
    # Navigation buttons
    col_prev, col_spelling, col_next = st.columns([1, 1, 1])
    with col_prev:
        if st.button("⬅️ Previous", key="prev_btn"):
            if st.session_state.current_index > 0:
                st.session_state.current_index -= 1
                st.session_state.show_spelling = False
                st.session_state.pronounce_flag = True
                st.rerun()
    with col_spelling:
        if st.button("📖 Show Spelling", key="spelling_btn"):
            st.session_state.show_spelling = not st.session_state.show_spelling
            st.rerun()
    with col_next:
        if st.button("➡️ Next", key="next_btn"):
            if st.session_state.current_index < len(st.session_state.words) - 1:
                st.session_state.current_index += 1
                st.session_state.show_spelling = False
                st.session_state.pronounce_flag = True
                st.rerun()
    # Automatically pronounce the word if flag is set
    if st.session_state.pronounce_flag:
        pronounce_word(current_word)
        st.session_state.pronounce_flag = False
    st.markdown('</div>', unsafe_allow_html=True) 