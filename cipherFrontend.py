import cipher
choice = 0
cipher.showLauncher()
while choice != "9":
    choice = input("Choose a function: ")

    if choice == "1":
        usrString = input("Text to encode: ")
        usrKey = cipher.getKey()
        print("".join(cipher.encrypt(usrString, usrKey)))
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "2":
        usrString = input("Text to decode: ")
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
        usrString = input("Text to decode with brute force: ")
        usrRunthrus = int(input("How many times? "))
        cipher.bruteforce(usrString, usrRunthrus)
        cipher.showLauncher()

    elif choice == "6":
        usrfile = input("Filename (exclude extension): ")
        cipher.bruteforceFromFile(f"{usrfile}")
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "7":
        usrString = input("Text to encode: ")
        print("".join(cipher.reverseCipher(usrString)))
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "8":
        usrfile = input("Filename (exclude extension): ")
        cipher.reverseCipherFromFile(f"{usrfile}")
        input("Press enter to return to the launcher...")
        cipher.showLauncher()

    elif choice == "9":
        pass

    else:
        print("Invalid choice")
