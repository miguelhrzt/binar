import re
import sqlite3
from dictionary import dictionary_map
from stopword import stopword_indo
from stopword import word_tokenize

db = sqlite3.connect('challenge.db', check_same_thread=False)
mycursor = db.cursor()


def lowercase(text):
    return text.lower()  # change text to lowercase


def remove_unnecessary_char(text):
    text = re.sub(r'(url|retweet|\\t|\\r|user)', '', text)  # remove misc
    text = re.sub(r'((www\.[^\s]+)|(https?://[^ ]+)|(http?://[^\s]+))', ' ', text)  # remove link
    text = re.sub("@[A-Za-z0-9_]+", "", text)  # remove mention
    text = re.sub("#[A-Za-z0-9_]+", "", text)  # remove hashtags
    text = re.sub(r'([A-Za-z])\1{2,}', r'\1', text)  # remove repeated char
    text = re.sub(r"^rt\s", "", text)  # remove RT
    return text


def remove_non_alpha_numeric(text):
    text = re.sub(r'[^\x00-\x7f]', r'', text)  # remove ASCII
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    text = re.sub('  +', ' ', text)
    text = text.strip()  # remove extra whitespace
    return text


def normalize_text(text):
    for word in dictionary_map:
        return ' '.join([dictionary_map[word] if word in dictionary_map else word for word in text.split(' ')])


def remove_stopword(text):
    return ' '.join([word for word in word_tokenize(text) if word not in stopword_indo])


# Untuk Proses Cleaning Data
def preprocess(text):
    text = lowercase(text)  # 1
    text = remove_unnecessary_char(text)  # 2
    text = remove_non_alpha_numeric(text)  # 3
    text = normalize_text(text)  # 4
    text = remove_stopword(text)
    return text


# Untuk File CSV
def process_csv(input_file):
    # untuk mengambil data dari tweet dari first column
    first_column = input_file.iloc[:, 0]
    print(first_column)

    for tweet in first_column:
        tweet_clean = preprocess(tweet)
        query_tabel = "INSERT INTO tweet (tweet_kotor,tweet_bersih) values (?, ?)"
        val = (tweet, tweet_clean)
        mycursor.execute(query_tabel, val)
        db.commit()
        print(tweet)


# Untuk File Text
def process_text(input_text):
    try:
        output_text = preprocess(input_text)
        return output_text
    except:
        print("Text is unreadable")
