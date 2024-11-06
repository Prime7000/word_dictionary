import streamlit as st
import math
from nltk.corpus import wordnet

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import wordnet

def extract_meaning(words):
    meanings = []
    for word in words:
        word = str(word).lower()  # Ensure the word is a string and convert to lowercase
        synsets = wordnet.synsets(word)
        if synsets:
            meanings.append(synsets[0].definition())
    return meanings

result = None

st.markdown('''<h1 style='text-align:center;'>Prime Word dictionary</h1>''', unsafe_allow_html=True)

text = st.text_input('Enter a word')
col1,col2,col3 = st.columns(3)

with col1:
    pass
with col2:
    sub = st.button('Submit')
    if sub:
        result = extract_meaning([text])
with col3:
    pass

if result:
    st.write(result[0])

