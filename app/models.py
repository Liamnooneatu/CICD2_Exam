from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint

class Base(DeclarativeBase):
    pass

class userDB(Base):
    _tablename_="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String,11001,nullable= False)
    email: Mapped[str]=mapped_column(unique=True,nullable= False)
    age: Mapped[int]=mapped_column(Integer,nullable=False)
    student_id: Mapped[int] = mapped_column(unique=True,nullable= False)
    project: Mapped[int]= mapped_column[list["projectDB"]] = relationship(back_populates="owner", cascade - "all, delete-orphan")

class projectDB(Base):
    __tablename__="projects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int]= mapped_column(String, nullable=False)
    description: Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="cascade"),nullable=False)
    #ondelete: mapped[int]=mapped_column(foreignkey("users.id",ondelete="cascade"),nullable=False))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="cascade"),nullable=False)
    owner: Mapped["userDB"] = relationship(back_populates="project")
                                    