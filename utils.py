import docx2txt
import textract


text = docx2txt.process("test/Adrien CHOROT.docx")
print("TEXT")
print(text)
text2 = textract.process("test/Adrien CHOROT.docx")
print("TEXT 2")
print(text2)
