# UsingModulePandas

Лабораторна робота No2
Використання модуля Pandas.
Аналіз даних по серцево-судинних захворюваннях
Мета роботи: набути практичних навичок роботи з модулем Pandas та
провести первинний аналіз даних.
Зміст роботи
Завдання 1. Ретельно опрацювати теоретичні відомості:
https://khashtamov.com/ru/pandas-introduction/
http://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/jupyter_russian/top
ic01_pandas_data_analysis/topic1_habr_pandas.ipynb
http://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/jupyter_russian/top
ic01_pandas_data_analysis/%5Bsolution%5D_lesson1_practice_pandas_titanic.ipynb
https://www.kaggle.com/crawford/python-groupby-tutorial
Завдання 2. Провести аналіз даних за допомогою Pandas
Опис даних.
Вхідні дані знаходяться у csv-файлі за посиланням:
http://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/data/mlbootcamp5
_train.csv
Dataset сформований з реальних даних, і в ньому використовуються
ознаки, які можна розбити на 3 групи:
Об’єктивні ознаки:

Вік (age)

Зріст (height)

Вага (weight)

Пол (gender)
Результати вимірювання:

Артеріальний тиск верхній і нижній (ap_hi, ap_lo)

Холестерин (cholesterol)

Глюкоза (gluc)
Суб'єктивні ознаки (зі слів пацієнта):

Куріння (smoke)

Вживання алкоголю (alco)

Фізична активність (active)
Цільова ознака (яку цікаво буде прогнозувати): Наявність серцево-
судинних захворювань за результатами класичного лікарського огляду
(cardio).Значення показників холестерину і глюкози представлені одним з трьох
класів: норма, вище норми, значно вище норми. Значення суб'єктивних ознак
- бінарні.
Всі показники отримані на момент огляду.
Необхідно провести первинний аналіз даних навчальної вибірки за
допомогою Pandas.
З бібліотек знадобляться тільки NumPy і Pandas.
import numpy as np
import pandas as pd
Зчитаємо дані з csv-файлу в об'єкт pandas DataFrame.
df = pd.read_csv('mlbootcamp5_train.csv', sep=';',index_col='id')
Подивимося на перші 5 записів ( df.head() ).

Кожну відповідь необхідно проілюструвати фрагментами програмного
коду, що відповідають на наступні питання...
