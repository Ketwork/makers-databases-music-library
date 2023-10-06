from lib.user import User

"""
constructs with a username and an email
"""
def test_constructs():
    user = User(1, "My Username", "My Email")
    assert user.id == 1
    assert user.username == "My Username"
    assert user.email == "My Email"

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test User", "Test Genre")
    user2 = User(1, "Test User", "Test Genre")
    assert user1 == user2

"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "Test User", "Test Genre")
    assert str(user) == "User(1, Test User, Test Genre)"