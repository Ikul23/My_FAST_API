import asyncio
from sqlalchemy import select
from db import AsyncSessionLocal
from models import Keyword, Step, Module, Lesson

async def list_modules():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Module))
        modules = result.scalars().all()
        for module in modules:
            print(module)

async def list_lessons():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Lesson))
        lessons = result.scalars().all()
        for lesson in lessons:
            print(lesson)

async def list_steps():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Step))
        steps = result.scalars().all()
        for step in steps:
            print(step)

async def list_keywords():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Keyword))
        keywords = result.scalars().all()
        for keyword in keywords:
            print(keyword)

async def main():
    while True:
        print("\nМеню:")
        print("1. Название таблицы: Список модулей")
        print("2. Название таблицы: Список уроков")
        print("3. Название таблицы: Список шагов")
        print("4. Название таблицы: Список ключевых слов")
        print("5. Выход")
        choice = input("Выберите опцию: ")

        if choice == "1":
            await list_modules()
        elif choice == "2":
            await list_lessons()
        elif choice == "3":
            await list_steps()
        elif choice == "4":
            await list_keywords()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    asyncio.run(main())
