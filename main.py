import os
import numpy as np
from nop import NOP
from collections import Counter
import json
import matplotlib.pyplot as plt
from textwrap import wrap

with open('160221.json', encoding="utf8") as f:
    data = json.load(f)

nop_list = []

# wczytanie obiketów klasy NOP do listy nop_list
for nop in data:
    nop_list.append(NOP(nop['ID'], nop['DATE'], nop['VOIVODESHIP'], nop['REGION'], nop['GENDER'], nop['DESCRIPTION']))

# punkt nr 2
number_of_women = 0
number_of_men = 0
for nop in nop_list:
    number_of_women += nop.gender.count('K')
    number_of_men += nop.gender.count('M')

with open('odpowiedzi.txt', "w", encoding="utf8") as file:
    file.write("Ilość NOPów: " + str(len(nop_list)) + "\n")
    file.write("Ilość kobiet: " + str(number_of_women) + "\n")
    file.write("Ilość mężczyzn: " + str(number_of_men) + "\n")

# punkt nr 3
count_fever = 0
for nop in nop_list:
    if str(nop.voivodeship) == 'pomorskie' and str(nop.symptoms) == 'Gorączka':
        count_fever += 1
        #print(nop.id)

with open('odpowiedzi.txt', "a", encoding="utf8") as file:
    file.write("Liczba osób z gorączką w woj. pomorskim: " + str(count_fever))



# punkt nr 4
voivodeship = set()
for nop in nop_list:
    voivodeship.add(nop.voivodeship)

if not os.path.exists('zestawienie.txt'):
    for v in voivodeship:
        count = 0
        for nop in nop_list:
            if v == nop.voivodeship:
                count += 1
        with open('zestawienie.txt', "a+", encoding="utf8") as file:
            file.write(v + ": " + str(count) + "\n")

# punkt nr 5
# nr indeksu xxx08, dwie ostatnie cyfry indexu to 08, tak więc 8 % 16 = 8, a ósmym województwem na liście jest podkarpackie ;-)
sympotms_in_podkarpackie = []
for nop in nop_list:
    if nop.voivodeship == 'podkarpackie':
        sympotms_in_podkarpackie.append(str(nop.symptoms))

count = Counter(sympotms_in_podkarpackie)
if not os.path.exists('podkarpackie.txt'):
    with open('podkarpackie.txt', "a+", encoding="utf8") as file:
        file.write('Statystyka ilościowa dla objawów w woj. podkarpackim: \n')
        for char in count:
            file.write('%s : %d' % (char, count[char]) + '\n')

# punkt nr 6
number_of_women = 0
number_of_men = 0
for nop in nop_list:
    number_of_women += nop.gender.count('K')
    number_of_men += nop.gender.count('M')
values = [number_of_men, number_of_women]
labels = ['mężczyźni', 'kobiety']
explode = [0.2, 0.2]
plt.title('Procent mężczyzn i kobiet, którzy doświadczyli NOP')
plt.pie(values, labels=labels, explode=explode, autopct='%.2f')
plt.savefig('wykres_zadanie_6.png')
plt.show()

# punkt nr 7
symptoms = ("Zaczerwienienie i bolesność", "Gorączka", "Drgawki", "Wymioty", "Omdlenie", "Pozostałe")
values = []
x = 0
for sym in symptoms:
    for nop in nop_list:
        if str(sym) == str(nop.symptoms):
            x += 1
    values.append(x)
    x = 0

lab = symptoms
lab = ['\n'.join(wrap(x, 10)) for x in lab]
val = values
plt.bar(lab, val, color='black')
plt.title('Liczba poszczególnych objawów')
plt.xlabel('Objawy')
plt.ylabel('Ilość')
plt.savefig('wykres_zadanie_7.png')
plt.show()

# punkt nr 8
dataK = []
dataM = []
for nop in nop_list:
    if nop.gender == 'K':
        dataK.append(nop.date)
    elif nop.gender == 'M':
        dataM.append(nop.date)

x_labels = list(Counter(dataK).keys())
osX = []
for label in x_labels:
    osX.append(label)

tick = np.linspace(0, 43, 43)
plt.figure(figsize=(13, 10))
plt.xticks(tick, labels=osX, rotation=90)
plt.plot(Counter(dataK).keys(), Counter(dataK).values())
plt.plot(Counter(dataM).keys(), Counter(dataM).values())
plt.title('Zmiana ilości NOPów w czasie', fontdict={'fontname': 'monospace', 'fontsize': 18})
plt.xlabel('Daty')
plt.ylabel('Ilość NOPów')
plt.legend(('Kobiety', 'Mężczyźni'))
plt.savefig('wykres_zadanie_8.png')
plt.show()
