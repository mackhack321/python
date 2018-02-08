import cipher
choice = 0
cipher.showLauncher()
while choice != "6":
    choice = input("Choose a function: ")

    if choice == "1":
        usrString = input("Text to encode: ").lower()
        usrKey = cipher.getKey()
        print("".join(cipher.encrypt(usrString, usrKey)))
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "2":
        usrString = input("Text to decode: ").lower()
        usrKey = cipher.getKey()
        print("".join(cipher.decrypt(usrString, usrKey)))
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "3":
        usrfile = input("Filename (exclude extension): ")
        usrkey = cipher.getKey()
        cipher.encryptFromFile(f"{usrfile}", usrkey)
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "4":
        usrfile = input("Filename (exclude extension): ")
        usrkey = cipher.getKey()
        cipher.decryptFromFile(f"{usrfile}", usrkey)
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "5":
        usrString = input("Text to decode with brute force: ").lower()
        cipher.bruteforce(usrString)
        cipher.showLauncher()

    elif choice == "6":
        pass

    else:
        print("Invalid choice")
