from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from Model import Keyword, Step, Module, Lesson, StepKeyword
from config import Settings

settings = Settings()


engine = create_engine(settings.DATABASE_URL_asyncpg)

Session = sessionmaker(bind=engine)
session = Session()

def list_modules():
    modules = session.scalars(select(Module)).all()
    for module in modules:
        print(module)

def list_lessons():
    lessons = session.scalars(select(Lesson)).all()
    for lesson in lessons:
        print(lesson)

def list_steps():
    steps = session.scalars(select(Step)).all()
    for step in steps:
        print(step)

def list_keywords():
    keywords = session.scalars(select(Keyword)).all()
    for keyword in keywords:
        print(keyword)

def main():
    while True:
        print("\nМеню:")
        print("1. Список модулей")
        print("2. Список уроков")
        print("3. Список шагов")
        print("4. Список ключевых слов")
        print("5. Выход")
        choice = input("Выберите опцию: ")

        if choice == "1":
            list_modules()
        elif choice == "2":
            list_lessons()
        elif choice == "3":
            list_steps()
        elif choice == "4":
            list_keywords()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    session.close()

if __name__ == "__main__":
    main()
