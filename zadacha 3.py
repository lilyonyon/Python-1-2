import string
print ('Введите текст: ')
text = input()
counter = {}
max_word = ''
punc = string.punctuation #тут знаки препинания
for d in text: #удаляем знаки препинания из строки, чтобы они не учитывались при поиске слов
    if d in punc:
        text1 = text.replace(d,"")
line = text1.split() #разделяем строку на слова
for word in line:
    counter[word] = counter.get(word, 0) + 1
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
for word in line: #ищем самое длинное слово:
    if len(word) > len(max_word):
        max_word = word
print("Самое часто встречающееся слово в строке: ", min(most_frequent))
print("Самое длинное слово в строке: ", max_word)
