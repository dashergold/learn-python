#definitioner här. Ifall du skriver samma sak flera gånger t.ex: %%%% och om du måste ändra så är det jobbigt att ändra alla samtidigt. därför har man definitioner!

#för int'ar
def get_int(prompt):
    print(prompt)
    sValue = input()
    return int(sValue)

#för strängar
def get_str(prompt):
    print(prompt)
    sValue = input()
    return (sValue)

#godis
def buy_candy():
    candy = get_int("Hur många gram godis vill du köpa?")
    if candy >= 200:
        print("Mycket godis kan leda till diabetes.")
    elif candy == 0:
        print("Bra att du tar hand om din hälsa!")
    elif candy < 0:
        print("Snyggt försök. men mig lurar du inte!")
        candy = 0
    return candy

#popcorn
def buy_popcorn():
    while True:
        popcorn = get_str("Vilken storlek vill du ha? (s,m,l)")
        if popcorn == "s":
            return 100
        elif popcorn == "m":
            return 200
        elif popcorn == "l":
            return 300
        elif popcorn == "":
            return 0
        print("Fel storlek försök igen! (s,m,l)")

#film
def play_movie(candy,popcorn):
    print("filmen börjar")
    while candy > 0 or popcorn > 0:
        choice = get_str("vad vill du äta? (p,g)")
        if choice == "p":
            popcorn = eat_popcorn(popcorn)
        elif choice == "g":
            candy == eat_candy(candy)
        else:
            print("försök igen (p,g)")

#äta popcorn
def eat_popcorn(popcorn):
    print("du har "+ str(popcorn) +" g kvar")
    eat = get_int("Hur många gram popcorn vill du äta?")
    if eat < popcorn:
        print("Du åt lite popcorn")
        popcorn = popcorn - eat
    elif eat == popcorn:
        print("du åt upp alla popcorn")
        popcorn = popcorn - eat
    else:
        print("Så mycket popcorn har du inte")
    return popcorn

#äta godis
def eat_candy(candy):
    print("du har "+ str(candy) +" g kvar")
    eat = get_int("Hur många gram godis vill du äta?")
    if eat < candy:
        print("du år lite godis")
        candy = candy - eat
    elif eat == candy:
        print("Du åt upp allt godis")
        candy = candy - eat
    else:
        print("Så mycket godis har du inte")
    return candy

#börja med en fråga. kan bli en definition senare.
age = get_int("hej, hur gammal är du?")
if age < 15:
    print("du är för ung för denna film")
else:
    print("välkommenm in!")

#Händelser under programmet
candy = buy_candy()

popcorn = buy_popcorn()

play_movie(candy,popcorn)

print("Tack för besöket! Ha en trevlig dag!!!!")