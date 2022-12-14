from xml.dom.minidom import Document, Element
from xml.dom import pulldom

import os
import nltk
import sys

#Sets an expanded recursion limit otherwise errors occur
Newlimit = 5000
sys.setrecursionlimit(Newlimit)


def wordElementTag(document: Document, text: str, pos: str):
    # Creates an element for each word/token.
    word = document.createElement("word")
    word.setAttribute("pos", pos)
    # Creates an attribute for element of each token for Part of Speech (pos)
    # The attribute also sets the identifies part of speech.
    word.setAttribute("lemma", lemmatizer(text, pos))
    # Creates an attribute for the element of each token for lemma.
    # The attribute also identifies the lemmatized word.
    textNode = document.createTextNode(text)
    word.appendChild(textNode)
    return word


def wordnetPos(treebankTag: str):
    posTags = {'J': nltk.corpus.reader.wordnet.ADJ, 'V': nltk.corpus.reader.wordnet.VERB,
               'R': nltk.corpus.reader.wordnet.ADV}
    return posTags.get(treebankTag[0], nltk.corpus.reader.wordnet.NOUN)


def lemmatizer(text: str, pos: str):
    # Returns lemma for each word
    return nltk.stem.WordNetLemmatizer().lemmatize(text.lower(), wordnetPos(pos))


def nltkParse(input_xml):
    # Initialize output as XML document, point to most recent node
    document = Document()
    currentNode = document
    doc = pulldom.parse(input_xml)
    for event, node in doc:
        if event == pulldom.START_ELEMENT:
            currentNode.appendChild(node)
            currentNode = node
        elif event == pulldom.END_ELEMENT:
            currentNode = node.parentNode
        elif event == pulldom.CHARACTERS and currentNode.tagName != 'LINE':
            words = node.toxml()
            text = document.createTextNode(words)
            currentNode.appendChild(text)
        elif event == pulldom.CHARACTERS and currentNode.tagName == 'LINE':
            words = nltk.word_tokenize(node.toxml())
            taggedWords = nltk.pos_tag(words)
            for (text, pos) in taggedWords:
                word = wordElementTag(document, text, pos)
                currentNode.appendChild(word)
    return document


def openXMLFolder(input_folder):
    path = input_folder
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        with open(fullname, 'r') as testing:
            results = nltkParse(testing)
            print(results.toprettyxml())
            #displays the results
            with open(filename.rstrip('.xml') + '_tag' + '.xml', "wb") as f:
                f.write(results.toprettyxml(encoding="utf8"))


openXMLFolder('/Users/brettfujioka/Downloads/shaks200')
limit = sys.getrecursionlimit()

# to find the current recursion limit
limit = sys.getrecursionlimit()


