import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

is_translation_enabled = False

translator = Translator()  # Initialize the translation module.
pygame.mixer.init()  # Initialize the audio mixer.

# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def retrieve_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translate_spoken_text(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src=from_language, dest=to_language)

def text_to_audio(text_data, to_language):
    audio_tts = gTTS(text=text_data, lang=to_language, slow=False)
    audio_tts.save("cache_file.mp3")
    audio = pygame.mixer.Sound("cache_file.mp3")  # Load the audio.
    audio.play()
    os.remove("cache_file.mp3")

def process_audio_input(output_placeholder, from_language, to_language):
    global is_translation_enabled
    
    while is_translation_enabled:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            output_placeholder.text("Listening...")
            recognizer.pause_threshold = 1
            audio_input = recognizer.listen(source, phrase_time_limit=10)
        
        try:
            output_placeholder.text("Processing...")
            spoken_text = recognizer.recognize_google(audio_input, language=from_language)
            
            output_placeholder.text("Translating...")
            translated_text = translate_spoken_text(spoken_text, from_language, to_language)

            text_to_audio(translated_text.text, to_language)
    
        except Exception as e:
            print(e)

# UI layout
st.title("Language Translator")

# Dropdowns for selecting languages
from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = retrieve_language_code(from_language_name)
to_language = retrieve_language_code(to_language_name)

# Button to initiate translation
start_button = st.button("Start")
stop_button = st.button("Stop")

# Check if "Start" button is clicked
if start_button:
    if not is_translation_enabled:
        is_translation_enabled = True
        output_placeholder = st.empty()
        process_audio_input(output_placeholder, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    is_translation_enabled = False
