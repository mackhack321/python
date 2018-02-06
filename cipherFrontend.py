import cipher
cipher.showLauncher()
choice = input("Choose a function: ")
if choice == "1":
    badKey = True
    while badKey is True:
        try:
            usrString = input("Text to encode: ")
            usrKey = int(input("Key: "))
            if usrKey == 0 or usrKey > 25:
                print("Bad key")
                continue
            badKey = False
            print("".join(cipher.encrypt(usrString, usrKey)))
        except ValueError:
            print("Bad key type")
    cipher.showLauncher()

elif choice == "2":
    badKey = True
    while badKey is True:
        try:
            usrString = input("Text to decode: ")
            usrKey = int(input("Key: "))
            if usrKey == 0 or usrKey > 25:
                print("Bad key")
                continue
            print("".join(cipher.decrypt(usrString, usrKey)))
            badKey = False
        except ValueError:
            print("Bad key type")
    cipher.showLauncher()

elif choice == "3":
    badKey = True
    while badKey is True:
        usrfile = input("Filename (exclude extension): ")
        usrkey = int(input("Key: "))
        if usrkey == 0 or usrkey > 25:
            print("Bad key")
            continue
        badKey = False
        try:
            cipher.encryptFromFile(f"{usrfile}.txt", usrkey)
        except FileExistsError as e:
            print(f"File Not Found: {e}")
            cipher.showLauncher()
    cipher.showLauncher()
