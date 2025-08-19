#on the basis of https://www.geeksforgeeks.org/hadoop-mrjob-python-library-for-mapreduce-with-example/
from mrjob.job import MRJob

def hasonlydigits(word):
    for i in word:
        if i not in "0123456789":
            return False
    return True

def clr(word):
    #Remove links
    if "https:" in word or "http:" in word:
        return ""
    #Remove special characters
    newword = ""
    for char in word:
        if char in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789":
            newword += char
    if hasonlydigits(newword):
        return ""
    newword = newword.lower()
    return newword

class Count(MRJob):
    def mapper(self, _, line): 
        for word in line.split():
            word = clr(word)
            yield(word, 1)        
    def reducer(self, word, counts):
        yield(word, sum(counts)) 
         
if __name__ == '__main__': 
    Count.run()
