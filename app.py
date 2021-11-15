from flask import Flask, render_template, request, redirect, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////mnt/6B334F454414F5E5/WebApps/blog_flask/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = "posts" 
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String(2000), nullable=False) 

@app.route('/')
def inicio():
   posts = Post.query.order_by(Post.fecha.desc()).all()

   return render_template("inicio.html", posts=posts)

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")

@app.route("/crear_post", methods=["POST"]) 
def crear_post():
   titulo = request.form.get('titulo') 
   texto = request.form.get('texto') 
   post = Post(titulo=titulo, texto=texto)
   db.session.add(post)
   db.session.commit()
 
   return redirect('/')

@app.route('/borrar_post', methods=['POST'])
def borrar():
    try:
        post_id = request.form.get('post_id') 
        post = db.session.query(Post).filter(Post.id == post_id).first()
        db.session.delete(post)
        db.session.commit()
        return jsonify(success=True, data='data') 
    except Exception as e:
        db.session.rollback()
        db.session.flush()
        return jsonify(success=False, data='data', error=e) 

@app.route('/editar_post/<int:post_id>')
def editar_post(post_id):
    post = Post.query.get(post_id) 

    return render_template('editar_post.html', post=post)

@app.route('/actualizar_post/<int:post_id>', methods=['POST'])
def actualizar_post(post_id):
    post = Post.query.get(post_id)
    post.titulo = request.form.get('titulo')
    post.texto = request.form.get('texto') 
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


