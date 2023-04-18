"""
В программе есть списки тестировщиков (имена, айдишники), которые:
- могут писать тест дизайны
- могут писать тест скрипты
- могут ревьюить скрипты
- сегодня не на работе

Любой тестировщик может входить в одну или несколько групп.
Создать списки:
- всех тестировщиков в команде
- тестировщиков, которые могут только писать скрипты
- тестировщиков, которые сегодня на работе
- тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе

Полученные списки вывести в отсортиованном виде.
test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

всех тестировщиков в команде
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

могут писать только тест скрипты
[4, 6, 7, 8]

тестировщиков, которые сегодня на работе
[3, 4, 7, 8, 9, 10]

тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе
[3]
"""

test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_tester = set(test_design_writers).union(scripters).union(reviewers).union(out_of_office_today)
only_write_scripts = set(scripters).difference(test_design_writers).difference(reviewers)
in_the_office_today = set(all_tester).difference(out_of_office_today)
scripters_reviewers_in_office = set(scripters).intersection(reviewers).intersection(in_the_office_today)
print(f"всех тестировщиков в команде\n{list(all_tester)}")
print(f"могут писать только тест скрипты\n{list(only_write_scripts)}")
print(f"тестировщиков, которые сегодня на работе\n{list(in_the_office_today)}")
print(f"тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе\n{list(scripters_reviewers_in_office)}")







