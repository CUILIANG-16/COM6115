import re

PATH = 'lab/data/RGX_DATA.html'


def load(PATH):
    with open(PATH) as handle:
        text = handle.read()
    return text

text = load(PATH)

# QUESTION: 1
def Q1(text):
    rule = re.compile("<(.*?)>",re.I)
    for tag in rule.findall(text):
        print("TAG: {}".format(tag))

Q1(text)

# QUESTION: 2
def Q2(text):
    rule = re.compile("<(.*?)>",re.I)
    tag_dict = {'p':"OPENTAG",'/p':"CLOSETAG"}
    for tag in rule.findall(text):
        print(tag_dict[tag],end='') if tag in tag_dict else print("TAG",end='')
        print(': {}'.format(tag))

Q2(text)

# QUESTION: 3
def Q3(text):
    rule = re.compile("<(.*?)>",re.I)
    tag_dict = {'p':"OPENTAG:",'/p':"CLOSETAG:"}
    for tag in rule.findall(text):
        if tag in tag_dict:
            print(tag_dict[tag],tag)
        elif ' ' in tag:
            opentag, param = tag.split()[0], tag.split()[1:]
            print("OPENTAG:",opentag)
            for i in param:
                print(' '*3+"PARAM:",i)
        else:
            print("TAG:",tag)

Q3(text)

# QUESTION: 4
def Q4(text):
    pass
