import json
# import re
import regex as re
import spacy
import textract
from nltk.corpus import words


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
    'test/Stefanie Haanfler.pdf',
    'test/vasileios  sakkas.docx'
]

email_re = r"[\w\.-]+@[\w\.-]+\.\w+"
phone_regex_plus = r"\+[0-9]{1,}"
phone_regex = r"[0-9]{5,}"
phone_regex_parenthesis = r"\([0-9]+\)"
name_re = r"name: [\w\.-]+[\w\.-]"


def get_name(text):
    matches = re.findall(name_re, text.lower(), re.MULTILINE)
    if matches:
        print(len(matches))
        matches_sec = re.finditer(name_re, text.lower(), re.MULTILINE)
        full_name = ''
        if matches_sec:
            match = [m.end(0) for m in matches_sec]
            for i in range(len(match)):
                rest_name = ''
                index = match[i]
                while(1):
                    if text[index] != ' ' and re.match(r'\p{L}', text[index]):
                        rest_name += text[index]
                        index += 1
                    elif text[index] == ' ' or text[index] == '\t':
                        rest_name += ' '
                        index += 1
                    else:
                        break
                full_name += ' '+matches[i][6:]+rest_name
            return full_name[1:]
    else:
        nlp = spacy.load('en_core_web_lg')
        doc = nlp(text)
        for ent in doc.ents:
            if(ent.label_ == 'PERSON' and ent.text.strip() not in words.words() and '/n' not in ent.text):
                return ent.text.strip()


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


def get_location(text):
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(text)
    for ent in doc.ents:
        if(ent.label_ == 'GPE' and ent.text.strip() not in words.words() and '/n' not in ent.text):
            return ent.text

# def get_language(text):
#    nlp = spacy.load('en_core_web_lg')
#    doc = nlp(text)
#    for ent in doc.ents:
#        if(ent.label_ == 'LANGUAGE' and ent.text.strip() not in words.words() and '/n' not in ent.text):
#            return ent.text


data = {}
cvs = []
for doc in docs:
    cv = {}
    text = textract.process(doc).decode('utf-8')
    cv['file'] = doc
    print(doc)
    cv['name'] = get_name(text)
    print(cv['name'])
    cv['email'] = get_email(text)
    print (cv['email'])
    cv['phone'] = get_phone(text)
    print (cv['phone'])
    cv['location'] = get_location(text)
    print (cv['location'])
    # cv['language'] = get_language(text)
    # print (cv['language'])
    print("==============")
    cvs.append(cv)
data['data'] = cvs
with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
