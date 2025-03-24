import re
import time
import pandas as pd
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import *

start_time = time.time()
double_quotes= re.compile(r"[«‹»›„“‟”❝❞❮❯〝〞〟＂]")
single_quotes= re.compile(r"[‘‛’❛❜`´]")
url_re = re.compile(r"http[^\s]*")
email_re = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
date_re = re.compile(r"([\w]+[ \.]+[\d]{,2}, [\d]{4})|(\d{4}-\d{2}-\d{2})")
time_re = re.compile(r"[\d]{2}:[\d]{2}:[\d]{2}(.[\d]+)?")
num_re = re.compile(r"\d+")

punctuation_marks = str.maketrans({p: " " for p in ".,:'\"[]()"})

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess(text):
    if not isinstance(text, str):  
        return ""
    
    #fix quotation marks
    text = double_quotes.sub('"', text)
    text = single_quotes.sub("'", text)
    
    #remove numbers, URLS, emails and dates
    text = url_re.sub('URL', text)
    text = email_re.sub('EMAIL', text)
    text = date_re.sub('DATE',text)
    text = time_re.sub('TIME',text)
    text = num_re.sub('NUM',text)

    #Replace punctuation with whitespaces
    text = text.translate(punctuation_marks)

    #Normalize whitespaces
    text = re.sub(r"\s+", " ", text).strip()

    text = wordpunct_tokenize(text.lower())

    text = [stemmer.stem(word) for word in text if word not in stop_words] 
        #stemming and stop-word removal at the same time
    
    return text

input_file = r'Group Project\995K.csv'
output_file = 'articles_preprocessed_1mio.csv'
num_rows = 1000

chunk_size = 100000
chunk_num = 1
first_chunk = True

print(f"Initialization = {time.time() - start_time:.2f} seconds") #Debug

for df in pd.read_csv(input_file,chunksize=chunk_size, usecols=['content', 'type']):
    df.dropna(subset=['content'], inplace=True) #Droppar rows með missing values
    df = df[df['content'].apply(lambda x: isinstance(x, str))] #Only use rows with string values

    #map 'type' to new labels, 1 = 'realiable' 0 = 'unreliable'
    label_mapping = {'reliable': 1, 'clickbait': 1, 'political': 1, 'unreliable': 0, 'hate': 0, 'conspiracy': 0}
    df['LABEL'] = df['type'].map(label_mapping)

    df.dropna(subset=['LABEL'], inplace=True) #drop rows not labeled above

    print(f"Chunk {chunk_num}: Restructuring = {time.time() - start_time:.2f} seconds") #Debug

    #apply preprocessing steps
    df['content'] = df['content'].apply(preprocess)

    print(f"Chunk {chunk_num}: Preprocessing = {time.time() - start_time:.2f} seconds") #Debug

    #output to csv file
    df[['content', 'LABEL']].to_csv(output_file, mode='w' if first_chunk else 'a', index=False, header=first_chunk)
    first_chunk = False
    print(f"Chunk {chunk_num}: Printing = {time.time() - start_time:.2f} seconds") #Debug
    chunk_num +=1