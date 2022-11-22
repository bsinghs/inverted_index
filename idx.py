"""Create an inverted index"""

from asyncore import read
import csv
import re
import pdb
import spacy
import pandas as pd

inverted_index = {}
document_map = {}

def get_search_results(search_term):
    result = []
    if search_term in inverted_index:
        for map_index in inverted_index[search_term]:
            result.append(document_map[map_index])
    else:
        result.append("No match found")
    return result

#Get Spacy NLP
nlp = spacy.load("en_core_web_lg")

with open('JEOPARDY_CSV.csv', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    #Skip header row
    next(reader)
    total_lines = len(pd.read_csv('JEOPARDY_CSV.csv')) - 1 
    #for each row in the document
    for i, row in enumerate(reader):
        #print(row)
        #Tokenize each work in the row
        #TODO use spacy for better tokenization (remove punctuations, stop words etc)
        document = " ".join(row[5:]).split()
        document = [word.lower() for word in document]
        #De-duplicate words in the row 
        document = list(set(document))
        document = nlp(" ".join(document))
        #pdb.set_trace
        #add terms to inverted index
        for nlptoken in document:
            if not nlptoken.is_stop and not nlptoken.is_punct and not nlptoken.is_digit:
                token = str(nlptoken)
                if token not in inverted_index:
                    inverted_index[token] = []
                inverted_index[token].append(i)
        #print(inverted_index)
        #if i == 1000:
        #    break
        #print('{} out of {} tokenized'.format(i, total_lines)) 
        document_map[i] = " ".join(row[5:])


#sample query to test
search_query = "king"
search_results = get_search_results(search_query)
print("Search Query: '{}'".format(search_query))
print("Search Results: ")
for i, result in enumerate(search_results):
    print("{} - {}".format(i, result))

