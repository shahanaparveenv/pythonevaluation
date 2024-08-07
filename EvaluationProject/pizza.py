def pizzaorder():
    size=input("pizza size: small,medium or large ")
    pepperoni=input("add pepperoni : yes or no ")
    extra_cheese=input("add extra cheese : yes or no ")
    bill = 0

    if size.lower() == "small":
        bill=150
        if pepperoni.lower() == "yes":
            bill+=20
        if extra_cheese.lower() == "yes":
            bill+=10

    elif size.lower() == "medium":
        bill=200
        if pepperoni.lower() == "yes":
            bill+=30
        if extra_cheese.lower() == "yes":
            bill+=10

    elif size.lower() == "large":
        bill = 250
        if pepperoni.lower() == "yes":
            bill += 30
        if extra_cheese.lower() == "yes":
            bill += 10

    else:
        print("invalid entry")

    print("Bill:"+str(bill))

pizzaorder()
