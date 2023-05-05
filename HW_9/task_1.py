"""
Есть фрагмент текста, состоящий из предложений.
Предложение - это строка, которая начинается с
большой буквы и заканчивается точкой, вопросительным или
восклицательным знаком (или несколькими такими знаками).
Предложение может состоять из одного слова. Слова состоят только из букв.
Внутри предложения могут быть запятые.
Составить предложение из первых слов предложений фрагмента.
Только первое слово итогового предложения должно быть с
большой буквы, остальные с маленькой.

Предложение должно заканчиваться точкой.

def generate_sentence(text: str) -> str:
    pass

""Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
""
->
"Happy wish please goodbye."
"""

text = """Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""

import re

result = re.findall(r"(?:^|(?:[.!?]\s))(\w+\.?)", text)
print(' '.join(result).capitalize())
