import transposition as tr
txtfile = open("problematicString.txt")
lines = txtfile.readlines()
txtfile.close()
for line in lines:
    tr.brute(line, "|")
