from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column

Base = declarative_base()


class Keyword(Base):
    __tablename__ = "keyword"
    keyword_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    keyword_name: Mapped[str] = mapped_column(String(30))

    step_keywords: Mapped[list["StepKeyword"]] = relationship("StepKeyword", back_populates="keyword",
                                                              cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Keyword(keyword_id={self.keyword_id!r}, keyword_name={self.keyword_name!r})"


class Step(Base):
    __tablename__ = "step"
    step_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    step_name: Mapped[str] = mapped_column(String(30))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lesson.lesson_id"))

    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="steps")
    step_keywords: Mapped[list["StepKeyword"]] = relationship("StepKeyword", back_populates="step",
                                                              cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Step(step_id={self.step_id!r}, step_name={self.step_name!r}, lesson_id={self.lesson_id!r})"


class StepKeyword(Base):
    __tablename__ = "step_keyword"
    step_keyword_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    step_id: Mapped[int] = mapped_column(ForeignKey("step.step_id"))
    keyword_id: Mapped[int] = mapped_column(ForeignKey("keyword.keyword_id"))

    step: Mapped["Step"] = relationship("Step", back_populates="step_keywords")
    keyword: Mapped["Keyword"] = relationship("Keyword", back_populates="step_keywords")

    def __repr__(self) -> str:
        return f"StepKeyword(step_keyword_id={self.step_keyword_id!r}, step_id={self.step_id!r}, keyword_id={self.keyword_id!r})"


class Module(Base):
    __tablename__ = "module"
    module_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    module_name: Mapped[str] = mapped_column(String(30))

    lessons: Mapped[list["Lesson"]] = relationship("Lesson", back_populates="module", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Module(module_id={self.module_id!r}, module_name={self.module_name!r})"


class Lesson(Base):
    __tablename__ = "lesson"
    lesson_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lesson_name: Mapped[str] = mapped_column(String(30))
    lesson_position: Mapped[str] = mapped_column(String(30))
    module_id: Mapped[int] = mapped_column(ForeignKey("module.module_id"))

    module: Mapped["Module"] = relationship("Module", back_populates="lessons")
    steps: Mapped[list["Step"]] = relationship("Step", back_populates="lesson", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return (f"Lesson(lesson_id={self.lesson_id!r}, lesson_name={self.lesson_name!r}, "
                f"lesson_position={self.lesson_position!r}, module_id={self.module_id!r})")
