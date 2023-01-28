import pandas as pd
import re
from flask import Flask, request

app = Flask(__name__)

@app.route('/clean_text', methods=['POST'])

def clean_text(text):
    text = request.form['text']
    text = lowercase(text)
    text = remove_irrelevant_char(text)
    text = remove_non_alpha_numeric(text)
    return text

##untuk merubah semua karakter menjadi huruf kecil secara merata
def lowercase(text):
    return text.lower()

#untuk membersihkan teks dari karakter-karakter yang tidak relevant
def remove_irrelevant_char(text):
    text = re.sub('\n', ' ', text)
    text = re.sub('rt', ' ', text)
    text = re.sub('user',' ', text)
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', ' ', text)
    text = re.sub('  +', ' ', text)
    return text

#untuk membersihkan teks dari karakter-karakter non-alpha numeric
def remove_non_alpha_numeric(text):
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    return text

