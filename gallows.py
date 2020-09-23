import random


words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
letters = 'abcefgiklnoprstuvxy'
secret = random.choice(words)


def game(s, test):
    print('Я загадал слово из ' + str(len(s)) + ' букв на английском языке. Отгадайте его, совершив не более четырёх ошибок.')
    s_p = ''
    for _ in range(len(s)):
        s_p += '_ '    
    print(s_p)

    p_point = 0
    win = False
    while p_point != 4 and not win:
        if test:
            x = random.choice(letters)
            print("Введите букву: ", x)
        else:
            x = input("Введите букву: ")
        if x in s:
            i = 0
            for l in secret:
                if l == x:
                    s_p = s_p[:i*2] + x + s_p[i*2+1:]
                i += 1
            print(s_p)
        else:
            p_point += 1
            print('Нет такой буквы. Осталось попыток: ', 4 - p_point)
        if '_' not in s_p:
            result = 'Вы выиграли! Поздравляю!'
            # print('Вы выиграли! Поздравляю!')
            win = True
        if p_point == 4:
            result = 'Вы проиграли. Попытки закончились.'
            # print('Вы проиграли. Попытки закончились.')
    return result
        

# Раскомментируйте строку ниже для для запуска игры в ручном режиме
# print(game(secret, False))