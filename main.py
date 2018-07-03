import argparse
import getpass
import json
import regex as re
import spacy
import textract
from nltk.corpus import words

email_re = r"[\w\.-]+@[\w\.-]+\.\w+"
phone_regex_plus = r"\+[0-9]{1,}"
phone_regex = r"[0-9]{5,}"
phone_regex_parenthesis = r"\([0-9]+\)"
name_re = r"name: [\w\.-]+[\w\.-]"
skills_re = r"skills+\n"
experience_re = r"(experience|employment|career)+\n"
titles_skilss = ['career', 'language', 'experience', 'employment']
titles_experience = ['skills', 'language']


def find_word_in_sentence(words, sentence):
    for word in words:
        if word in sentence:
            return True, word
    return False, ''


def get_name(text, nlp):
    matches = re.findall(name_re, text.lower(), re.MULTILINE)
    if matches:
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
        doc = nlp(text.replace('\n\n', '\n'))
        for ent in doc.ents:
            if(ent.label_ == 'PERSON' and ent.text.strip() not in words.words() and re.match(r'\p{L}', ent.text.strip())):
                if '\n' in ent.text:
                    return ent.text.strip().split('\n')[0]
                else:
                    return ent.text.strip()
        return ("no name detected")


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


def get_location(text, doc):
    for ent in doc.ents:
        if(ent.label_ == 'GPE' and ent.text.strip() not in words.words() and '/n' not in ent.text):
            return ent.text
    return("no location detected")


def get_language(text, doc):
    for ent in doc.ents:
        if(ent.label_ == 'LANGUAGE' and ent.text.strip() not in words.words() and '/n' not in ent.text):
            return ent.text
    return("no location detected")


def get_skills(text):
    matches = re.findall(skills_re, text.lower(), re.MULTILINE)
    if matches:
        matches_sec = re.finditer(skills_re, text.lower(), re.MULTILINE)
        rest_name = ''
        if matches_sec:
            match = [m.end(0) for m in matches_sec]
            index = match[0]
            skill_index = match[0]
            while(index < len(text)):
                rest_name += text[index]
                index += 1
            sentences = rest_name.split('\n')
            for sentence in sentences:
                if len(sentence) > 4:
                    find_it, title = find_word_in_sentence(
                        titles_skilss, sentence.lower())
                    if find_it:
                        matches_sec = re.finditer(
                            skills_re, text.lower(), re.MULTILINE)
                        if matches_sec:
                            match = [m.start(0) for m in matches_sec]
                            other_index = match[0]
                            for i in range(len(match)):
                                if match[i] > skill_index:
                                    other_index = match[i]
                            skill_resume = ''
                            while(skill_index < other_index):
                                skill_resume += text[skill_index]
                                skill_index += 1
                            rest_name = skill_resume
            return rest_name
    else:
        return ("no skill detected")


def get_experience(text):
    matches = re.findall(experience_re, text.lower(), re.MULTILINE)
    if matches:
        matches_sec = re.finditer(experience_re, text.lower(), re.MULTILINE)
        rest_name = ''
        if matches_sec:
            match = [m.end(0) for m in matches_sec]
            index = match[0]
            skill_index = match[0]
            while(index < len(text)):
                rest_name += text[index]
                index += 1
            sentences = rest_name.split('\n')
            for sentence in sentences:
                if len(sentence) > 4:
                    find_it, title = find_word_in_sentence(
                        titles_experience, sentence.lower())
                    if find_it:
                        matches_sec = re.finditer(
                            experience_re, text.lower(), re.MULTILINE)
                        if matches_sec:
                            match = [m.start(0) for m in matches_sec]
                            other_index = match[0]
                            for i in range(len(match)):
                                if match[i] > skill_index:
                                    other_index = match[i]
                            experience_resume = ''
                            while(skill_index < other_index):
                                experience_resume += text[skill_index]
                                skill_index += 1
                            rest_name = experience_resume
            return rest_name
    else:
        return ("no experience detected")


def main():
    parser = argparse.ArgumentParser(
        description='This tool lets you parse a cv')
    parser.add_argument(
        '-f', '--file', help='The cv file you want to parse', required=True)
    args = vars(parser.parse_args())
    data = {}
    cv = {}
    text = textract.process(args['file']).decode('utf-8')
    nlp = spacy.load('en_core_web_lg')
    doct = nlp(text.replace('\n\n', '\n'))
    cv['file'] = args['file']
    print(args['file'])
    cv['name'] = get_name(text, nlp)
    cv['email'] = get_email(text)
    cv['phone'] = get_phone(text)
    cv['location'] = get_location(text, doct)
    cv['language'] = get_language(text, doct)
    cv['skills'] = get_skills(text)
    cv['experience'] = get_experience(text)
    print("==============")
    data['data'] = cv
    with open('data.json', 'w') as f:
        output = json.dump(data, f, ensure_ascii=False)
        return output


if __name__ == '__main__':
    main()
