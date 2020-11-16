import os
import re
from board import SnakeLadderBoard
from player import PlayerList
from player import checkSnakeOrLadder

if __name__ == "__main__":
    path=os.getcwd()+"\\testcases\\"
    
    b = SnakeLadderBoard()
    c = PlayerList()
    m = input('Enter no of players(Default 4): ')
    dices=input('To use 2 dices press\'y\' or Any key to 1 dice (Default \'n\'):')
    if dices=='y':
        c.noOfDices=2
    if m=='':
        c.noOfPlayers()
    else:
        m=int(m)
        c.noOfPlayers(m)
    m=c.playersNo
    nt = False
    while nt == False:
        if m == 2 or m == 3 or m == 4:
            nt = True
            break
        else:
            m = int(input('Min players required-2 & Max players required-4'))
    if m == 2:
        f = open(path+"2players.txt", "r")
    elif m == 3:
        f = open(path+"3players.txt", "r")
    else:
        f = open(path+"4players.txt", "r")

    lines = f.readlines()
    s = int(lines[0])
    print(f'Be careful with snakes, There are {s} snakes at :')
    for i in range(1, s+1):
        sn = list(map(int, lines[i].split()))
        sh = sn[0]
        st = sn[1]
        print(f'Snake {i}, head-{sh} & tail-{st}')
        b.insertSnake(sh, st)
    print()
    l = int(lines[s+1])
    print(f'Hit the jackpot with Ladders, There are {l} Ladders at :')
    for i in range(s+2, s+l+2):
        ln = list(map(int, lines[i].split()))
        lh = ln[0]
        lt = ln[1]
        print(f'Ladder {s+2-i}, tail-{lt} & head-{lt}')
        b.insertLadder(lh, lt)
    print()
    npc = 0
    fp = open(path+"defaultplayers.txt", "r")
    names = fp.readlines()
    for i in range(m):
        pn1=names[i]
        pn1 = re.sub('\s+', '', pn1)
        pn = input(f'Enter Player name(Default {pn1}): ')
        if pn=='':
            pn=names[i]
        pn = re.sub('\s+', '', pn)
        npc += 1
        c.addPlayer(pn, npc)
    fp.close()
    nl = b.displayBoard()
    f.close()
    fd1 = open(path+"outboard.txt", "w")
    fd1.write(nl)
    fd1.close()
    fd2 = open(path+"outboard.txt", "r")
    for ln in fd2:
        print(ln)
    fd2.close()
    d = input('Press Enter to roll a dice')
    while d != "exit":
        pptr, ppos = c.gameTurn()
        den = b.snakeLadderCells[ppos]
        checkSnakeOrLadder(pptr, ppos, den[0], den[1])
        d = input()
