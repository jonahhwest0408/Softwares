# Overview

This movie management system utilizes a SQLite Relational Database to store movie and director information. Users can add, update, delete, and query movie data via the program, which integrates SQL commands to interact with the database, facilitating efficient management and retrieval of movie-related information.

The purpose of writing this software is to create a flexible and efficient system for managing movie data, allowing users to easily add, update, delete, and query movie information. It aims to provide a user-friendly interface for interacting with a SQL Relational Database, facilitating effective organization and retrieval of movie-related data.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The relational database used in this software is SQLite. It is a lightweight, embedded SQL database engine that is widely used due to its simplicity, reliability, and ease of integration into various applications. SQLite supports standard SQL syntax and provides features for creating, managing, and querying relational databases efficiently.

The relational database created for this software consists of two tables:

Movies Table:
Columns:
movie_id (INTEGER): Primary key for uniquely identifying each movie.
title (TEXT): Stores the title of the movie.
release_date (DATE): Represents the release date of the movie.
director (TEXT): Stores the name of the director of the movie.
genre (TEXT): Represents the genre of the movie.

Directors Table:
Columns:
director_id (INTEGER): Primary key for uniquely identifying each director.
name (TEXT): Stores the name of the director.
These tables are designed to efficiently store and manage information about movies and directors in a structured format, facilitating easy retrieval and manipulation of data.

# Development Environment

The software was developed using Python programming language and SQLite for the relational database management. Python's built-in sqlite3 module was utilized for interacting with the SQLite database, while standard Python libraries were employed for handling data manipulation and program execution. Additionally, VSCode was used for writing and testing the code.


The software was primarily developed using Python, a high-level programming language known for its simplicity and versatility. Python's built-in sqlite3 module was utilized for interacting with the SQLite database, providing functions to execute SQL commands and manage database connections. Additionally, no external libraries were used for this project, as the functionality required for database interaction and data manipulation was available within Python's standard library.

# Useful Websites

- [YouTube](https://www.youtube.com/watch?v=c8yHTlrs9EA)
- [YouTube](https://www.youtube.com/watch?v=LZPyuLnZI34&list=WL&index=2&t=449s)

# Future Work

- Implement user input validation to prevent invalid data entry.
- Enhance error messages for better user feedback and troubleshooting.
- Optimize database queries and transactions for improved performance.