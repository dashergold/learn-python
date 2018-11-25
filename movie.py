#Hämta ett tal från användaren
def get_int(prompt):
    print(prompt)
    sValue = input()
    return int(sValue)

def print_banner():
    print("%%%%%%%%%%%%%%%%")

def eat_popcorn(popcorn):
    print("du har "+ str(popcorn) +" g kvar" )
    eat = get_int("Hur många gram popcorn vill du äta?")
    if eat < popcorn:
        print("knaster,knaster")
        popcorn = popcorn - eat
    elif eat == popcorn:
        print("kanster,knaster raaaaaaaap")
        print("slut på popcorn")
        popcorn = popcorn - eat
    else:
        print("så mycket popcorn har du inte.")
    return popcorn


def eat_candy(candy):
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
        print("så mycket godis har du inte.")
    return candy

def show_movie(candy,popcorn):
     #Nu börjar filmen!
    print_banner()
    print("tatataatataa...")
    while candy > 0 or popcorn > 0:
        choice = get_str("vad vill du äta? (p,g)")
        if choice == "p":
            popcorn = eat_popcorn (popcorn)
        elif choice == "g":
            candy = eat_candy(candy)
        else:
            print ("försök igen")


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

def get_str(prompt):
    print(prompt)
    sValue = input()
    return sValue

def buy_popcorn():
    while True: 
        popcorn = get_str("Vilken storlek vill du ha? (s, m, l)")
        if popcorn == "s":
            return 100
        elif popcorn == "m":
            return 200
        elif popcorn == "l":
            return 300
        elif popcorn == "":
            return 0
        print("Fel storlek, prova igen")

#Filmstart
print_banner()
age = get_int("Hej hur gammal är du?")
if age < 15:
    print("Du är för ung!")
else:
    print("Välkommen in")

    candy = buy_candy()

    popcorn = buy_popcorn()

    show_movie(candy,popcorn)
    
    print_banner()
    print("Tack för besöket!")
