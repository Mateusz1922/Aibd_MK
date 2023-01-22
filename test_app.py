from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

testdata1 = ["I think today will be a great day"]#, "I do not think this will turn out well"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

lista = [
    [1,5,2,7,4,8,4,7],
    [58,3,7,3,7,2,9,2,7]
]

@pytest.mark.parametrize('lista', lista)
def test_bubble_sort(lista):
    result = bubble_sort(lista)
    assert sorted(lista) == result
