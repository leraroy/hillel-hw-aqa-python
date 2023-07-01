"""
Написать скрипт, который преобразовывает xml файл в json файл.

Файлы находятся здесь:

https://github.com/AlexLitvino/hl_pyauto_27mar23/tree/main/L25/HW

Исходный xml файл содержит узлы страниц и элементов, атрибутами
указаны имена страниц, элементов и типы локаторов элементов.
Текст элемента указывает значение локатора.

json файл должен хранить словарь-страниц, страница должна
быть словарем элементов, ключи словаря элемента соответствуют
платформе, а значения - список из типа локатора и значения локатора.
"""

import json
import xml.etree.ElementTree as ET

tree = ET.parse('pages.xml')
root = tree.getroot()
res_dict = {}

for page in root:
    element_dict = {}
    for element in page:
        locator_dict = {}
        for locator in element:
            locator_dict[locator.attrib["platform"]] = [locator.attrib["locator_type"], locator.text]
        element_dict[element.attrib["name"]] = locator_dict
    res_dict[page.attrib["name"]] = element_dict

with open("pages.json", 'w') as f:
    json.dump(res_dict, f, indent=4)
