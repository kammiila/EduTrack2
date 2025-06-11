from collections import defaultdict
from datetime import date

GROUPS_DATA = [
    {"id": "cs-11-24", "name": "CS-11-24"},
    {"id": "cs-12-24", "name": "CS-12-24"},
    {"id": "cs-13-24", "name": "CS-13-24"},
    {"id": "cs-14-24", "name": "CS-14-24"},
    {"id": "cs-15-24", "name": "CS-15-24"},
    {"id": "cs-16-24", "name": "CS-16-24"}
]

STUDENTS_DATA = {
    "cs-11-24": [
        {"id": 1, "name": "Ашимова Асема", "present": False},
        {"id": 2, "name": "Жапаров Дамир", "present": False},
        {"id": 3, "name": "Кумарбекова Сауле", "present": False},
        {"id": 4, "name": "Камбарбеков Алихан", "present": False},
        {"id": 5, "name": "Камыталиев Даниел", "present": False},
        {"id": 6, "name": "Кыязбеков Мирсултан", "present": False},
        {"id": 7, "name": "Маманов Мухаммед", "present": False},
        {"id": 8, "name": "Нурбеков Айдар", "present": False},
        {"id": 9, "name": "Сатыбалдиев Нурхан", "present": False},
        {"id": 10, "name": "Таирбеков Амир", "present": False},
        {"id": 11, "name": "Шамаев Даниель", "present": False}
    ],
    "cs-12-24": [
        {"id": 1, "name": "Абдикаримов Тимур", "present": False},
        {"id": 2, "name": "Абдраимов Иброхим", "present": False},
        {"id": 3, "name": "Баекеева Камила", "present": False},
        {"id": 4, "name": "Казыбеков Санжар", "present": False},
        {"id": 5, "name": "Кайратов Султанбек", "present": False},
        {"id": 6, "name": "Кашымбеков Актан", "present": False},
        {"id": 7, "name": "Кенжебекова Жибек", "present": False},
        {"id": 8, "name": "Кумушбеков Анвар", "present": False},
        {"id": 9, "name": "Курбатов Максим", "present": False},
        {"id": 10, "name": "Мидинов Илияр", "present": False},
        {"id": 11, "name": "Нурбаев Мырзабек", "present": False},
        {"id": 12, "name": "Сатымкулов Адилхан", "present": False},
        {"id": 13, "name": "Султангазиева Раида", "present": False}
    ],
    "cs-13-24": [
        {"id": 1, "name": "Абдиев Мухаммед", "present": False},
        {"id": 2, "name": "Анаркулов Омурбек", "present": False},
        {"id": 3, "name": "Атамкулов Атай", "present": False},
        {"id": 4, "name": "Аширбекова Адеми", "present": False},
        {"id": 5, "name": "Вудуньян Ринат", "present": False},
        {"id": 6, "name": "Жуматаев Султан", "present": False},
        {"id": 7, "name": "Болотоева Камила", "present": False},
        {"id": 8, "name": "Ибраимова Аяна", "present": False},
        {"id": 9, "name": "Искаков Бекзат", "present": False},
        {"id": 10, "name": "Коңурбаев Барсбек", "present": False},
        {"id": 11, "name": "Маданзи Абдуль-Алим", "present": False},
        {"id": 12, "name": "Мунуров Нурсултан", "present": False},
        {"id": 13, "name": "Айе Мажид", "present": False},
        {"id": 14, "name": "Сактанов Байэл", "present": False},
        {"id": 15, "name": "Токтобеков Кутман", "present": False},
        {"id": 16, "name": "Тыныстанов Санжар", "present": False},
        {"id": 17, "name": "Халилов Нурсейит", "present": False},
        {"id": 18, "name": "Шамилов Бекмырза", "present": False},
        {"id": 19, "name": "Эшанкулов Муса", "present": False}
    ],
    "cs-14-24": [
        {"id": 1, "name": "Асанов Элмырза", "present": False},
        {"id": 2, "name": "Байызбекова Перизат", "present": False},
        {"id": 3, "name": "Баргыбаев Нуртилек", "present": False},
        {"id": 4, "name": "Бердибекова Нурбийке", "present": False},
        {"id": 5, "name": "Жумакадыров Байэл", "present": False},
        {"id": 6, "name": "Искаков Куттуубай", "present": False},
        {"id": 7, "name": "Махмудов Ислам", "present": False},
        {"id": 8, "name": "Мырзабекова Айжамал", "present": False},
        {"id": 9, "name": "Райымбердиев Исхак", "present": False},
        {"id": 10, "name": "Сактанова Милана", "present": False},
        {"id": 11, "name": "Суйуналиев Баэл", "present": False},
        {"id": 12, "name": "Эркинбеков Айман", "present": False},
    ],
    "cs-15-24": [
        {"id": 1, "name": "Абдилазизов Алихан", "present": False},
        {"id": 2, "name": "Абдуллаева Айгүл", "present": False},
        {"id": 3, "name": "Алтынбекова Айзат", "present": False},
        {"id": 4, "name": "Байдадаев Нурсултан", "present": False},
        {"id": 5, "name": "Жумабеков Чынгыз", "present": False},
        {"id": 6, "name": "Гульчороева Асема", "present": False},
        {"id": 7, "name": "Кабылбеков Айжигит", "present": False},
        {"id": 8, "name": "Козубаев Абдуазим", "present": False},
        {"id": 9, "name": "Сапаралиев Элдар", "present": False},
        {"id": 10, "name": "Сатмурзаев Эмирбек", "present": False},
        {"id": 11, "name": "Султанов Эрзат", "present": False},
        {"id": 12, "name": "Сүйүнбеков Нурбол", "present": False},
        {"id": 13, "name": "Талипов Тилек", "present": False},
        {"id": 14, "name": "Турсунбеков Аскар", "present": False},
        {"id": 15, "name": "Эмилбеков Айбек", "present": False}
    ],
    "cs-16-24": [
        {"id": 1, "name": "Адылов Арсен", "present": False},
        {"id": 2, "name": "Азаматов Али", "present": False},
        {"id": 3, "name": "Акаев Байжигит", "present": False},
        {"id": 4, "name": "Акматов Элдар", "present": False},
        {"id": 5, "name": "Ашимканов Али", "present": False},
        {"id": 6, "name": "Базарбаев Юнус", "present": False},
        {"id": 7, "name": "Джумабеков Азирет", "present": False},
        {"id": 8, "name": "Ибрагимова Райена", "present": False},
        {"id": 9, "name": "Каракашев Айдар", "present": False},
        {"id": 10, "name": "Ногойбаев Нурсултан", "present": False},
        {"id": 11, "name": "Омуракунова Айлин", "present": False},
        {"id": 12, "name": "Омургазиев Нурсултан", "present": False},
        {"id": 13, "name": "Осмонов Медер", "present": False},
        {"id": 14, "name": "Тариэлев Алихан", "present": False},
        {"id": 15, "name": "Тоголокова Айназик", "present": False}
    ],
    

    "se-21-23": [],
    "ds-10-23": [],
    "it-01-22": [],
    "ml-22-24": []
}
# data.py

