from transformers import MarianMTModel, MarianTokenizer
import streamlit as st

# Load English to French translation model
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text, source_lang="en", target_lang="fr"):
    # Tokenize input text
    inputs = tokenizer.encode(text, return_tensors="pt", language=source_lang)

    # Translate input text
    translated = model.generate(inputs, language=target_lang)

    # Decode translated text
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text

def main():
    st.title("Translator app")
    source_text = st.text_input("Enter text to translate: ")
    source_lang = st.text_input("Enter source language (e.g., en): ")
    target_lang = st.text_input("Enter target language (e.g., fr): ")
    if st.button("Translate"):
        translated_text = translate(source_text, source_lang, target_lang)
        st.write("Translated text:", translated_text)

if __name__ == "__main__":
    main()
