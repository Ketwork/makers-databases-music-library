from lib.post import Post

"""
constructs with an id, title, content, views and user_id
"""
def test_constructs():
    post = Post(1, "My Title", "My content", 2, 1)
    assert post.id == 1
    assert post.title == "My Title"
    assert post.content == "My content"
    assert post.views == 2
    assert post.user_id == 1

"""
We can compare two identical users
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "My Title", "My content", 2, 1)
    post2 = Post(1, "My Title", "My content", 2, 1)
    assert post1 == post2

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "My Title", "My content", 2, 1)
    assert str(post) == "Post(1, My Title, My content, 2, 1)"