# Хранилище посещаемости: { group_id: { date_string: set(student_ids) } }
ATTENDANCE_DB = defaultdict(lambda: defaultdict(set))


# 📌 Сохраняем посещаемость
def save_attendance(group_id, date_str, present_student_ids):
    ATTENDANCE_DB[group_id][date_str] = set(present_student_ids)


# 📌 Получаем студентов с пометкой present на дату
def get_students_with_attendance(group_id, date_str):
    students = STUDENTS_DATA.get(group_id, [])
    present_ids = ATTENDANCE_DB[group_id].get(date_str, set())

    return [
        {
            "id": student["id"],
            "name": student["name"],
            "present": student["id"] in present_ids
        }
        for student in students
    ]


# 📌 Получить статистику по группе
def get_attendance_summary(group_id, date_str):
    students = STUDENTS_DATA.get(group_id, [])
    total = len(students)

    present_today = len(ATTENDANCE_DB[group_id].get(date_str, set()))
    absent_today = total - present_today

    all_dates = ATTENDANCE_DB[group_id]
    total_present = sum(len(present_ids) for present_ids in all_dates.values())
    total_possible = total * len(all_dates)

    total_absent = total_possible - total_present

    rate = round((total_present / total_possible) * 100, 1) if total_possible else 0.0

    return {
        "total": total,
        "present_today": present_today,
        "absent_today": absent_today,
        "total_present": total_present,
        "total_absent": total_absent,
        "attendance_rate": rate
    }
