from collections import Counter
def get_digit(number, n):
    return number // 10**n % 10

passwords = 0
counter = 108457
while(counter < 562041):
    print("counter:" + str(counter) + "passwords:" + str(passwords))
    num = Counter(str(counter)).most_common()
    adjacents = []
    nice = False
    if(get_digit(counter, 5) == get_digit(counter, 4)):
        adjacents.append(get_digit(counter, 5))
    if(get_digit(counter, 4) == get_digit(counter, 3)):
        adjacents.append(get_digit(counter, 4))
    if(get_digit(counter, 3) == get_digit(counter, 2)):
        adjacents.append(get_digit(counter, 3))
    if(get_digit(counter, 2) == get_digit(counter, 1)):
        adjacents.append(get_digit(counter, 2))
    if(get_digit(counter, 1) == get_digit(counter, 0)):
        adjacents.append(get_digit(counter, 1))
    for x in range(len(adjacents)):
        test = adjacents[x]
        for i in range(len(num)):
            compare = num[i]
            if(int(compare[0]) == int(test) and int(compare[1]) == 2):
                nice = True
    if(nice == True):
        if(get_digit(counter, 5) <= get_digit(counter, 4)):
            if(get_digit(counter, 4) <= get_digit(counter, 3)):
                if(get_digit(counter, 3) <= get_digit(counter, 2)):
                    if(get_digit(counter, 2) <= get_digit(counter, 1)):
                        if(get_digit(counter, 1) <= get_digit(counter, 0)):
                            passwords += 1
    counter += 1
print(passwords)
