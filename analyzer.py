import string

def clean_text(text):
    """Удаляет знаки препинания и приводит текст к нижнему регистру"""
    translator = str.maketrans('', '', string.punctuation + '«»—')
    return text.translate(translator).lower()

def count_words(words):
    """Возвращает количество слов"""
    return len(words)

def find_longest_word(words):
    """Находит самое длинное слово (первое при равенстве длины)"""
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def count_vowels(text, vowels="аеёиоуыэюя"):
    """Подсчитывает количество гласных в тексте"""
    return sum(1 for char in text.lower() if char in vowels)

def word_frequency(words):
    """Создаёт словарь частоты встречаемости слов"""
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


# === Основной блок программы ===

# Получаем текст от пользователя
text = input("Введите текст: ")

# Очищаем текст и разбиваем на слова
cleaned = clean_text(text)
words = cleaned.split()

# Подсчёт данных
total_words = count_words(words)
longest = find_longest_word(words)
vowel_count = count_vowels(text)
frequency = word_frequency(words)

# Вывод результатов
print("\nАнализ текста:")
print(f"Количество слов: {total_words}")
print(f"Самое длинное слово: {longest}")
print(f"Общее количество гласных букв: {vowel_count}")
print("Частота слов:")

for word, count in frequency.items():
    print(f"{word}: {count}")
