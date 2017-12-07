ls = []
get = "null"
while get != "Done":
    get = input("Add an input to the list or type \"Done\"")
    if get == "Done":
        break
    ls.append(get)
    print(ls)
