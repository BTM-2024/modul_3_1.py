#Модуль 3_4. Задача "Однокоренные" по уроку "Произвольное число параметров"
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:    # Перебирает слова в последовательности
        if root_word.lower() in word.lower() or word.lower() in root_word.lower(): # переводит все слова в нижний регистр и
                                                                                 # проверяет содержится ли исходное слово в последовательности или наоборот
            same_words.append(word)     # добавляет в новый список нужные слова
    return (same_words)     # возвращаем новый список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)