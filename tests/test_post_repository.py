from lib.post_repository import PostRepository
from lib.post import Post

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Post(1, 'my title 1', 'My Content', 0, 1),
        Post(2, 'my title 2', 'My Content', 0, 2)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.find(2)
    assert result == Post(2, 'my title 2', 'My Content', 0, 2)

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'my Title 3', 'My Content 3', 1, 1))
    assert repository.all() == [
        Post(1, 'my title 1', 'My Content', 0, 1),
        Post(2, 'my title 2', 'My Content', 0, 2),
        Post(3, 'my Title 3', 'My Content 3', 1, 1)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
        Post(2, 'my title 2', 'My Content', 0, 2)
    ]

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(1)
    post.title = "New title"
    assert repository.update(post) is None
    assert repository.all() == [
        Post(1, 'New title', 'My Content', 0, 1),
        Post(2, 'my title 2', 'My Content', 0, 2),
    ]
