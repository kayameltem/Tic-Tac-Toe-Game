from math import * # tanimladigim matriks fonksiyonunda basamak hesabi icin log10() kullandim
def matriks(liste,size):
    x = 0
    y = size
    for i in range(size) :
        for j in liste[x:y] :
            print("%{}s".format((int(log10(size*size))+2)) %j , end = " ")
        print()
        x , y = y , y + size

def check_column():
    startswith = 0
    while True:
        liste_column = list()
        if startswith < size:
            for i in liste[startswith::size]:
                liste_column.append(i)
            check_variations.append(liste_column)
            startswith += 1
        else:
            break

def check_row():
    startswith = 0
    size_copy = size
    while True:
        liste_row = list()
        if size_copy <= size * size:
            for j in liste[startswith:size_copy]:
                liste_row.append(j)
            check_variations.append(liste_row)
            startswith, size_copy = startswith + size, size_copy + size
        else:
            break

def check_diagonal():
    startswith = 0
    startswith_other = size - 1
    liste_diagonal = list()
    for i in liste[startswith:: (size + 1)]:
        liste_diagonal.append(i)
    check_variations.append(liste_diagonal)
    liste_diagonal = list()
    for j in liste[startswith_other:(1 - size):startswith_other]:
        liste_diagonal.append(j)
    check_variations.append(liste_diagonal)

def size_out_error(player_input) :
        if not (int(player_input) in range(0, size * size)) :
            print("Please enter a valid number ")
            matriks(liste, size)

def choosen_error(player_input,player) :
    if liste[int(player_input)] == player :
        print("You have made this choice before")
    elif (liste[int(player_input)] == "X" and player == "O") or (liste[int(player_input)] == "O" and player== "X") :
        print("The other player select this cell before")

while 1 :
    size = int(input("What Size Game GoPy?"))
    if size < 3 :
        print("Given size is not suitable for a two player game.\nPlease choose size at least 3. ")
    else :
        break

value = True
liste = [str(n) for n in range(size * size)]
liste_check = [str(n) for n in range(size * size)]
matriks(liste, size)
while value :
    for player in "X","O" :
        if not (value):
            break
        if player == "X" :
            player_input = input("{} turn --> ".format("Player 1"))
        else :
            player_input = input("{} turn--> ".format("Player 2"))
        size_out_error(player_input)
        if int(player_input) in range(size * size) :
            if liste[int(player_input)] !=  player_input :
                choosen_error(player_input,player)
                matriks(liste, size)
            else :
                liste[int(player_input)] = player
                check_variations = []
                check_column()
                check_row()
                check_diagonal()
                matriks(liste, size)
                for x in check_variations:
                    for i in ["X", "O"]:
                        if x.count(i) == size :
                            print("Winner:", i)
                            value = False
                if value :
                    liste_check.remove(player_input)
                    if len(liste_check) == 0 :
                        print("No winner")
                        value = False
