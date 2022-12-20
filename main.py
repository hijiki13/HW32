# TODO 1) Можно сделать без повторения кода? (все функции одинаковые кроме имени файла. Но они привязаны к потокам. У всех потоков есть start()/join(), но в цикл их засунуть нельзя - не будут выполняться одновременно.)
# 2) Как еще можно остановить все потоки? Если код большой, будет супер неудобно постоянно делать проверку.

import random
import string
import threading

def generate_files():
    letters = string.ascii_lowercase
    word = ''
    i = 0

    for j in range(1, 11):
        with open(f'text{j}.txt', 'w') as f:
            while i < 5000:
                # if u change val in sample() (int one), u change len of random word
                word = ''.join(random.sample(letters, 3))
                f.writelines([word, '\n'])
                i += 1
        i = 0

# создает 10 файлов со случайным текстом
generate_files()
found = 0

def search1():
    # для проверки
    # print('Thread start')
    global found
    if found:
        return

    with open('text1.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search2():
    # print('Thread start')
    global found
    if found:
        return

    with open('text2.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return

    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search3():
    # print('Thread start')
    global found
    if found:
        return

    with open('text3.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))

    if found:
        return

    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search4():
    # print('Thread start')
    global found
    if found:
        return

    with open('text4.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search5():
    # print('Thread start')
    global found
    if found:
        return

    with open('text5.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search6():
    # print('Thread start')
    global found
    if found:
        return

    with open('text6.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search7():
    # print('Thread start')
    global found
    if found:
        return

    with open('text7.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search8():
    # print('Thread start')
    global found
    if found:
        return

    with open('text8.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search9():
    # print('Thread start')
    global found
    if found:
        return

    with open('text9.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
        print(f'Found in {f.name} at {found + 1} line. All threads stoped.')
        return
    # print('Thread ended')

def search10():
    # print('Thread start')
    global found
    if found:
        return

    with open('text10.txt', 'r') as f:
        text = f.read()
        text = list(text.split('\n'))
        
    if found:
        return
        
    if 'cat' in text:
        found = text.index('cat')
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

print(threading.active_count())

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