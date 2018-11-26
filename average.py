total = 0.0
n = 0
while True:
    sNumber = input()
    if sNumber == "":
        break
    number = int(sNumber)
    total += number
    n += 1
print("The average is "+ str(total/n))
