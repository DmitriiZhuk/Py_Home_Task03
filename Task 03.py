# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
#  Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

import json 

file = open("Task03_lib.txt", encoding="utf-8")
data = file.read()
file.close()

data = "{"+data+"}"

dict = json.loads(data)

def continue_Dialog(speak_to_me):
    print("Я не знаю что такое " + speak_to_me)
    yes_no = input("Хотите внесем вопрос и ответ на него в мою библиотеку? (Y/N) ")
    if yes_no.lower() == 'y':
        add_to_dict(speak_to_me)
    else:
        print("Спасибо за общение")

def add_to_dict(speak_to_me):
    phrase = speak_to_me
    print("Вы сказали: " + phrase)
    phrase_reply = input("Введите ответ на эту фразу: ")
    do_add_dict(phrase, phrase_reply)

def do_add_dict(phrase, phrase_reply):
    lib_file = open("Task03_lib.txt", "a+", encoding="utf-8")
    lib_file.write(','+'\n'+'"'+phrase+'"'+":"+'"'+phrase_reply+'"')
    lib_file.close()
    print("Ваш вопрос-ответ успешно записан!")

checker = False
answer = None

speak_to_me = input("Введите вопрос: ")

for key in dict:
    if key.lower() == speak_to_me.lower():
        checker = True
        answer = dict[key]

if checker == True:
    print(answer)
else:
    continue_Dialog(speak_to_me)