import sqlite3

# connect to the database
def connect_to_database():
    conn = sqlite3.connect(r'C:\Users\Jonah West\Softwares\week1\moviesdb')
    return conn

# create a new table in the database called 'Movies' with columns for title, director and year of release
def update_movie_title(movie_id, new_title):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE Movies SET title = ? WHERE movie_id = ?", (new_title, movie_id))
    conn.commit()
    conn.close()

# delete movies  from the database based on their id number
def delete_movie(movie_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Movies WHERE movie_id = ?", (movie_id,))
    conn.commit()
    conn.close()

# connect to the database
conn = sqlite3.connect(r'C:\Users\Jonah West\Softwares\week1\moviesdb')

# create a cursor object
cursor = conn.cursor()

# execute the CREATE TABLE command for Movies table
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
                       movie_id INTEGER PRIMARY KEY,
                       title TEXT,
                       release_date DATE,
                       director TEXT,
                       genre TEXT
)''')

# insert data into the Movies table
movies_data = [
    ('The Shawshank Redemption', '1994-10-14', 'Frank Darabont', 'Drama'),
    ('The Godfather', '1972-03-24', 'Francis Ford Coppola', 'Crime'),
    ('The Dark Knight', '2008-07-18', 'Christopher Nolan', 'Action'),
    ('Pulp Fiction', '1994-10-14', 'Quentin Tarantino', 'Crime'),
    ('Schindler\'s List', '1993-12-15', 'Steven Spielberg', 'Biography'),
    ('Inception', '2010-07-16', 'Christopher Nolan', 'Action'),
    ('The Matrix', '1999-03-31', 'Lana Wachowski, Lilly Wachowski', 'Action'),
    ('Forrest Gump', '1994-07-06', 'Robert Zemeckis', 'Drama'),
    ('The Lord of the Rings: The Return of the King', '2003-12-17', 'Peter Jackson', 'Adventure'),
    ('Fight Club', '1999-10-15', 'David Fincher', 'Drama'),
    ('Transformers', '2007-07-03', 'Michael Bay', 'Action')
]

# use execute method of the cursor object to insert records
cursor.executemany('''
    INSERT INTO Movies (title, release_date, director, genre) VALUES (?, ?, ?, ?)
''', movies_data)

conn.commit() # commit the transaction

# create Directors table
cursor.execute('''CREATE TABLE IF NOT EXISTS Directors (
                       director_id INTEGER PRIMARY KEY,
                       name TEXT
)''')

# insert data into Directors table
directors_data = [   
    ('Frank Darabont',),
    ('Francis Ford Coppola',),
    ('Christopher Nolan',),
    ('Quentin Tarantino',),
    ('Steven Spielberg',),
    ('Christopher Nolan',), 
    ('Lana Wachowski',),
    ('Robert  Zemeckis',),
    ('Peter Jackson',),
    ('David Fincher',),
    ('Michael Bay',)
]

# insert records using executor method of the cursor object with a tuple containing the query and the record
cursor.executemany('''
    INSERT INTO Directors (name) VALUES (?)
''', directors_data)

# perform a join between Movies and Directors tables
cursor.execute('''
    SELECT Movies.title, Directors.name 
    FROM Movies 
    INNER JOIN Directors ON Movies.director = Directors.name
''') 

# fetch and display the joined data
joined_data = cursor.fetchall() 
for row in joined_data:
    print(row)

# close the database connection
conn.close()
