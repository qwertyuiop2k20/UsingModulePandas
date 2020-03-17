# Лаба 2. Використання модуля Pandas.
# Аналіз даних по серцево-судинних захворюваннях

# in Linux Debian/Ubuntu to install:
# sudo apt install python3-tk python3 python3-pip
# sudo pip3 install pandas seaborn matplotlib numpy statsmodels

import numpy as np
import pandas as pd

# Завдання 1. Ретельно опрацювати теоретичні відомості: 
# https://khashtamov.com/ru/pandas-introduction/ 
# http://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/jupyter_russian/topic0 1_pandas_data_analysis/topic1_habr_pandas.ipynb

# Завдання 2. Провести аналіз даних за допомогою Pandas

# Зчитуємо дані з csv-файлу в об'єкт pandas DataFrame
df = pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id');
# та дивимося на перші 5 записів
print(df.head()); # метод head по замовчуванню (без параметрів)
		  # виводить перших 5 записів
print();

# Питання 1. Скільки чоловіків і жінок представлено в цьому наборі даних?
# Відповідно до зросту, в ознаці «стать» 1 відповідає жінкам, а 2 – чоловікам.
# Запускаємо код:

print(df[df.gender == 1]['gender'].count());
print(df[df.gender == 2]['gender'].count());
# print();

# Отримуємо 45530 жінок і 24470 чоловіків

# Питання 2. Хто в середньому рідше вказує, що вживає алкоголь - чоловіки чи жінки?

df_g1 = df[df['gender'] == 1];
print(len(df_g1), df_g1['height'].mean());
df_g2 = df[df['gender'] == 2];
print(len(df_g2), df_g2['height'].mean());
print();
#
df.groupby('gender')['alco'].mean();
len(df_g1[df_g1['alco'] == 1]) / len(df_g1);
len(df_g2[df_g2['alco'] == 1]) / len(df_g2);
print(df_g1['alco'].describe());
print(df_g2['alco'].describe());
print();

# Жінок, які вказали, що вживають алкоголь 1161, натомість чоловіків – 2603.
# У відсотковому відношенні від загальної кількості виходить, що приблизно
# 2,5% жінок вказали, що вживають алкоголь, тоді як таких чоловіків 10,63%.
# Тому в середньому жінки рідше вказують, що вживають алкоголь.

# Питання 3. У скільки разів (округлити, round) відсоток
# курців серед чоловіків більше, ніж відсоток курців
# серед жінок (принаймні, за цими анкетними даними)?

df.groupby('gender')['smoke'].mean();
df[df['gender'] == 2]['smoke'].mean() / df[df['gender'] == 1]['smoke'].mean();
count_man_smoke = len(df[(df['gender'] == 2) & (df['smoke'] == 1)]);
man_smoke_percentile = (count_man_smoke * 100.0) / len(df[df['gender'] == 2]);
print(man_smoke_percentile);
count_woman_smoke = len(df[(df['gender'] == 1) & (df['smoke'] == 1)]);
woman_smoke_percentile = (count_woman_smoke * 100.0) / len(df[df['gender'] == 1]);
print(woman_smoke_percentile);
print(round(man_smoke_percentile / woman_smoke_percentile));
print();

# Відповідь: в 12 разів.

# Питання 4. Здогадайтеся, в чому тут вимірюється вік,
# і дайте відповідь, на скільки місяців (приблизно)
# відрізняються медіанне значення віку курців і тих хто не курить.

# Вік вимірюється в днях.

df.groupby('smoke')['age'].median() / 365.25;
print((df[df['smoke'] == 0]['age'].median() - df[df['smoke'] == 1]['age'].median()) / 365.25 * 12);
print();

# Різниця між медіанним значенням віку курців і тих,
# хто не курить складає приблизно 20 місяців.

