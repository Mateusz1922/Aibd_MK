from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubble_sort(lista: list):
    lista1 = lista[:]
    n = len(lista1)
    swap = True
    while n > 1 and swap:
        swap = False
        for i in range(1, n):
            if lista1[i-1] > lista1[i]:
                lista1[i-1], lista1[i] = lista1[i], lista1[i-1]
                swap = True
        n = n - 1
    return lista1
#
# lista = [1,5,7,6,3]
# print(bubble_sort(lista))

# Wnioski
# Podejście TDD jest dość efektywne podczas pracy nad jakimś projektem, w którym mamy dokładnie sprecyzowane, np. przez
# klienta co powinniśmy otrzymać na wyjściu naszego programu, który np. zarządza aplikacją. Jednak bardzo często taki sam
# wygląd czy funkcjonalność może być bardzo trudna do osiągnięcia, szczególnie przy bardzo skomplikowanych projektach,
# przez co należy wtedy zastosować podejście BDD. W tym przypadku członkowie zespołu oraz klienci nie posiadający wiedzy
# technicznej mogą na bieżąco mieć wgląd w to, co jest pokrywane przez testy i jakie są ich wyniki.