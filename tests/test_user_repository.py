from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result == [
        User(1, 'ket', 'ket@ket.net'),
        User(2, 'User 2', 'user2@ket.net')
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.find(2)
    assert result == User(2, 'User 2', 'user2@ket.net')

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "The Beatles", "Rock@net.com"))
    assert repository.all() == [
        User(1, 'ket', 'ket@ket.net'),
        User(2, 'User 2', 'user2@ket.net'),
        User(3, "The Beatles", "Rock@net.com")
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
        User(2, 'User 2', 'user2@ket.net')
    ]

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    user.email = "ket@ket.com"
    assert repository.update(user) is None
    assert repository.all() == [
        User(1, 'ket', 'ket@ket.com'),
        User(2, 'User 2', 'user2@ket.net')
    ]
