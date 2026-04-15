# 8.1
capitals = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим", "Япония": "Токио" }
# a
print("Все страны и их столицы:")
for country, capital in capitals.items():
    print(country, "-", capital)
# b
country_name = input("\nВведите название страны: ")
if country_name in capitals:
    print("Столица:", capitals[country_name])
else:
    print("Страна не найдена")
# c
print("\nСтраны в алфавитном порядке:")
for country in sorted(capitals.keys()):
    print(country, "-", capitals[country])