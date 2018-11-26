#total = 0.0
#n = 0
#while True:
#    sNumber = input()
#    if sNumber == "":
#        break
#    number = int(sNumber)
#    total += number
#    n += 1
#print("The average is "+ str(total/n))

def average2(n):
    avg = (n + 1) / 2
    print("The average is " +str(avg))

def average(n):
    total = 0
    for i in range(n):
        total += i + 1
    print("The average is "+ str(total/n))

q = 100000000 
average2(q)
average(q)
