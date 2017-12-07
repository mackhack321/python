nums = []
usrInput = "null"
while usrInput != "done":
    usrInput = raw_input("Give a number to add: ")
    if usrInput == "done":
        break
    nums.append(float(usrInput))
    print(nums)

for i in range(len(nums)):
    nums[i] = nums[i] ** nums[i]

print "The sum of the squares of the numbers you gave is: " + str(sum(nums))
