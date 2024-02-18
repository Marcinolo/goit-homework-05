

import sqlite3
from faker import Faker
import random

# Utwórz instancję Faker
fake = Faker()

# Połącz się z bazą danych SQLite
conn = sqlite3.connect('example4.db')
cur = conn.cursor()

# Utwórz tabelę 'Groups'
cur.execute('''CREATE TABLE Groups (
                id INTEGER PRIMARY KEY,
                group_name VARCHAR(50),
                year INT
            )''')

# Utwórz tabelę 'Students'
cur.execute('''CREATE TABLE Students (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                group_id INT,
                FOREIGN KEY (group_id) REFERENCES Groups(id)
            )''')

# Utwórz tabelę 'Lecturers'
cur.execute('''CREATE TABLE Lecturers (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50)
            )''')

# Utwórz tabelę 'Subjects'
cur.execute('''CREATE TABLE Subjects (
                id INTEGER PRIMARY KEY,
                subject_name VARCHAR(100),
                lecturer_id INT,
                FOREIGN KEY (lecturer_id) REFERENCES Lecturers(id)
            )''')

# Utwórz tabelę 'Grades'
cur.execute('''CREATE TABLE Grades (
                id INTEGER PRIMARY KEY,
                student_id INT,
                subject_id INT,
                group_id_id INT,
                grade DECIMAL(3, 2),
                date_given DATE,
                FOREIGN KEY (student_id) REFERENCES Students(id),
                FOREIGN KEY (subject_id) REFERENCES Subjects(id),
                FOREIGN KEY (group_id_id) REFERENCES Students(group_id)
            )''')

# Wypełnij tabelę 'Students' 40 losowymi nazwiskami i imionami
for _ in range(40):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = random.randint(1, 3)  # Losowo wybierz numer od 1 do 3
    cur.execute("INSERT INTO Students (first_name, last_name, group_id) VALUES (?, ?, ?)",
                (first_name, last_name, group_id))

# Wypełnij tabelę 'Groups' trzema wybranymi grupami
groups = ['Grupa A', 'Grupa B', 'Grupa C']
for group_name in groups:
    year = random.randint(2018, 2022)
    cur.execute("INSERT INTO Groups (group_name, year) VALUES (?, ?)", (group_name, year))

# Wypełnij tabelę 'Subjects' 7 wybranymi przedmiotami
subjects = ['Matematyka', 'Fizyka', 'Chemia', 'Informatyka', 'Historia', 'Biologia', 'Język angielski']
lecturer_ids = list(range(1, 5))  # Zakładam, że wykładowcy mają identyfikatory od 1 do 4
for subject_name in subjects:
    lecturer_id = random.choice(lecturer_ids)
    cur.execute("INSERT INTO Subjects (subject_name, lecturer_id) VALUES (?, ?)", (subject_name, lecturer_id))

# Wypełnij tabelę 'Lecturers' 4 wykładowcami
for _ in range(4):
    first_name = fake.first_name()
    last_name = fake.last_name()
    #email = fake.email()
    cur.execute("INSERT INTO Lecturers (first_name, last_name) VALUES (?, ?)", (first_name, last_name))

# Wypełnij tabelę 'Grades' 20 ocenami dla każdego studenta
#students_ids = list(range(1, 41))  # Zakładam, że identyfikatory studentów są od 1 do 40
#for student_id in students_ids:
    #for subject_id in range(1, 8):  # Zakładam, że identyfikatory przedmiotów są od 1 do 7
        #for _ in range(20):
            #grade = round(random.uniform(2, 5), 2)
            #date_given = fake.date_between(start_date='-1y', end_date='today')
            #cur.execute("INSERT INTO Grades (student_id, subject_id, grade, date_given) VALUES (?, ?, ?, ?)",
                        #(student_id, subject_id, grade, date_given))

students_ids = list(range(1, 41))  # Zakładam, że identyfikatory studentów są od 1 do 40
for student_id in students_ids:
    for subject_id in range(1, 8):  # Zakładam, że identyfikatory przedmiotów są od 1 do 7
        for _ in range(20):
            grade = round(random.uniform(2, 5), 2)
            date_given = fake.date_between(start_date='-1y', end_date='today')
            group_id = random.randint(1, 3)  # Losowo wybierz identyfikator grupy
            cur.execute("INSERT INTO Grades (student_id, subject_id, group_id_id, grade, date_given) VALUES (?, ?, ?, ?, ?)",
                        (student_id, subject_id, group_id, grade, date_given))


# Zatwierdź zmiany i zamknij połączenie
conn.commit()
conn.close()