# "Database code" for the DB Forum.
import bleach
import datetime
import psycopg2


POSTS = [("This is the first post.", datetime.datetime.now())]


def get_posts():
    """ Return all posts from the 'database', most recent first. """
    with psycopg2.connect("dbname=forum") as db:
        c = db.cursor()
        c.execute("SELECT time, content FROM posts ORDER BY time DESC")
        posts = [{'content': str(row[1]), 'time': str(row[0])}for row in c.fetchall()]
    return reversed(posts)


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    cleaned_content = bleach.clean(content)
    with psycopg2.connect("dbname=forum") as db:
        c = db.cursor()
        c.execute("INSERT INTO posts (content) VALUES (%s)", (cleaned_content, ))
        db.commit()
