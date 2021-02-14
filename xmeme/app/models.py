from app import db
from datetime import datetime

class Post(db.Model):
	id=db.Column(db.Integer, primary_key=True )
	name=db.Column(db.String(40))
	timestamp=db.Column(db.DateTime, index=True, default=datetime.utcnow)
	caption=db.Column(db.String(140))
	url=db.Column(db.String(140)) 

	def __repr__(self):
		return '<Memeowner {}>'.format(self.name)

	# def top_memes(self):
	# 	return Post.query.order_by(Post.timestamp.desc()).limit(100).with_entities(Post.id, Post.name, Post.url, Post.caption)