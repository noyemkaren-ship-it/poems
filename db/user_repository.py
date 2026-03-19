from db.database import session, User, Poem
import datetime


class UserRepository:
    def __init__(self):
        self.session = session

    def create_user(self, name, email, password):
        db_user = User(
            username=name,
            email=email,
            password=password
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def delete_user(self, username):
        user = self.session.query(User).filter_by(username=username).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            return {"message": "User deleted"}
        return {"message": "User does not exist"}

    def get_user(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def get_all_users(self):
        return self.session.query(User).all()


class PoemsRepository:
    def __init__(self):
        self.session = session

    def create_poem(self, name, username, text):
        date = datetime.datetime.now()
        db_poem = Poem(
            username=username,
            name=name,
            text=text,
            date=date
        )
        self.session.add(db_poem)
        self.session.commit()
        self.session.refresh(db_poem)
        return db_poem

    def delete_poem(self, name):
        poem = self.session.query(Poem).filter_by(name=name).first()
        if poem:
            self.session.delete(poem)
            self.session.commit()
            return {"message": "Poem deleted"}
        return {"message": "Poem does not exist"}

    def get_all_poems(self):
        poems = self.session.query(Poem).all()
        return poems if poems else []

    def get_poem(self, username):
        return self.session.query(Poem).filter_by(username=username).first()

    def get_poem_by_author(self, username):
        poems = self.session.query(Poem).filter_by(username=username).all()
        return poems if poems else []