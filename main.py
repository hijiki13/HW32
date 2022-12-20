# TODO 1) Можно сделать без повторения кода? (все функции одинаковые кроме имени файла. Но они привязаны к потокам. У всех потоков есть start()/join(), но в цикл их засунуть нельзя - не будут выполняться одновременно.)
# 2) Как еще можно остановить все потоки? Если код большой, будет супер неудобно постоянно делать проверку.
# 3) Семафор нужен? В задании написано все потоки должны выполняться одновременно, но их может быть и 100...

import random
import string
import threading

def generate_files(insert_word):
    letters = string.ascii_lowercase
    i = 0
    to_insert = random.randint(1, 10)

    for j in range(1, 11):
        with open(f'text{j}.txt', 'w+') as f:
            while i < random.randint(1000, 2500):
                word = ''.join(random.sample(letters, len(insert_word)))
                f.writelines([word, '\n'])
                i += 1
        
        # чтобы слово точно было хотя бы в одном из файлов (чем длинее слово, тем меньше шанс его случайно сгенерировать)        
        if j == to_insert:
            with open(f'text{to_insert}.txt', 'r+') as f2:
                text = f2.readlines()
                text.insert(random.randint(0, len(text)), insert_word+'\n')
                f2.writelines(text)
        i = 0

# какое слово найти
to_find = input('Word to find: ').lower()
# создает 10 файлов со случайными "словами" длиной заданого слова
generate_files(to_find)
# для проверки найдено соответствие или нет
found = 0

def search1():
    # для проверки
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text1.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search2():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text2.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return

    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search3():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text3.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))

    if found:
        return

    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search4():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text4.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search5():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text5.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search6():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text6.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search7():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text7.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search8():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text8.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search9():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text9.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search10():
    # print('Thread start')
    global to_find
    global found
    if found:
        return

    with open('text10.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if to_find in text:
        found = text.index(to_find)
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')


th1 = threading.Thread(target=search1)
th2 = threading.Thread(target=search2)
th3 = threading.Thread(target=search3)
th4 = threading.Thread(target=search4)
th5 = threading.Thread(target=search5)
th6 = threading.Thread(target=search6)
th7 = threading.Thread(target=search7)
th8 = threading.Thread(target=search8)
th9 = threading.Thread(target=search9)
th10 = threading.Thread(target=search10)

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()
th7.start()
th8.start()
th9.start()
th10.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
th6.join()
th7.join()
th8.join()
th9.join()
th10.join()