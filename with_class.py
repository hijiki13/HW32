import string, random, threading


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


class Search:
    _found = False

    def __init__(self, file, word) -> None:
        self.file = file
        self.word = word

    def __check_if_found(self):
        if self._found:
            return True
        return False

    def search_it(self):
        if self.__check_if_found():
            return

        with open(self.file, 'r') as f:
            text = f.read()
            text = list(text.split('\n'))

        if self.__check_if_found():
            return

        if self.word in text:
            Search._found = True
            found_ind = text.index(self.word)
            print(f'Found in {f.name} at {found_ind + 1} line. All threads stoped.')
            return
        
        # for debug
        print(f'thread {self.file} ends')

# какое слово найти
to_find = input('Word to find: ').lower()
# создает 10 файлов со случайными "словами" длиной заданого слова
generate_files(to_find)

# creating obj
obj1 = Search('text1.txt', to_find)
obj2 = Search('text2.txt', to_find)
obj3 = Search('text3.txt', to_find)
obj4 = Search('text4.txt', to_find)
obj5 = Search('text5.txt', to_find)
obj6 = Search('text6.txt', to_find)
obj7 = Search('text7.txt', to_find)
obj8 = Search('text8.txt', to_find)
obj9 = Search('text9.txt', to_find)
obj10 = Search('text10.txt', to_find)

threads = []
objects = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10]

# starting threads
for obj in objects:
    thread = threading.Thread(target=obj.search_it)
    threads.append(thread)

for th in threads:
    th.start()

for th in threads:
    th.join()