# Питання 5. У статті на Вікіпедії про серцево-судинний ризик показана
# шкала SCORE для розрахунку ризику смерті від серцево-судинного
# захворювання в найближчі 10 років. Порахувати аналогічне значення на
# наших даних.
# У скільки разів (round) відрізняються частки хворих людей (відповідно
# до цільової ознаки, cardio) в цих двох підвибірках?

df['age_years'] = (df['age'] / 365.25).round().astype('int');
df['age_years'].describe(); df['age_years'].max();
smoking_old_men = df[(df['gender'] == 2) & (df['age_years'] >= 60) &
(df['age_years'] < 65) & (df['smoke'] == 1)];
print(smoking_old_men[(smoking_old_men['cholesterol'] == 1) &
(smoking_old_men['ap_hi'] < 120)]['cardio'].mean());
print(smoking_old_men[(smoking_old_men['cholesterol'] == 3) &
(smoking_old_men['ap_hi'] >= 160) & (smoking_old_men['ap_hi'] < 180)]
['cardio'].mean());
print();

# Відповідь: частки хворих людей (відповідно до цільової ознаки, cardio)
# в цих двох підвибірках відрізняються приблизно в 3 рази.

# Питання 6. Побудуйте нову ознаку - BMI (Body Mass Index). Для цього
# треба вагу у кілограмах поділити на квадрат зросту в метрах.
# Нормальними вважаються значення BMI від 18.5 до 25.

df['BMI'] = df['weight'] / (df['height'] / 100) ** 2;
# df['bmi'] = df.apply(lambda row: row['weight'] / np.square(row['height'] / 100.0), axis = 1);
print(df['BMI'].median());
print(df.groupby('gender')['BMI'].mean());
print(df.groupby('cardio')['BMI'].mean());
print(df.groupby(['gender', 'alco', 'cardio'])['BMI'].mean());
df_healthy = df[(df['cardio'] == 0) & (df['alco'] == 0)];
print(df_healthy.groupby('gender')['BMI'].mean());
print();

# Відповідь:
# 1) Перше твердження вірне, медіанний BMI по вибірці перевищує
#    норму в 25 одиниць.
# 2) Друге твердження не вірне, у жінок в середньому BMI вище, ніж у чоловіків.
# 3) Третє твердження не вірне. У здорових в середньому BMI нижче, ніж у хворих.
# 4) Четверте твердження вірне. У сегменті здорових і тих що не вживають
#    алкоголь чоловіків в середньому BMI ближче до норми, ніж в сегменті
#    здорових і тих що не вживають алкоголь жінок.

# Питання 7.
# Відфільтруйте наступні сегменти пацієнтів (вважаємо це помилками в даних):
#     - вказане нижнє значення артеріального тиску строго вище верхнього;
#     - зріст строго менше 2.5% - перцентілі або строго більше
#       97.5% - перцентілі (використовуйте pd.Series.quantile,
#       якщо не знаєте, що це таке - прочитайте)
#     - вага строго менше 2.5% - перцентілі або строго більше
#       97.5% - перцентілі

filtered_df = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >=
df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
& (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <=
df['weight'].quantile(0.975))];
print(filtered_df.shape[0] / df.shape[0]);
filtered_ap = df[df['ap_lo'] > df['ap_hi']];
filtered_qu_25 = df['height'].quantile(.025);
filtered_qu_975 = df['height'].quantile(.975);
print(filtered_qu_25, filtered_qu_975);
filtered_qu = df[(df['height'] < filtered_qu_25) | (df['height'] >
filtered_qu_975)];
filtered_w_25 = df['weight'].quantile(.025);
filtered_w_975 = df['weight'].quantile(.975);
print(filtered_w_25, filtered_w_975);
filtered_w = df[(df['weight'] < filtered_w_25) | (df['weight'] >
filtered_w_975)];
print(round((len(filtered_ap) + len(filtered_qu) + len(filtered_w)) *
100 / len(df)));
print();

# В результаті викинули 10% даних.
