import re
import textract

email_re = r"[\w\.-]+@[\w\.-]+\.\w+"

docs = [
    'test/Adrien CHOROT.docx',
    'test/Aikaterini Vafeiadi.pdf',
    'test/Akram Sherif.doc',
    'test/Babacar-Ndiaye.pdf',
    'test/CHAND FINAL RESUME (11).docx',
    'test/Cisem-Demirci.pdf',
    'test/CV (1).pdf',
    'test/CV English ( Cover Letter         included).pdf',
    'test/CV English Edcel Uylenbroeck.docx',
    'test/CV_by_Helen_Mäeots.docx',
    'test/CV_EN.pdf',
    'test/cv_Resume.docx',
    'test/cvantoniolima_(1).pdf',
    'test/ElenaA.pdf',
    'test/Ihab El Mortada-resume new.doc',
    'test/Ivonne Blanco.rtf',
    'test/Jaap Gerretse.pdf',
    'test/Jose Daniel Andino Pereira.docx',
    'test/Piotr Lemanski.docx',
    'test/primary%3ADownload%2FEngin Kılıç.pdf',
    'test/Stefanie Haanfler.pdf',
    'test/vasileios  sakkas.docx'
]

for doc in docs:
    text = textract.process(doc).decode('utf-8')
    matches = re.findall(email_re, text, re.MULTILINE)
    if matches:
        print(matches[0])
    else:
        print("no email detected")
