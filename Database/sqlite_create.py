# This Python file uses the following encoding: utf-8
import sqlite3

conn = sqlite3.connect('/web/Sqlite-Data/example.db')

c = conn.cursor()
c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE address
          (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
           post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES person(id))
          ''')

c.execute('''
        CREATE TABLE customer
        (first_name varchar(250) NOT NULL, last_name varchar(250) NOT NULL, username varchar(250) NOT NULL,
        email varchar(250), address varchar(250), town varchar(250))
''')

c.execute('''
        CREATE TABLE items
        (name varchar(250), cost_price INTEGER, selling_price INTEGER, quantity INTEGER)
''')


c.execute('''
          INSERT INTO person VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()
conn.close()