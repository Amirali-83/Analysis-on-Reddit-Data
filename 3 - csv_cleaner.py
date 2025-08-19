import csv

def removelinks(word):
    if "http" in word:
        return ""
    return word

def leavechars(word, lchars):
    newword = ""
    for char in word:
        if char in lchars:
            newword += char
    return newword

def clean(word):
    word = removelinks(word)
    word = leavechars(word, "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789 $+-")
    word = word.lower()
    return word

with open("json_text.csv", 'r', newline='', encoding='utf-8') as infile:
    csv_read = csv.reader(infile)
    rows = list(csv_read)
    
with open("csv_clean.csv", 'w', newline='', encoding='utf-8') as outfile:
    csv_write = csv.writer(outfile)

    for row in rows:
        clean_row = [clean(cell) for cell in row]
        csv_write.writerow(clean_row)
