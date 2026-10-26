import os
from flask import Flask, render_template, request, redirect, url_for
import pymysql
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'mysecretkey123')

UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'library_db'),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT BOOK.book_id, BOOK.title, BOOK.price, BOOK.cover_url, 
                   AUTHOR.name AS author_name, AUTHOR.author_id
            FROM BOOK 
            JOIN AUTHOR ON BOOK.author_id = AUTHOR.author_id
        """)
        books = cursor.fetchall()

        cursor.execute("SELECT * FROM AUTHOR")
        authors = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=books, authors=authors)

@app.route('/add_author', methods=['POST'])
def add_author():
    name = request.form['name']
    country = request.form['country']
    photo = request.files.get('photo')
    
    photo_filename = None
    if photo and allowed_file(photo.filename):
        photo_filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO AUTHOR (name, country, photo_url) VALUES (%s, %s, %s)",
            (name, country, photo_filename)
        )
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    price = request.form['price']
    author_id = request.form['author_id']
    cover = request.files.get('cover')

    cover_filename = None
    if cover and allowed_file(cover.filename):
        cover_filename = secure_filename(cover.filename)
        cover.save(os.path.join(app.config['UPLOAD_FOLDER'], cover_filename))

    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO BOOK (title, price, author_id, cover_url) VALUES (%s, %s, %s, %s)",
            (title, price, author_id, cover_filename)
        )
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_author/<int:author_id>', methods=['POST'])
def delete_author(author_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM AUTHOR WHERE author_id = %s", (author_id,))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)