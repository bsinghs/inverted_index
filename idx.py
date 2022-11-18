"""Create an inverted index"""

from asyncore import read
import csv
import re
import pdb

inverted_index = {}

with open('JEOPARDY_CSV.csv', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    for i, row in enumerate(reader):
        print(row)
        # document = " ".join(row[5:]).split()
        # document = [word.lower() for word in document]
        # document = list(set(document))
        # for term in document:
        #     if term not in inverted_index:
        #         inverted_index[term] = []
        #     inverted_index[term].append(i)
        #     print(inverted_index)
        # pdb.set_trace()
        # windoes getting
        #TODO remove punctiations joined words special characters
        #Separate noun verb
        # Getting error: UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 2875: character maps to <undefined>
