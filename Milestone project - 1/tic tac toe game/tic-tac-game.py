import random

def playground_set():
#this is for initialize the playground
	playground = [[] for i in range(3)]
	#i - string number
	#j - column number 
	for i in range(3):
	    for j in range(3):
	        playground[i].append(' ')

	return playground

from IPython.display import clear_output

def playground_print(playground):
#list unpacking - you can unpack every sequence
#this is for printing the playground
    clear_output()
    for i,j,k in playground:
        print(i,j,k)

def playground_check(player_number, player_marker, playground):
#check the playground for winning conditions
    free_slots = 0

    if (playground[0][0] == player_marker and 
        playground[0][1] == player_marker and
        playground[0][2] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    elif (playground[0][0] == player_marker and 
        playground[1][0] == player_marker and
        playground[2][0] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    elif (playground[0][0] == player_marker and 
        playground[1][1] == player_marker and
        playground[2][2] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    elif (playground[1][0] == player_marker and 
        playground[1][1] == player_marker and
        playground[1][2] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    elif (playground[2][0] == player_marker and 
        playground[2][1] == player_marker and
        playground[2][2] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    elif (playground[0][1] == player_marker and 
        playground[1][1] == player_marker and
        playground[2][1] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    elif (playground[0][2] == player_marker and 
        playground[1][2] == player_marker and
        playground[2][2] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    elif (playground[0][2] == player_marker and 
        playground[1][1] == player_marker and
        playground[2][0] == player_marker):
            print(f'Game over! Player-{player_number} win')
            return True

    else:
        for i in range(3):
            for j in range(3):
                if playground[i][j] == ' ':
                    free_slots +=1
        
        if free_slots == 1:
            print("Game over! Nobody wins!")
            return True

def player_marker_set():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O: ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def players_input(playground):
    args = []
    while True:
        player_input = input()
        #i = player_input.split()[0]
        #j = player_input.split()[1]
        
        if players_input_check(player_input) != False:
            i = int(player_input[0])
            j = int(player_input[2])
            if playground_slot_check(playground,i,j):
                return i,j

def players_input_check(args):
    if len(args) != 3:
        print("Enter [i]space[j], where i - string, j - column")
        return False
    
    if (args[0] in ['0','1','2'] and
        args[2] in ['0','1','2']):
            return args[0], args[2]
    
    else:
        print("Enter 0,1,2 please")
        return False

def playground_slot_check(playground,i,j):
    if playground[i][j] in ['X','O']:
        print("This slot already set! Please choose another:")
        return False
    else:
        return True

def players_turn(player_number,player_marker,playground):
    #player's turn
    
    if player_number == '1':
        print(f"Player {player_number} turn:")
        i,j = players_input(playground)
        playground[i][j] = player_marker
    elif player_number == '2':
        print(f"Player {player_number} turn:")
        i,j = players_input(playground)
        playground[i][j] = player_marker
    
    playground_print(playground)

    return playground_check(player_number,player_marker,playground)

def replay():
    replay = input("Want to play again?(Yes or No:")
    
    if replay == 'Yes':
        return True

def game():
    playground = playground_set()
    player_1_marker, player_2_marker = player_marker_set()
    flip = random.randint(0,1)
    
    if flip == 0:
        while (players_turn('1',player_1_marker, playground) != True and 
               players_turn('2',player_2_marker, playground) !=True):
                continue
        
    else:
        while (players_turn('2',player_2_marker, playground) != True and 
               players_turn('1',player_1_marker, playground) !=True):
                continue
    
    if replay():
        game()

if __name__ == '__main__':
	game()
