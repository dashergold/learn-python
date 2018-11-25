def verify(expected,actual):
    print(actual)
    if expected != actual:
        print("FEL!")
        return False
    else:
        return True

#Hur man använder heltal
correct = 0
a = 5
b = 8
c = 12
if verify(13,a + b):
    correct += 1

a = 8
b = -9
c = 16
if verify(17,a - b):
    correct += 1

print("du fick " + str(correct) + " rätt")

