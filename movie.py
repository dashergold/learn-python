#Filmstart
print("Hej hur gammal är du?")
sAge = input()
age = int(sAge)
if age < 15:
    print("Du är för ung!")
else:
    print("Välkommen in")
    print("Hur många gram godis skall du köpa?")
    sCandy = input()
    candy = int(sCandy)
    if candy >= 200:
        print ("diabetiker!")
    elif candy == 0:
        print("Bra att du sköter din hälsa")
    elif candy < 0:
        print("Snyggt försök!")
    
    #Nu börjar filmen!
    print("tatataatataa...")
    while candy > 0:   
        print("du har "+ str(candy) +" g kvar" )
        print("Hur många gram godis vill du äta?")
        sEat = input()
        eat = int(sEat)
        if eat < candy:
            print("namnamnam")
            candy = candy - eat
        elif eat == candy:
            print("namnamnam raaaaaaaap")
            print("slut på godis")
            candy = candy - eat
        else:
            print("så mycket godis har du intel.")

    print("Tack för besöket!")
