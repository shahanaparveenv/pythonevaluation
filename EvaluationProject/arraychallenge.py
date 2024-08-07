
def ArrayChallenge(array):
    array1=array
    initial_price=array1[0]
    profit=0

    for i in array1:
        if i < initial_price:
            initial_price = i

        elif i - initial_price > profit:
            profit = i - initial_price

    print(profit)

test = [10,8,9,20]
ArrayChallenge(test)


array = [44,30,24,32,35,30,40,38,15]
ArrayChallenge(array)
