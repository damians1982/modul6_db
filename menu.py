#Functions for main text menu loop

import ex_01_connection_to_db



def menu():
    print("--------MENU--------------------------")
    print("1 - Create table projects")
    print("2 - ")
    print("0 - exit")
    print("--------------------------------------")
    print("")

def main_loop(conn):
    input1 = 1
    while (input1 != 0):
        menu()
        input1 = input()
        if (input1 == '1'):
            ex_01_connection_to_db.just_hello()
            ex_01_connection_to_db.execute_sql(conn,ex_01_connection_to_db.create_projects_sql)

        elif (input1 == '2'):
            print("Wybrales 2")
        elif (input1 == '3'):
            print("Wybrales 3")
        elif (input1 == '4'):
            print("Wybrales 4")
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