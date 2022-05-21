'''
Описати функцію RearRange(x, y), яка перевіряє, чи можливо переставивши букви в
слові х отримати слово y
'''


def RearRange(x, y):
    x.sort()
    y.sort()
    if len(x) != len(y):
        return "Неможливо отримати слово"
    else:
        for i in range(len(x)):
            if x[i] != y[i]:
                print('Неможливо отримати слово')
    return 'Можливо отримати слово'


word_x = list(input("Введіть слово x: "))
word_y = list(input("Введіть слово y: "))
print(RearRange(word_x, word_y))
