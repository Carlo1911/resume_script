import re
import textract
import json

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

phone_regex_plus = r"\+[0-9]{1,}"
phone_regex = r"[0-9]{5,}"
phone_regex_parenthesis = r"\([0-9]+\)"


def get_email(text):
    matches = re.findall(email_re, text, re.MULTILINE)
    if matches:
        return matches[0]
    else:
        return("no email detected")


def get_phone(text):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    matches = re.findall(phone_regex_plus, text, re.MULTILINE)
    if matches:
        if len(matches[0]) > 9:
            return matches[0]
        else:
            matches_sec = re.finditer(phone_regex_plus, text, re.MULTILINE)
            rest_number = ''
            if matches_sec:
                match = [m.end(0) for m in matches_sec]
                index = match[0]
                while(1):
                    if text[index] != ' ' and text[index] in numbers:
                        rest_number += text[index]
                        index += 1
                    elif text[index] == ' ' or text[index] == '(' or text[index] == ')' or text[index] == '.' or text[index] == '-':
                        index += 1
                    else:
                        break
                return(matches[0]+rest_number)
    else:
        matches = re.findall(phone_regex_parenthesis, text, re.MULTILINE)
        if matches:
            matches_sec = re.finditer(
                phone_regex_parenthesis, text, re.MULTILINE)
            rest_number = ''
            if matches_sec:
                match = [m.end(0) for m in matches_sec]
                index = match[0]
                while(1):
                    if text[index] != ' ' and text[index] in numbers:
                        rest_number += text[index]
                        index += 1
                    elif text[index] == ' ' or text[index] == '(' or text[index] == ')' or text[index] == '.' or text[index] == '-':
                        index += 1
                    else:
                        break
                return(matches[0].strip('\(\)')+rest_number)
        else:
            matches = re.findall(phone_regex, text, re.MULTILINE)
            if matches:
                if len(matches[0]) > 9:
                    return matches[0]
                else:
                    matches_sec = re.finditer(phone_regex, text, re.MULTILINE)
                    rest_number = ''
                    if matches_sec:
                        match = [m.end(0) for m in matches_sec]
                        index = match[0]
                        while(1):
                            if text[index] != ' ' and text[index] in numbers:
                                rest_number += text[index]
                                index += 1
                            elif text[index] == ' ' or text[index] == '(' or text[index] == ')' or text[index] == '.' or text[index] == '-':
                                index += 1
                            else:
                                break
                        if len(matches[0]+rest_number) > 5:
                            return(matches[0]+rest_number)
                        else:
                            return(matches[1])
            else:
                return("no phone detected")


data = {}
cvs = []
for doc in docs:
    cv = {}
    text = textract.process(doc).decode('utf-8')
    cv['file'] = doc
    print(doc)
    cv['email'] = get_email(text)
    print (cv['email'])
    cv['phone'] = get_phone(text)
    print (cv['phone'])
    print("==============")
    cvs.append(cv)
data['data'] = cvs
with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
