import numpy as np
import pandas as pd
import PyPDF2
import re

def replace_all(repls, str):
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str)          

def find_messages(content):
    message_table_content = list()
    begin_pattern = r"^\w{3}(\d{4}|\d{4}R1)$"
    end_pattern = r"^\/\w{3}(\d{4}|\d{4}R1)$"

    content_list = list(filter(lambda  x: x != '', content.split('\n ')))
    content_list = list(map(lambda x: replace_all({'\n':'', '<':'', '>':''},x), content_list))
    begin_message_table = False
    for item in content_list:     
        if re.search(end_pattern, item): # is last tag of message
            begin_message_table = False

        if begin_message_table:
            message_table_content.append(item)
        
        if re.search(begin_pattern, item): # is first tag of message
            begin_message_table = True
            message_table_content.append('0')
            message_table_content.append(item)
            message_table_content.append('')
            message_table_content.append('')
        
    num = np.array(message_table_content)
    reshaped = num.reshape(len(num)//4,4)
    df = pd.DataFrame(reshaped, columns=['tag_index','tag','description','multiplicity'])
    print(df.head())

    return df                


def process_messages(df):
    parent_tag = df['tag'][0]
    df['parent_tag'] = parent_tag
    #TODO: MUDAR O PARENT TAG PARA O CASO DE GRUPOS
    print(df.head())
    

file = open('Catalogo_Volume_I_501.pdf', 'rb')
fileReader = PyPDF2.PdfFileReader(file)

page = fileReader.getPage(104)
page_content = page.extractText()

df = find_messages(page_content)
process_messages(df)





