from app import app
from flask import request, jsonify
from flask import abort
from app.models import Post
from app import db


# meme=[

#     {

# "id": "1",       

# "name": "MS Dhoni",

# "url": "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg",

# "caption": "Meme for my place"

#     },

#     {

# "id": "2",

# "name": "Viral Kohli",

# "url": "https://images.pexels.com/photos/1078983/pexels-photo-1078983.jpeg",

# "caption": "Another home meme"

#     },

#     {

# "id": "3",

# "name": "Viral Kohli",

# "url": "https://images.pexels.com/photos/1078983/pexels-photo-1078983.jpeg",

# "caption": "Another home meme"

#     },

#     {

# "id": "4",

# "name": "Viral Kohli",

# "url": "https://images.pexels.com/photos/1078983/pexels-photo-1078983.jpeg",

# "caption": "Another home meme"

#     }

#  	]

# lastid=2


@app.route('/memes', methods=['GET'])
def ret():
	meme=Post.query.order_by(Post.timestamp.desc()).limit(100).all()
	#.with_entities(Post.id, Post.name, Post.url, Post.caption)
	# for m in meme:
	# 	print(m.name)
	ret=[]

	for m in meme:
		obj={}
		obj["id"]=str(m.id)
		obj["name"]=str(m.name)
		obj["url"]=str(m.url)
		obj["caption"]=str(m.caption)
		ret.append(obj)
	return jsonify(ret)

@app.route('/memes/<int:meme_id>', methods=['GET'])
def get_meme(meme_id):
	meme=Post.query.get(meme_id)
	obj={}
	obj["id"]=str(meme.id)
	obj["name"]=str(meme.name)
	obj["url"]=str(meme.url)
	obj["caption"]=str(meme.caption)
	return obj

@app.route('/memes',methods=['POST'])
def retpost():
	#global lastid
	data=request.get_json(force=True)
	name1=data['name']
	url1=data['url']
	caption1=data['caption']
	#return url
	# newpost={}
	# lastid=lastid+1
	# newpost['id']=str(lastid)
	# newpost['name']=str(name)
	# newpost['url']=str(url)
	# newpost['caption']=str(caption)
	# meme.append(newpost)
	post=Post(name=name1,url=url1,caption=caption1)
	db.session.add(post)
	db.session.flush()
	db.session.refresh(post)
	lastid=post.id
	db.session.commit()
	obj={}
	obj["id"]=str(lastid)
	return jsonify(obj)
	#return jsonify(meme)