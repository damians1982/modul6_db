#Functions for main text menu loop

import ex_01_connection_to_db



def menu():
    print("--------MENU--------------------------")
    print("1 - Create table projects")
    print("2 - Create table tasks")
    print("3 - show tables")
    print("4 - dodaj project")
    print("0 - exit")
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
        elif (input1 == '5'):
            print("Wybrales 5")
        elif (input1 == '6'):
            print("Wybrales 6")
        elif (input1 == '7'):
            print("Wybrales 7")
        elif(input1=='8'):
            print("Wybrales 8")
        elif (input1 == '0'):
            break
        else:
            pass