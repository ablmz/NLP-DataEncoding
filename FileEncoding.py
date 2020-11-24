#!/usr/bin/env python
# coding: utf-8

# In[73]:


import encodings
import codecs
import chardet 
import glob


# for one Text, we found the encoding format

# In[74]:


datei = open('Texte/Stress.txt', 'rb')
text_type = chardet.detect(datei.read())
print(text_type)
datei.close()


# https://www.kaggle.com/rtatman/automatically-detecting-character-encodings
# 
# With this code we are trying to write encoding types of all files under the folder Texte

# In[76]:


# for every text file, print the file name & guess of its file encoding
print("Text File".ljust(25), "Encoding")

for filename in glob.glob('Texte/*.txt'):
    with open(filename, 'rb') as rawdata:
        result = chardet.detect(rawdata.read())
    print(filename.ljust(25), result['encoding'])


# Quick test whether the files in UTF8

# In[77]:


def isItUnicode(filename):
    with open(filename, 'rb') as f:
        encodingInfo = chardet.detect(f.read())
        if "UTF" not in encodingInfo['encoding']: 
            print("This isn't Unicode! It's", encodingInfo['encoding'])
        else: 
            print("Yep, it's Unicode.")
 
# test our function, the first one is not unicode, the second one is!
isItUnicode("Texte\Weinen.txt")
isItUnicode("../Grimm.txt")
isItUnicode("Siemens.txt")


# In[85]:


testdata = codecs.open('Texte/testdata.txt','w','utf-8')

datei = open('Texte/testdata.txt', 'rb')
text_type = chardet.detect(datei.read())
print(text_type)
testdata.close()


# https://www.kaggle.com/charusaxena/predicting-character-encoding-using-chardet?select=shisei_UTF-8.txt

# To change the file encoding from ISO-8859-1 to utf-8

# In[91]:


path1 = "Texte/Sprachen.txt"
path2 = "Texte/testdata.txt"

coding1 = "ISO-8859-1"
coding2 = "utf-8"

f= open(path1, 'r', encoding=coding1)
content= f.read()
f.close()
f= open(path2, 'w', encoding=coding2)
f.write(content)
f.close()

print("done")


# In[92]:


def detect_encoding(file):
    with open(file,'rb') as raw_data:
        result = chardet.detect(raw_data.read())
        return(result)
    
detect_encoding('Texte/testdata.txt')

