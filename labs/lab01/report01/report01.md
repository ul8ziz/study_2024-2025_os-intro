---
# Front matter
lang: ru-RU
title: "Лабораторная работа №1"
subtitle: "Дисциплина: Математические основы защиты информации и информационной безопасности"
author: "Алгайли Абдулазиз Мохаммед"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # Список рисунков
lot: true # Список таблиц
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Познакомиться с шифрами Цезаря и Атбаш.

# Задание

1. Реализовать шифр Цезаря с произвольным ключом k.
2. Реализовать шифр Атбаш.

# Выполнение лабораторной работы

1) Сначала я реализовал шифр Цезаря на языке Python. Я использовал переменную k в качестве сдвига. При проверке слова берётся конкретный символ (char). Далее при помощи match-case я реализовал проверки на наличие выбранного символа в русском или английском алфавите. При этом я учёл регистр символа. Если символ находится в алфавите, то берётся его код ASCII, из которого вычитается код ASCII первой буквы алфавита. Затем прибавляется сдвиг k и берётся остаток от количества символов в алфавите (русский - 32, английский 26). После чего мы определяем, какая по счёту буква в алфавите, и прибавляем код ASCII первой буквы алфавита. Затем вписываем каждый символ в result и возвращаем его.

![Шифр Цезаря на языке Python](image01/image_01.png){ width=70% }

2) Далее я реализовал запрос текста у пользователя и вывод результата алгоритма шифра Цезаря.

![Запрос текста и вывод результата шифра Цезаря](image01/image_02.png){ width=70% }

3) После я вызвал написанный метод через командную строку и проверил все русские и английские буквы.

![Проверка метода шифра Цезаря](image01/image_03.png){ width=70% }

4) Затем я реализовал шифр Атбаша. При проверке слова берётся конкретный символ (char). match-case я реализовал проверки на наличие выбранного символа в русском или английском алфавите. При этом я учёл регистр символа. Если символ находится в алфавите, то берётся код ASCII последней буквы алфавита, из которого вычитается код ASCII выбранного символа. С помощью этого мы определяем, какое значение имеет симметричный центру символ алфавита. Затем мы прибавляем код ASCII первой буквы алфавита, чтобы определить нужный нам символ. Затем вписываем каждый символ в result и возвращаем его.

![Шифр Атбаш на языке Python](image01/image_04.png){ width=70% }

5) Далее я реализовал вывод результата алгоритма шифра Атбаш после вывода результата алгоритма шифра Цезаря.

![Вывод результата шифра Атбаш](image01/image_05.png){ width=70% }

6) После я вызвал написанный метод через командную строку и проверил все русские и английские буквы.

![Проверка метода шифра Атбаш](image01/image_06.png){ width=70% }

7) Итоговый код можно увидеть на картинке ниже.

![Итоговый код](image01/image_07.png){ width=70% }

# Выводы

Я реализовал шифр Цезаря с произвольным ключом k и реализовал шифр Атбаш.
