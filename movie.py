#Hämta ett tal från användaren
def get_int(prompt):
    print(prompt)
    sValue = input()
    return int(sValue)

def print_banner():
    print("%%%%%%%%%%%%%%%%")

def show_movie(candy):
     #Nu börjar filmen!
    print_banner()
    print("tatataatataa...")
    while candy > 0:   
        print("du har "+ str(candy) +" g kvar" )
        eat = get_int("Hur många gram godis vill du äta?")
        if eat < candy:
            print("namnamnam")
            candy = candy - eat
        elif eat == candy:
            print("namnamnam raaaaaaaap")
            print("slut på godis")
            candy = candy - eat
        else:
            print("så mycket godis har du intel.")

def buy_candy():
    candy = get_int("Hur många gram godis skall du köpa?")
    if candy >= 200:
        print ("diabetiker!")
    elif candy == 0:
        print("Bra att du sköter din hälsa")
    elif candy < 0:
        print("Snyggt försök!")
        candy = 0
    return candy 

#Filmstart
print_banner()
age = get_int("Hej hur gammal är du?")
if age < 15:
    print("Du är för ung!")
else:
    print("Välkommen in")

    candy = buy_candy()

    show_movie(candy) 
    
    print_banner()
    print("Tack för besöket!")
