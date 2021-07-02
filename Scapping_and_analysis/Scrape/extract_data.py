import textract
text = textract.process('Resume10001.pdf')
print(text)

# from tika import parser
# import urllib.parse
# raw = parser.from_file('V:/Final_Project/Resume_fin/Resume10001.pdf')
# raw = str(raw)

# safe_text = raw.encode('utf-8', errors = 'ignore')
# print(urllib.parse(safe_text))
# safe_text = str(safe_text).replace("\n",'').replace('\\','')
# print(safe_text)

# import PyPDF2
# # pdf file object
# # you can find find the pdf file with complete code in below
# pdfFileObj = open('Resume10001.pdf', 'rb')
# # pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# # a page object
# pageObj = pdfReader.getPage(1)
# # extracting text from page.
# # this will print the text you can also save that into String
# print(pageObj.extractText())

# pdfFileObj.close()