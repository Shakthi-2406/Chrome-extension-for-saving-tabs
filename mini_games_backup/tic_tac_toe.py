import random
import time



def print_as_i_want(input_item):
    i= 0
    while i<=2:
        print(input_item[i][0]," ",input_item[i][1]," ",input_item[i][2],"\n")
        i+=1

def check_out(question):
    if question[0][0] == question[0][1] == question[0][2] == 'X' or question[1][0] == question[1][1] == question[1][2] == 'X' or question[2][0] == question[2][1] == question[2][2] == 'X' or question[0][0] == question[1][0] == question[2][0] == 'X' or question[0][1] == question[1][1] == question[2][1] == 'X' or question[0][2] == question[1][2] == question[2][2] == 'X' or question[0][0] == question[1][1] == question[2][2] == 'X' or question[0][2] == question[1][1] == question[2][0] == 'X' :
        print("\n\n\n\t\tYou have won!!! :( :( :(\n\n\n")
        return False
    elif question[0][0] == question[0][1] == question[0][2] == 'O' or question[1][0] == question[1][1] == question[1][2] == 'O' or question[2][0] == question[2][1] == question[2][2] == 'O' or question[0][0] == question[1][0] == question[2][0] == 'O' or question[0][1] == question[1][1] == question[2][1] == 'O' or question[0][2] == question[1][2] == question[2][2] == 'O' or question[0][0] == question[1][1] == question[2][2] == 'O' or question[0][2] == question[1][1] == question[2][0] == 'O' :
        print("\n\n\n\t\tHeHeHe I have won!!! ;) :) :)\n\n\n")
        return False
    else:
        return True

def user_playing():
    while True:
        row = int(input("enter the row to place coin: "))-1
        column = int(input("enter the column to place coin: "))-1
        if 0<=row<=2 and 0<=column<=2 and [row,column] in position:
            break
        else:
            print("There are 3 rows and columns. Enter accordingly")

    user_choice = [row,column]
    position.remove(user_choice)
    question[row][column] = 'X'
    print_as_i_want(question)
    if check_out(question):
        print("\nIts my turn babe........lemme place my coin")
        time.sleep(2)
        computer_play()


def computer_play():
    comp_choice = random.choice(position)
    position.remove(comp_choice)
    row = comp_choice[0]
    column = comp_choice[1]
    question[row][column] = 'O'
    print_as_i_want(question)
    if check_out(question):
        print("\nYou can play now....")
        user_playing()






end = 0
position = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
question = [['_','_','_'],['_','_','_'],['_','_','_']]
print_as_i_want(question)
print("You can start placing coins :)")
user_playing()




    
    







