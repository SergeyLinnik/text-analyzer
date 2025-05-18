import string

# Получаем текст от пользователя
text = input("Введите текст: ")

# Удаляем знаки препинания и приводим к нижнему регистру
translator = str.maketrans('', '', string.punctuation + '«»—')
cleaned_text = text.translate(translator).lower()

# Разбиваем текст на слова
words = cleaned_text.split()

# 1. Количество слов
word_count = len(words)

# 2. Самое длинное слово
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# 3. Подсчёт гласных (русские)
vowels = "аеёиоуыэюя"
vowel_count = 0
for letter in text.lower():
    if letter in vowels:
        vowel_count += 1

# 4. Частота встречаемости слов
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Вывод результатов
print("\nАнализ текста:")
print(f"Количество слов: {word_count}")
print(f"Самое длинное слово: {longest_word}")
print(f"Общее количество гласных букв: {vowel_count}")
print("Частота слов:")

for word, count in word_frequency.items():
    print(f"{word}: {count}")
