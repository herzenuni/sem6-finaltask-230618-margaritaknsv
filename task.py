#функция подсчета слов

def CountOfWords(string):
    count = 0
    string = string.strip()
    for i in range(1, len(string)-1):
        if string[i] == ' ' and string[i - 1] != ' ':
            count += 1
    if len(string)-1 != ' ':
        count += 1
    return "Количество слов в строке: {}".format(count)

#функция подсчета длинны слова

def LenOfWord(string):
    words = string.strip().split(' ')
    index = -1
    while True:
        index += 1
        if (index == len(words)):
            break
        if (words[index] == ' '):
            continue
        yield len(words[index])

text = 'What about zachet'
g = LenOfWord(text)

print(CountOfWords(text))

print(next(g))
print(next(g))
print(next(g))


#unittests

if __name__ == '__main__':
    import unittest

    class MyTests(unittest.TestCase):

        def test_string(self):
            self.assertEqual(CountOfWords("hello world"), ("Количество слов в строке: 2"))
            self.assertEqual(CountOfWords("my name is Rita"), ("Количество слов в строке: 4"))

        def test_string_not(self):
            self.assertNotEqual(CountOfWords("hello world"), ("Количество слов в строке: 3"))
            self.assertNotEqual(CountOfWords("my name is Rita"), ("Количество слов в строке: 3"))

    unittest.main(verbosity=2)