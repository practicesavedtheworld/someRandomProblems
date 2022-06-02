# На вход программы подается текст. Определите, какое слово в нем встречается
# чаще всего и напечатайте его в нижнем регистре.
# Слова "the" и "The" считаются одним словом:) Если таких слов несколько, напечатайте
# первое в лексикографическом порядке

text = input().lower().split()


def solution(some_text) -> str:
    d = {el: some_text.count(el) for el in some_text}
    return [k for k, v in d.items() if max(d.values()) == v][0]


if __name__ == '__main__':
    print(solution(text))
