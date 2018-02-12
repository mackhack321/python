mess = 'If you want to keep a secret, don\'t tell it to even you.' # sets input
encoded = ' ' # makes new empty string
i = len(mess) - 1 # grabs length of input string
while i >= 0: # do this while i is more than or equal to 0
    encoded = encoded + mess[i] # adds the last char to the new string, then the second to last, and so on
    print(i,mess[i],encoded) # prints progress
    i = i - 1 # take 1 away from i, which moves on to the next character

print(encoded) # prints result
