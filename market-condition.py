cont, tot, et1000, v_cheap, cheap = 0, 0, 0, 0, ''

while True:
    print('\n\033[40m' + ('~~' * 10) + ' Market ' + ('~~' * 10) + '\033[m')
    name = str(input('Type the product name: ')).strip().title()
    price = float(input('Type the product price: $'))
    c = str(input('Want you to continue [Y/N]? ')).strip().upper()[0]
    while c != 'Y' and c != 'N':
        print('\033[37mInvalid answer. Try again.')
        c = str(input('Want you to continue [Y/N]? ')).strip().upper()[0]
    tot += price
    if cont == 0:
        cheap = name
        v_cheap = price
    else:
        if price < v_cheap:
            cheap = price
    if price > 1000:
        et1000 += 1
    cont += 1
    if c == 'N':
        break

print(f'''
1) The total expended in this purchase: ${tot:.2f}
2) The total of products more expensive than $1000: {et1000}
3) The cheaper product: {cheap}
\033[37m{'END':-^60}''')
