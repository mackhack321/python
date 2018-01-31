from soupGenerator import makesoup
urlsoup = makesoup("http://www.spanishdict.com/conjugate/hablar")
tables = urlsoup.findAll("table",{"class":"vtable"})

for table in tables:
    tense = table.tr.td.next.a.span.text
    print(tense)
#print(tables[0].tr.td.next.a.span.text)
