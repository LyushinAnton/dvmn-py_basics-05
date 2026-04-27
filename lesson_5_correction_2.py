import os
import file_operations
from faker import Faker
from collections import OrderedDict
from random import randint, sample


SKILLS = [
        "Стремительный прыжок",
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд"
    ]


LETTERS_MAPPING = OrderedDict([
        ('а', 'а͠'),
        ('б', 'б̋'),
        ('в', 'в͒͠'),
        ('г', 'г͒͠'),
        ('д', 'д̋'),
        ('е', 'е͠'),
        ('ё', 'ё͒͠'),
        ('ж', 'ж͒'),
        ('з', 'з̋̋͠'),
        ('и', 'и'),
        ('й', 'й͒͠'),
        ('к', 'к̋̋'),
        ('л', 'л̋͠'),
        ('м', 'м͒͠'),
        ('н', 'н͒'),
        ('о', 'о̋'),
        ('п', 'п̋͠'),
        ('р', 'р̋͠'),
        ('с', 'с͒'),
        ('т', 'т͒'),
        ('у', 'у͒͠'),
        ('ф', 'ф̋̋͠'),
        ('х', 'х͒͠'),
        ('ц', 'ц̋'),
        ('ч', 'ч̋͠'),
        ('ш', 'ш͒͠'),
        ('щ', 'щ̋'),
        ('ъ', 'ъ̋͠'),
        ('ы', 'ы̋͠'),
        ('ь', 'ь̋'),
        ('э', 'э͒͠͠'),
        ('ю', 'ю̋͠'),
        ('я', 'я̋'),
        ('А', 'А͠'),
        ('Б', 'Б̋'),
        ('В', 'В͒͠'),
        ('Г', 'Г͒͠'),
        ('Д', 'Д̋'),
        ('Е', 'Е'),
        ('Ё', 'Ё͒͠'),
        ('Ж', 'Ж͒'),
        ('З', 'З̋̋͠'),
        ('И', 'И'),
        ('Й', 'Й͒͠'),
        ('К', 'К̋̋'),
        ('Л', 'Л̋͠'),
        ('М', 'М͒͠'),
        ('Н', 'Н͒'),
        ('О', 'О̋'),
        ('П', 'П̋͠'),
        ('Р', 'Р̋͠'),
        ('С', 'С͒'),
        ('Т', 'Т͒'),
        ('У', 'У͒͠'),
        ('Ф', 'Ф̋̋͠'),
        ('Х', 'Х͒͠'),
        ('Ц', 'Ц̋'),
        ('Ч', 'Ч̋͠'),
        ('Ш', 'Ш͒͠'),
        ('Щ', 'Щ̋'),
        ('Ъ', 'Ъ̋͠'),
        ('Ы', 'Ы̋͠'),
        ('Ь', 'Ь̋'),
        ('Э', 'Э͒͠͠'),
        ('Ю', 'Ю̋͠'),
        ('Я', 'Я̋'),
        (' ', ' ')
    ])


def create_results_folder():
    existing_file_path = "lesson_5_correction_2.py"
    parent_directory = os.path.dirname(os.path.abspath(existing_file_path))
    new_folder_path = os.path.join(parent_directory, "Results")
    os.makedirs(new_folder_path, exist_ok=True)


def multiple_replace(target_str, LETTERS_MAPPING):
    for i, j in LETTERS_MAPPING.items():
        target_str = target_str.replace(i, j)
    return target_str


def main():

    create_results_folder()

    for i in range(0, 10):

        skill = sample(SKILLS, 3)

        skill_1 = skill[0]
        skill_2 = skill[1]
        skill_3 = skill[2]

        fake = Faker("ru_RU")

        skill_1 = multiple_replace(skill_1, LETTERS_MAPPING)
        skill_2 = multiple_replace(skill_2, LETTERS_MAPPING)
        skill_3 = multiple_replace(skill_3, LETTERS_MAPPING)

        content = {
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": (randint(3, 18)),
            "agility": (randint(3, 18)),
            "endurance": (randint(3, 18)),
            "intelligence": (randint(3, 18)),
            "luck": (randint(3, 18)),
            "skill_1": (skill_1),
            "skill_2": (skill_2),
            "skill_3": (skill_3),
        }

        file_operations.render_template(
            "charsheet.svg",
            f"Results/result{i}.svg",
            content
        )


if __name__ == '__main__':
    main()
