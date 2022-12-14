# `ex_01_conection_to_db.py`

import sqlite3
from sqlite3 import Error
from datetime import datetime
import menu
import csv

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
       return conn
   except Error as e:
       print(e)
   
   return conn

def create_connection_in_memory():
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(":memory:")
       print(f"Connected, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

def execute_sql(conn, sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        print("executing sql:"+sql)
    except Error as e:
        print("Error:")
        print(e)

def execute_select(conn,sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script (SELECT)
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        print("executing sql:"+sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error:")
        print(e)

def find_project_by_name(conn,name1):
    #finding project by name
    try:
        cur = conn.cursor()

        cur.execute("SELECT * FROM projects WHERE nazwa=?",(name1,))
        print("executing sql: SELECT * FROM projects WHERE name="+str(name1))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error:")
        print(e)


def add_project(conn,project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    commit_result = conn.commit()
    print("executing sql:"+sql+str(project))
    return cur.lastrowid

def add_task(conn,task):
    """
    Create a new task into the task table
    :param conn:
    :param task:
    :return: task_id
    """

    sql = '''INSERT INTO tasks(projekt_id,nazwa,opis,status,start_date,end_date)
             VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()
    print("executing sql:"+sql)
    return cur.lastrowid

def update_project_by_id(conn,id,params):
    print("update_project_by_id")

    sql1 = f"UPDATE projects SET nazwa='{params[0]}',start_date='{params[1]}',end_date='{params[2]}' WHERE id={id};"
    print("sql="+sql1)
    try:
        cur = conn.cursor()
        cur.execute(sql1)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

def deleta_project_by_id(conn,id):

    sql1 = f"DELETE FROM projects WHERE id={id}"
    print("sql="+sql1)
    try:
        cur = conn.cursor()
        cur.execute(sql1)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

def just_hello():
    print("Just hello")

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())



def create_measures_table(conn,sql1):
    print("Inside: create_measures_table()")
    file1 = open('clean_measure.csv')
    sql2 = "INSERT INTO measures ("

    csvreader = csv.reader(file1)

    header = []
    header = next(csvreader)

    item_num=0
    for menu_item in header:
        sql1 = sql1 + ","+menu_item+" text NOT NULL"
        if(len(header)!=item_num+1):
            sql2=sql2+menu_item+","
        else:
            sql2=sql2+menu_item+")"
        item_num+=1
    sql1 = sql1+");"
    
    execute_sql(conn,sql1)  #creating table

    sql2+=" VALUES"

    for row in csvreader:
        #dla ka??dego wiersza robimy ladnego inserta
        row_len = 0
        sql_row = ""
        sql_row = sql2
        for item in row:
            if(row_len==0):
                sql_row=sql_row+"('"+item+"'"
            elif(row_len < (len(row)-1)):
                sql_row=sql_row+",'"+item+"'"
            else:
                sql_row=sql_row+",'"+item+"')"
            row_len+=1
        #TU INSERT
        execute_sql(conn,sql_row)
    file1.close()

def create_stations_table(conn,sql1):
    print("Inside: create_stations_table()")
    file1 = open('clean_stations.csv')
    sql2 = "INSERT INTO stations ("

    csvreader = csv.reader(file1)

    header = []
    header = next(csvreader)

    item_num=0
    for menu_item in header:
        sql1 = sql1 + ","+menu_item+" text NOT NULL"
        print(menu_item)
        if(len(header)!=item_num+1):
            sql2=sql2+menu_item+","
        else:
            sql2=sql2+menu_item+")"
        item_num+=1
    sql1 = sql1+");"

    execute_sql(conn,sql1)  #creating table

    sql2+=" VALUES"

    for row in csvreader:
        #dla ka??dego wiersza robimy ladnego inserta
        row_len = 0
        sql_row = ""
        sql_row = sql2
        for item in row:
            if(row_len==0):
                sql_row=sql_row+"('"+item+"'"
            elif(row_len < (len(row)-1)):
                sql_row=sql_row+",'"+item+"'"
            else:
                sql_row=sql_row+",'"+item+"')"
            row_len+=1
        #TU INSERT
        execute_sql(conn,sql_row)
    file1.close()

create_projects_sql = """
-- projects table
CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    nazwa text NOT NULL,
    start_date text,
    end_date text
);
"""

create_tasks_sql = """
-- zadanie table
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    projekt_id integer NOT NULL,
    nazwa VARCHAR(250) NOT NULL,
    opis TEXT,
    status VARCHAR(15) NOT NULL,
    start_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (projekt_id) REFERENCES projects (id)
);
"""

create_measures_sql = """
-- zadanie table
CREATE TABLE IF NOT EXISTS measures (
    id integer PRIMARY KEY
"""

create_stations_sql = """
-- zadanie table
CREATE TABLE IF NOT EXISTS stations (
    id integer PRIMARY KEY
"""


if __name__ == '__main__':  

    now1 = datetime.now()
    time1 = now1.strftime("%H:%M:%S")
    row1 = """
    INSERT INTO projects(id, nazwa, start_date, end_date)
    VALUES (1,
        "Zrob zadania",
        "2020-05-08 00:00:00",
        "2020-05-10 00:00:00"
        );
    """
    row2 = """
    INSERT INTO projects(id, nazwa, start_date, end_date)
    VALUES (4,
        "dalej robimy i robimy",
        "2020-06-05 00:00:00",
        "2020-06-16 00:00:00"
        );
    """

    select1 = """
    SELECT * 
    FROM projects;
    """

    db_file = "database.db"
   
    conn = create_connection(r"database.db")

    if(conn is not None):
        menu.main_loop(conn)
        #execute_sql(conn, create_projects_sql)
        #execute_sql(conn, create_tasks_sql)
        #execute_sql(conn,row1)
        #execute_sql(conn,row2)

        #project = ("Data Scientist", "2022-11-25 00:00:00", "2033-12-01 00:00:00")
        #pr_id = add_project(conn, project)

        #task = (9,"Analiza Apple","Jakie jest ryzyko zwi??zane z Applem","Czeka","20222-12-01 00:00:00","2023-05-22 00:00:00")
        #pr_id2 = add_task(conn,task)

        #sql1 = "SELECT * from projects"
        #rows1 = execute_select(conn,sql1)

        #sql2 = "SELECT * from tasks"
        #rows2 = execute_select(conn,sql2)

        #for i in rows1:
        #    print(i)

        #print("---")

        #for i in rows2:
        #    for j in i:
        #        print(str(j).encode("utf-8"))

        #execute_sql(conn,select1)
        conn.close()
   
    