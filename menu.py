#Functions for main text menu loop

import ex_01_connection_to_db



def menu():
    print("")
    print("")
    print("--------MENU--------------------------")
    print("1 - Create table projects")
    print("2 - Create table tasks")
    print("3 - show tables")
    print("4 - dodaj project")
    print("5 - wyswietl projekty")
    print("6 - wyszukaj projekt po nazwie")
    print("0 - exit")
    print("999 - testy")
    print("--------------------------------------")
    print("")

def main_loop(conn):
    input1 = 1
    while (input1 != 0):
        menu()
        input1 = input()
        if (input1 == '1'):
            print("Dodaje tabele projects")
            ex_01_connection_to_db.just_hello()
            ex_01_connection_to_db.execute_sql(conn,ex_01_connection_to_db.create_projects_sql)
        elif (input1 == '2'):
            print("Dodaje tabele tasks")
            ex_01_connection_to_db.just_hello()
            ex_01_connection_to_db.execute_sql(conn,ex_01_connection_to_db.create_tasks_sql)
        elif (input1 == '3'):
            print("Lista tabel w bazie danych")
            ex_01_connection_to_db.sql_fetch(conn)
        elif (input1 == '4'):
            print("Dodawanie projektu")
            project1 = text_input_project()
            pr_id = ex_01_connection_to_db.add_project(conn,project1)
        elif (input1 == '5'):
            print("Wyswietlenie listy projektow")
            rows1 = print_projects(conn)
        elif (input1 == '6'):
            print("Wprowadz nazwe projektu:")
            proj_name = input()
            find_project_and_print(conn, proj_name)
        elif (input1 == '7'):
            print("Wybrales 7")
        elif(input1=='8'):
            print("Wybrales 8")
        elif (input1 == '0'):
            break
        elif(input1=='999'):
            print("testowe")
        else:
            pass

def text_input_project():
    #narazie duze uproszczenie z datami bo nie chce mi sie bawic z formatowaniem wejscia na daty
    print("Wprowadzanie nowego projektu")
    project_name = input()
    project_start_date = "2022-11-25 00:00:00"
    project_end_date = "2033-12-01 00:00:00"
    project = (project_name,project_start_date,project_end_date)
    return project

def print_projects(conn):
    #wyswietlenie wszystkich projektow
    sql_pr1 = "SELECT * FROM projects"
    rows1 = ex_01_connection_to_db.execute_select(conn,sql_pr1)
    for i in rows1:
        print(i)
    return rows1

def find_project_and_print(conn,name1):
    rows1 = ex_01_connection_to_db.find_project_by_name(conn,name1)
    print("")
    
    if(rows1!=None and len(rows1)>0):
        print("Znaleziono nastepujace projekty o nazwie"+name1+":")
        for i in rows1:
            print(i)
    else:
        print("Nie znaleziono zadnych projektow o nazwie "+name1+":")
    return rows1