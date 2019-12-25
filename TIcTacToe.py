from itertools import combinations

# for checking if the player as won
win = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [3, 5, 7]]
fin = 0
count = 9


class Board:
    def __init__(self, pos = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}):
        self.pos = pos
    def dis(self): # prints the board in the output
        print("     |     |     ")
        print("  {0}  |  {1}  |  {2}  ".format(self.pos[7], self.pos[8], self.pos[9]))
        print("_____|_____|_____")
        print("     |     |     ")
        print("  {0}  |  {1}  |  {2}  ".format(self.pos[4], self.pos[5], self.pos[6]))
        print("_____|_____|_____")
        print("     |     |     ")
        print("  {0}  |  {1}  |  {2}  ".format(self.pos[1], self.pos[2], self.pos[3]))
        print("     |     |     ")

    def reset(self):
        self.pos = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

board = Board()
class Player1():
    def __init__(self, marker, mar_pos = [], score = 0):
        self.marker = marker
        self.mar_pos = mar_pos
        self.score = score

    def turn(self, ind):
        if board.pos[ind] != " ":
            print("Positon already taken. Turn skipped")
        else:
            board.pos[ind] = self.marker
            self.mar_pos.append(ind)

    def reset(self):
        self.mar_pos = []


class Player2():
    def __init__(self, marker, mar_pos = [], score = 0):
        self.marker = marker
        self.mar_pos = mar_pos
        self.score = score

    def turn(self, ind):
        if board.pos[ind] != " ":
            print("Postion already taken. Turn skipped")
        else:
            board.pos[ind] = self.marker
            self.mar_pos.append(ind)

    def reset(self):
        self.mar_pos = []

def win_check(lis):
    per = list(combinations(lis, 3))
    for i in per:
        for j in win:
            if set(i) == set(j):
                fin = 1
                return True
    return False

n1 = input(("Enter name of player 1: "))
n1n = n1
n1m = input("Enter marker of player 1: ")
n1 = Player1(n1m)

n2 = input(("Enter name of player 2: "))
n2n = n2
n2m = input("Enter marker of player 2: ")
n2 = Player2(n2m)

cont = 0
while cont == 0:
    count = 9
    board.reset()
    n1.reset()
    n2.reset()
    print("{} will go first".format(n1n))
    board.dis()
    while (fin == 0):
        try:
            pos = int(input("Enter your position {}: ".format(n1n)))
            n1.turn(pos)
            count -= 1
            if len(n1.mar_pos) >= 3:
                res = win_check(n1.mar_pos)
                if res:
                    board.dis()
                    print("Congratulations! {} has won this game!!!".format(n1n))
                    n1.score += 1
                    break
            print("\n" * 5)
            board.dis()
            if (count == 0):
                print("Game is drawn")
                print("You both are great!")
                fin = 1
                break
            pos = int(input("Enter your position {}: ".format(n2n)))
            n2.turn(pos)
            count -= 1
            if len(n2.mar_pos) >= 3:
                if win_check(n2.mar_pos):
                    board.dis()
                    print("Congratulations! {} has won this game!!!".format(n2n))
                    n2.score += 1
                    break

            print("\n" * 5)
            board.dis()
        except:
            print("INVALID")
    print("After this match, the scores are: \n{} : {}\n{} : {}".format(n1n, n1.score, n2n, n2.score))
    cont = int(input("Do you want to play another game? \nEnter 0 to play: "))
