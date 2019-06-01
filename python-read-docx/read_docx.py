import docx

#Extract text from DOCX
def getDocxContent(filename):
    doc = docx.Document(filename)
    fullText = ""
    for para in doc.paragraphs:
        fullText += para.text
    return fullText
	
resume = getDocxContent("sample.docx")

#Importing NLTK for sentence tokenizing
from nltk.tokenize import sent_tokenize

sentences = sent_tokenize(resume)
for sentence in sentences:
	print(sentence)
	print("\n")