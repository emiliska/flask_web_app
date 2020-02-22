class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Cloumn(db.Integer, primary_key=True)
    body = db.Cloumn(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class User(UserMixin, db.Model):
    # ...
    posts = db.relationship('Post', backref='author', lazy='dynamic')

