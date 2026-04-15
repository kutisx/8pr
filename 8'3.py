# 8.3
students = { "РОберт:0": {"русский", "немецкий"}, "Зайцев": {"китайский", "английский"}, "Кутищева": {"французский", "английский"}, "Козлов": {"испанский"}, "Смирнова": {"китайский", "японский"} }
all_languages = set()
for langs in students.values():
    for lang in langs:
        all_languages.add(lang)
print("Все языки:", sorted(all_languages))
chinese_students = []
for name, langs in students.items():
    if "китайский" in langs:
        chinese_students.append(name)
print("Студенты, знающие китайский:", chinese_students)