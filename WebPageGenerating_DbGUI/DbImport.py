import sqlite3

conn = sqlite3.connect('webpage_gen.db')

def createTable():
    conn.execute("CREATE TABLE if not exists webpage_gen(\
    id INTEGER PRIMARY KEY AUTOINCREMENT, \
    name TEXT,\
    title TEXT,\
    message TEXT,\
    background_color TEXT,\
    font_style TEXT,\
    font_size INTEGER);")

def populate_table():
    conn.execute("DELETE FROM webpage_gen;")
    conn.commit()
    conn.execute("INSERT INTO webpage_gen(name, title, message, background_color, font_style, font_size) VALUES \
    ('Sale', 'Sa!e Sa!e Sa!e', 'Come join us this weekend for a blowout sale!', 'red', 'normal', 12),\
    ('Charity', 'Help us help others!', 'Come visit us this weekend when 20% of proceeds go to local charity!', 'yellow', 'italic', 14),\
    ('Free', 'Free coffee!', 'Stop by this weekend for free coffee while you shop!', 'lightblue', 'normal', 16);")
    conn.commit()
    
def pull_theme(theme_selection):
    thematic = "SELECT * FROM webpage_gen WHERE name = '{}';".format(theme_selection)
    cursor = conn.execute(thematic)
    rows = cursor.fetchall()
    return rows

createTable()
populate_table()
