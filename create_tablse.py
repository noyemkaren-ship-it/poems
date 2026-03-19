from db.database import Base, engine
from shemas.ret import Returns

def create_tables():
    Base.metadata.create_all(bind=engine)
    return Returns(
        text="Таблицы успешно созданы"
    )

result = create_tables()
print(result.text)