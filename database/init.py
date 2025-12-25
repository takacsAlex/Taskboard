import sqlite3

def create_database(project_name: str):
    """
    :INITIALIZE DATABASE:
    
    \n:Structure:
        \ntasks(table): {id; title; description; done(0 or 1); developer_id(foreign key); difficulty_id(foreign key)},
        \ndevelopers(table): {id; name},
        \ndifficulty(table): {id; name; color}
    """
    
    with open("./.env", "w") as env:
        env.write("PROJECT_NAME=" + project_name)
    
    con = sqlite3.connect("./database/database.db")
    
    #create tables
    con.execute("""
    CREATE TABLE IF NOT EXISTS developers(
        id INTEGER PRIMARY KEY,
        name STRING
    )
    """)
    con.execute("""
    CREATE TABLE IF NOT EXISTS difficulty(
        id INTEGER PRIMARY KEY,
        name STRING,
        color STRING
    )
    """)
    con.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title STRING,
        description STRING,
        done INTEGER,
        developer_id INTEGER,
        difficulty_id INTEGER,
        FOREIGN KEY (developer_id) REFERENCES developers(id),
        FOREIGN KEY (difficulty_id) REFERENCES difficulty(id)
    )
    """)

    #fill difficulty values
    con.execute("""INSERT INTO difficulty (id, name, color) VALUES (NULL, ?, ?)""", ("easy", "green"))
    con.execute("""INSERT INTO difficulty (id, name, color) VALUES (NULL, ?, ?)""", ("medium", "yellow"))
    con.execute("""INSERT INTO difficulty (id, name, color) VALUES (NULL, ?, ?)""", ("hard", "red"))
    
    con.commit()
    con.close()