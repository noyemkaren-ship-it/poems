from db.repository import UserRepository


def test_add_user():
    repo = UserRepository()
    user = repo.create_user("batya", "batya@test.com", "123456")
    assert user is not None
    assert user.username == "batya"
    assert user.email == "batya@test.com"
    assert user.password == "123456"