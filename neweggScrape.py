from soupGenerator import makesoup
urlsoup = makesoup("https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709")

f = open("data.csv","w")
f.write("Brand,Name,Shipping,Price\n")

containers = urlsoup.findAll("div",{"class":"item-container"})
for container in containers:
    productName = container.a.img["title"].replace(","," |")
    try:
        brandName = container.div.div.a.img["title"]
    except AttributeError:
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
f.close()
print("Done!")
