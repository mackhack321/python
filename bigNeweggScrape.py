from soupGenerator import makesoup
import csv

urltxt = open("urls.txt","r")
urls = urltxt.readlines()
urltxt.close()

f = open("bigdata.csv","w")
f.write("Brand,Name,Shipping,Price\n")

for url in urls:
    urlsoup = makesoup(url)
    containers = urlsoup.findAll("div",{"class":"item-container"})
    for container in containers:
        productName = container.a.img["title"].replace(","," |")
        try:
            brandName = container.div.div.a.img["title"]
        except:
            brandName = "NA"

        itemaction = container.find("div",{"class":"item-action"})
        try:
            dollars = itemaction.ul.find("li",{"class":"price-current"}).strong.text
            cents = itemaction.ul.find("li",{"class":"price-current"}).sup.text
            price = dollars.replace(",",".") + cents
        except AttributeError:
            price = "NA"
        shipping = itemaction.ul.find("li",{"class":"price-ship"}).text.strip()
        f.write(f"{brandName},{productName},{shipping},{price}\n")
    print("Done!")
f.close()
