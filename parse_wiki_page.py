from bs4 import BeautifulSoup
import html
import re

def prepare_text(text):
    sent = ' '.join(map(lambda x: "<p>"+x+"</p>", 
                        map(str.strip, 
                            filter(len, 
                                   ' '.join(map(lambda string: re.sub(r"\xa0", " ", re.sub('\\\\"','"', string)), 
                                                filter( lambda x: "Section::::" not in x, 
                                                       map(str.strip, 
                                                           map(lambda x:x+'.', 
                                                               filter(len, 
                                                                      BeautifulSoup(html.unescape(text.strip('\" '))).get_text().split('.'))
                                                              )
                                                          )
                                                      )
                                               )
                                           ).split('\\n')
                                  ) 
                           )
                       )
                   )
    return sent

    
#https://ru.wikipedia.org/wiki/Матрица_(фильм)
with open('./input/ru/The_Matrix.json', encoding='utf-8') as f:
    title, raw_text, _ = f.readline().split('\t')
    out_text = prepare_text(raw_text)
    

#alternative function
def _prepare_text(text):
    text = text.strip('\" ')
    text = html.unescape(text)
    parser = BeautifulSoup(text)
    sent = parser.get_text()
    sent = sent.split('.')
    sent = filter(len, sent) #remove last empty element
    sent = map(lambda x:x+'.', sent)
    sent = map(str.strip, sent)
    sent = filter( lambda x: "Section::::" not in x, sent)
    # # sent = list(map(lambda x: x[x.find('Section::::')+len('Section::::'):] if 'Section::::' in x else x, sent))
    sent = map(clean_str, sent)
    sent = ' '.join(sent).split('\\n')
    sent = filter(len, sent) #remove empty string in list ["a", "", "b" ] => ["a", "b"]
    sent = map(str.strip, sent)
    sent = map(lambda x: "<p>"+x+"</p>", sent)
    sent = ' '.join(sent)
    return sent