import matplotlib.pyplot as plt

# Генерируем данные для графика
years = [2018, 2019, 2020, 2021, 2022]
values = [100, 200, 150, 300, 250]

# Построение графика
plt.plot(years, values, marker='o', linestyle='-', color='b')
plt.title("Рост показателей по годам")
plt.xlabel("Годы")
plt.ylabel("Показатели")
plt.grid(True)
plt.show()
