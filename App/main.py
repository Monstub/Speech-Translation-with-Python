import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

translation_active = False

language_translator = Translator()  # Initialize the translation module.
pygame.mixer.init()  # Initialize the mixer module.

# Mapping language names to language codes
lang_code_map = {name: code for code, name in LANGUAGES.items()}

def fetch_language_code(lang_name):
    return lang_code_map.get(lang_name, lang_name)

def translate_text(spoken_text, src_lang, dest_lang):
    return language_translator.translate(spoken_text, src=src_lang, dest=dest_lang)

def synthesize_speech(text, lang):
    speech_obj = gTTS(text=text, lang=lang, slow=False)
    speech_obj.save("audio_cache.mp3")
    audio = pygame.mixer.Sound("audio_cache.mp3")
    audio.play()
    os.remove("audio_cache.mp3")

def translation_process(display_placeholder, src_lang, dest_lang):
    
    global translation_active
    
    while translation_active:
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            display_placeholder.markdown("<div class='listening'>Listening...</div>", unsafe_allow_html=True)
            recognizer.pause_threshold = 1
            audio_data = recognizer.listen(mic, phrase_time_limit=10)
        
        try:
            display_placeholder.markdown("<div class='processing'>Processing...</div>", unsafe_allow_html=True)
            detected_text = recognizer.recognize_google(audio_data, language=src_lang)
            
            display_placeholder.markdown("<div class='translating'>Translating...</div>", unsafe_allow_html=True)
            translated_result = translate_text(detected_text, src_lang, dest_lang)

            synthesize_speech(translated_result.text, dest_lang)
    
        except Exception as error:
            display_placeholder.text(f"Error: {error}")

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .listening, .processing, .translating {
        font-size: 1.5em;
        color: #FF5722;
        text-align: center;
        margin-top: 20px;
        font-family: 'Arial', sans-serif;
    }
    .css-1aumxhk {
        background: #4CAF50 !important;
        border: none !important;
        color: #fff !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        font-size: 1em !important;
        font-family: 'Arial', sans-serif !important;
    }
    .st-bb {
        border: 1px solid #4CAF50 !important;
    }
    .st-bc {
        border: 1px solid #4CAF50 !important;
    }
    </style>
""", unsafe_allow_html=True)

# UI layout
st.markdown("<div class='title'>Language Translator</div>", unsafe_allow_html=True)

# Dropdowns for selecting languages
source_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
target_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# Convert language names to language codes
source_language = fetch_language_code(source_language_name)
target_language = fetch_language_code(target_language_name)

# Buttons to control translation
col1, col2 = st.columns(2)
with col1:
    begin_translation = st.button("Start")
with col2:
    end_translation = st.button("Stop")

# Placeholder for output messages
display_placeholder = st.empty()

# Check if "Start" button is clicked
if begin_translation:
    if not translation_active:
        translation_active = True
        translation_process(display_placeholder, source_language, target_language)

# Check if "Stop" button is clicked
if end_translation:
    translation_active = False
