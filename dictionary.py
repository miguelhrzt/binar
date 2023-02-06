import pandas as pd

# Akses dictionary untuk normalisasi teks
dict_url = "https://raw.githubusercontent.com/miguelhrzt/binar/main/challenge_gold/assets/kamusalay.csv"
dictionary = pd.read_csv(dict_url, encoding='latin-1')
dictionary_map = dict(zip(dictionary['original'], dictionary['replacement']))
