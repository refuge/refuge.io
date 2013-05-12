import datetime
import codecs

from couchdbkit import *

class Post(Document):
    body = StringProperty()
    title = StringProperty()
    created_at = DateTimeProperty()

# server object
server = Server()

# create database
db = server.get_or_create_db("refuge")

# associate Greeting to the db
Post.set_db(db)

posts = Post.view("refuge.blog/latest_posts").all()

for post in posts:
    post_date = post.created_at
    post_name = "%04d-%02d-%02d-%s.md" % (post_date.year, post_date.month, post_date.day, post._id)
    print "Creating post file '%s'." % post_name
    f = codecs.open(post_name, encoding='utf-8',  mode='w+')
    f.write("---\n")
    f.write("layout: post\n")
    f.write("title: %s\n" % post.title)
    f.write("---\n")
    f.write("\n")
    f.write(post.body)
    f.close()

