import sqlite3

def connect_to_database():
    conn = sqlite3.connect(r'C:\Users\Jonah West\Softwares\week1\moviesdb')
    return conn

def update_movie_title(movie_id, new_title):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE Movies SET title = ? WHERE movie_id = ?", (new_title, movie_id))
    conn.commit()
    conn.close()

def delete_movie(movie_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Movies WHERE movie_id = ?", (movie_id,))
    conn.commit()
    conn.close()

# Connect to the database
conn = sqlite3.connect(r'C:\Users\Jonah West\Softwares\week1\moviesdb')

# Create a cursor object
cursor = conn.cursor()

# Execute the CREATE TABLE command for Movies table
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
                       movie_id INTEGER PRIMARY KEY,
                       title TEXT,
                       release_date DATE,
                       director TEXT,
                       genre TEXT
)''')

# Insert data into the Movies table
movies_data = [
    ('The Shawshank Redemption', '1994-10-14', 'Frank Darabont', 'Drama'),
    ('The Godfather', '1972-03-24', 'Francis Ford Coppola', 'Crime'),
    ('The Dark Knight', '2008-07-18', 'Christopher Nolan', 'Action'),
    ('Pulp Fiction', '1994-10-14', 'Quentin Tarantino', 'Crime'),
    ('Schindler\'s List', '1993-12-15', 'Steven Spielberg', 'Biography')
]

cursor.executemany('''
    INSERT INTO Movies (title, release_date, director, genre) VALUES (?, ?, ?, ?)
''', movies_data)

# Commit the transaction
conn.commit()

# Create Directors table
cursor.execute('''CREATE TABLE IF NOT EXISTS Directors (
                       director_id INTEGER PRIMARY KEY,
                       name TEXT
)''')

# Insert data into Directors table
directors_data = [
    ('Frank Darabont',),
    ('Francis Ford Coppola',),
    ('Christopher Nolan',),
    ('Quentin Tarantino',),
    ('Steven Spielberg',)
]

cursor.executemany('''
    INSERT INTO Directors (name) VALUES (?)
''', directors_data)

# Perform a join between Movies and Directors tables
cursor.execute('''
    SELECT Movies.title, Directors.name 
    FROM Movies 
    INNER JOIN Directors ON Movies.director = Directors.name
''')

# Fetch and display the joined data
joined_data = cursor.fetchall()
for row in joined_data:
    print(row)

# Close the database connection
conn.close()
