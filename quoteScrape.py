from soupGenerator import makesoup
import csv

urlsoup = makesoup("http://quotes.toscrape.com/")

f = csv.writer(open("quotes.csv","w",newline=""))
f.writerow(["Quote","Author"])

quotes = urlsoup.findAll("div",{"class":"quote"})
for quote in quotes:
    text = quote.span.text
    author = quote.findAll("span")[1].small.text
    f.writerow([f"{text}",f"{author}"])
print("Done!")
