import sqlite3
import os

DB_NAME = 'images.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS images
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  path TEXT NOT NULL)''')
    conn.commit()
    conn.close()

    # Add some initial images to the database
    initial_images = [
        'static/images/image1.jpg',
        'static/images/image2.jpg',
        'static/images/image3.jpg',
        'static/images/image4.jpg',
        'static/images/image5.jpg',
        'static/images/image6.jpg',
        'static/images/image7.jpg',
        'static/images/image8.jpg',
        'static/images/image9.jpg',
        'static/images/image10.jpg',
        'static/images/image11.jpg',
        'static/images/image12.jpg'
    ]
    
    for index in range(len(initial_images)):
        if os.path.exists(initial_images[index]):
            add_image(initial_images[index])

def add_image(path):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO images (path) VALUES (?)", (path,))
    conn.commit()
    conn.close()

def get_all_images():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM images")
    images = [{'id': row[0], 'path': row[1]} for row in c.fetchall()]
    conn.close()
    return images