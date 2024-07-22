# Курс на платформе Stepik состоит из нескольких модулей, каждый модуль включает несколько уроков,
# для каждого урока хранится информация о его положении в модуле. Каждый урок состоит из последовательности шагов.
# Каждый шаг имеет свой тип (это может быть текст, задание на SQL и пр.)
# и также порядковый номер в уроке.

# Шаги:
# 1. Подключить базу данные Postgres, развернуть базу, создать окружение, создать движок (sqlalchelmy, asyncpg,  и т.д.;
# 2. Создать модельки алхимии, продумать какие должны быть связи между таблицами;
# 3. Написать код для наполнения базы;
# 4. Написать запросы на получение данных с использование relationship.

from sqlalchemy import engine
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Keyword, Step, StepKeyword, Module, Lesson


engine = engine(config.Settings.DATABASE_URL_asyncpg) #подключение БД через путь
Base.metadata.create_all(engine)

# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)

# Создание фабрики сессий
Session = sessionmaker(bind=engine)
session = Session()

# Добавление начальных данных
# Добавляем ключевые слова
keyword1 = Keyword(keyword_name="Python")
keyword2 = Keyword(keyword_name="SQLAlchemy")

# Добавляем модули
module1 = Module(module_name="Основы Python")
module2 = Module(module_name="Продвинутый Python")

# Добавляем уроки
lesson1 = Lesson(lesson_name="Введение в Python", lesson_position="1", module=module1)
lesson2 = Lesson(lesson_name="ООП в Python", lesson_position="2", module=module1)
lesson3 = Lesson(lesson_name="Модели в SQLAlchemy", lesson_position="1", module=module2)

# Добавляем шаги
step1 = Step(step_name="Установка Python", lesson=lesson1)
step2 = Step(step_name="Первая программа", lesson=lesson1)
step3 = Step(step_name="Создание класса", lesson=lesson2)
step4 = Step(step_name="Использование моделей", lesson=lesson3)

# Добавляем ключевые слова к шагам
step_keyword1 = StepKeyword(step=step1, keyword=keyword1)
step_keyword2 = StepKeyword(step=step2, keyword=keyword1)
step_keyword3 = StepKeyword(step=step3, keyword=keyword1)
step_keyword4 = StepKeyword(step=step4, keyword=keyword2)

# Добавляем все объекты в сессию
session.add_all([
    keyword1, keyword2,
    module1, module2,
    lesson1, lesson2, lesson3,
    step1, step2, step3, step4,
    step_keyword1, step_keyword2, step_keyword3, step_keyword4
])

# Фиксируем изменения (сохраняем в базе данных)
session.commit()

# Закрываем сессию
session.close()

print("База данных успешно создана и заполнена начальными данными.")