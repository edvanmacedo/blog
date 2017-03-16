from db_user import User
from blog_handler import BlogHandler
from utils import *
from db_comment import Comment
import time

class DeleteComment(BlogHandler):
    def get(self, post_id, comment_id):
        if self.user:
            key = db.Key.from_path('Comment', int(comment_id),
                                   parent=blog_key())
            c = db.get(key)            
            c.delete()
            self.redirect("/"+post_id)
        else:
            self.redirect("/")