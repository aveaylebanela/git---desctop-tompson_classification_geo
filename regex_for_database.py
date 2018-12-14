import re

def opener(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.split(']')
    return text

def cleaner(text):
    for i,c in enumerate(text):
        c = c.strip("\"").strip(",")
        #print(c)
        iden = re.search('\d+',c) # id
        if iden:
            iden = iden.group(0)
        #    print(iden)
        name = re.findall('\"(.+?)\"',c) # name of tale
        if name:
                print(name[1])
        author = re.search('author=\S*>(.+?)</a> -(.+?)</p>', c) # finder?
        if author:
            author = author.group(1)
        country = re.search('country=(.+?)>', c) # country of origin
        if country:
            country = country.group(1)
            country = country.strip('"')[:-1]
        #    print(country)
        index = re.search('atu=(.+?)>',c) # atu index
        if index: 
            index = index.group(1)
            index = index.strip('"')[:-1]
        #    print(index)
        translation = re.findall('<p>\s*<b>(.+?)</b>',c)
        #print(translation)
        year = re.search('author=\S*>(.+?)</a> - (.+?)</p>',c)
        if year:
            year = year.group(2)
        #    print(year)

def main():
    a = opener("database_with_tables.txt")
    cleaner(a)

main()
