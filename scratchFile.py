
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#Import libraries
import xml.etree.ElementTree as ET
import itertools
import contractions
import nltk
import ssl
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download('popular')
data =[]
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
stopwords_sentence = []
#Hard coded file path set to read with f as the variable
#https://stackoverflow.com/questions/16838509/add-pos-tags-as-attribute-to-xml-element
#https://github.com/dahyeK0420/NLTKprocessing/blob/main/scrapingJSONTweet_XML/scrapeTweetsExportXML.ipynb writing
#http://xml.coverpages.org/bosakShakespeare200.html
tree = ET.parse('/Users/brettfujioka/PycharmProjects/NLTKXML/shaks200/dream.xml')
root = tree.getroot()
print(root.text)
textSample = []
contractedText = []
"""for child in root:
    print(child.tag)"""
for element in root.iter():
    if element.tag == 'LINE':
        stringTest = str(element.text)
        contractionsFix = contractions.fix(stringTest)
        lowerCaseText = contractionsFix.lower()
        #print(lemmatizedText)
        splitText = word_tokenize(lowerCaseText)
        textSample.append([lemmatizer.lemmatize(w) for w in splitText])
        #textSample.append(lemmatizedText)
merged = list(itertools.chain.from_iterable(textSample))
for w in merged:
    if w not in stop_words:
        stopwords_sentence.append(w)
print(stopwords_sentence)
#print(merged)

"""for element in root.iter():
    if element.tag == 'LINE':
        splitText = str(element.text).split()
        textSample.append(splitText)
merged = list(itertools.chain.from_iterable(textSample))
print(merged)"""
#new_list = [re.sub(r'[^a-zA-Z0-9]+', '', specialList) for specialList in merged]
#print(new_list)

"""with open('/Users/brettfujioka/PycharmProjects/NLTKXML/shaks200/dream.xml', 'r') as f:
    data = f.read()
    bs_data = bs(data, features="lxml-xml")
    print(bs_data)"""
"""
To Do:
1. DONE Expansion of contractions
2. DONE Case conversions
3. stemming
4. lemmatisation
5. removal of stop words
"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#Import libraries
import xml.etree.ElementTree as ET
import itertools
import contractions
import nltk
import ssl
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download('popular')
data =[]
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
stopwords_sentence = []
#Hard coded file path set to read with f as the variable
#https://stackoverflow.com/questions/16838509/add-pos-tags-as-attribute-to-xml-element
#http://xml.coverpages.org/bosakShakespeare200.html
tree = ET.parse('/Users/brettfujioka/PycharmProjects/NLTKXML/shaks200/dream.xml')
root = tree.getroot()
print(root.text)
textSample = []
contractedText = []
"""for child in root:
    print(child.tag)"""
for element in root.iter():
    if element.tag == 'LINE':
        stringTest = str(element.text)
        contractionsFix = contractions.fix(stringTest)
        lowerCaseText = contractionsFix.lower()
        #print(lemmatizedText)
        splitText = word_tokenize(lowerCaseText)
        textSample.append([lemmatizer.lemmatize(w) for w in splitText])
        #textSample.append(lemmatizedText)
merged = list(itertools.chain.from_iterable(textSample))
for w in merged:
    if w not in stop_words:
        stopwords_sentence.append(w)
print(stopwords_sentence)
#print(merged)

"""for element in root.iter():
    if element.tag == 'LINE':
        splitText = str(element.text).split()
        textSample.append(splitText)
merged = list(itertools.chain.from_iterable(textSample))
print(merged)"""
#new_list = [re.sub(r'[^a-zA-Z0-9]+', '', specialList) for specialList in merged]
#print(new_list)

"""with open('/Users/brettfujioka/PycharmProjects/NLTKXML/shaks200/dream.xml', 'r') as f:
    data = f.read()
    bs_data = bs(data, features="lxml-xml")
    print(bs_data)"""
"""
To Do:
1. DONE Expansion of contractions
2. DONE Case conversions
3. stemming
4. lemmatisation
5. removal of stop words
"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/