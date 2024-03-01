from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import streamlit as st

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def download_model():
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50Tokenizer.from_pretrained(model_name)
    return model, tokenizer
model, tokenizer = download_model()

def main():
    st.title("Englist to Tamil Translator")
    text = st.text_area("Enter the text to translate")
    if st.button("Translate"):
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "en_XX"
        encoded_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.lang_code_to_id["ta_IN"])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.success(str(out).strip('][\''))
if __name__ == "__main__":
    main()
