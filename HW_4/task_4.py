"""
Пользователь вводит адрес элемктронной почты.
Вывести True, если строка является валидным адресом, иначе False.

Валидным адресом считаем, строку

- в которой встречается один раз '@' и один раз '.'

- '@' идет до '.'

- строка не начинается с '@' и не заканчивается '.'

В комментариях к коду должны быть указаны строки,
которыми протестировали код

Регулярные выражения не использовать.

email = "aaa@bbb.ccc"  # True
"""

email = input("Enter email: ")

if email.count('@') == 1 and email.count('.') == 1:
    if not email.startswith('@') and not email.endswith('.'):
        if email.find('@') < email.find('.'):
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)

# testdata
# qwerty@ewqw.tewu  -> True
# @hidisd.sokdo -> False
# hudu.sdijsdi@ -> False
# jdii@mdmdo@jdoke.ksk -> False
# hsuhd.jsij@jdojd.kok -> False
# skjd@jkdk. -> False
# jcj.jodj@dkpk -> False


