from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import streamlit as st

@st.cache(allow_output_mutation=True, suppress_st_warning=True)


def main():
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
    st.title("Englist to Tamil Translator")
    text = st.text_area("Enter the text to translate")
    if st.button("Translate"):
        model_inputs = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["ta_IN"])
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.success(str(translation).strip('][\''))
if __name__ == "__main__":
    main()
