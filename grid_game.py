import os
import time
import random

class Grid(object):
    def __init__(self, n):
        self.n = n
        self.grid = []
        choices = [(0,random.randrange(0,n-1)),(random.randrange(0,n-1),0),(n-1, random.randrange(0,n-1)),(random.randrange(0,n-1), n-1)]
        self.goal = random.choice(choices) 
        self.start = random.choice(choices)
        while self.start == self.goal:
            self.start = random.choice(choices)
        self.myObstacles = []
        self.myRewards = []
        for i in range(n):
            
            for j in range(n):
                if random.random() >= 0.6  and (i,j) not in [self.start, self.goal]:
                    self.myObstacles.append((i,j))
                elif random.random() <= 0.2 and (i,j) not in [self.start, self.goal]:
                    self.myRewards.append((i,j))
        for i in range(n):
            temp = []
            for j in range(n):
                if (i,j) == self.start:
                    temp.append('Q')
                elif (i,j) == self.goal:
                    temp.append('G')
                elif (i,j) in self.myObstacles:
                    temp.append('#')
                elif (i,j) in self.myRewards:
                    reward = Reward(i,j, random.randrange(1,9))
                    temp.append(str(reward.value))
                else:
                    temp.append('.')
            self.grid.append(temp)
    
    

    def showGrid(self):
        for i in range(self.n):
            for j in range(self.n):
                print(f'{self.grid[i][j]} ', end='')
            print('')

    def transpose(self):
        self.grid = list(zip(*self.grid))
    
    def reverse_columns(self):
        for i in range(self.n):
            self.grid[i] = list(reversed(self.grid[i]))

    def rotateAnticlockwise(self):
        self.reverse_columns()
        self.transpose()
        self.grid = list(self.grid)
        for i in range(len(self.grid)):
            self.grid[i] = list(self.grid[i])
    
    def rotateClockwise(self):
        for i in range(3):
            self.rotateAnticlockwise()

class Player(object):
    def __init__(self, x, y, energy, n):
        self.x = x
        self.y = y
        self.pos = (x,y)
        self.energy = energy
        self.n = n

    def makeMove(self, s):
        
        if(s == 'U'):
            self.x = (self.x-1)%self.n
        elif(s == 'D'):
            self.x = (self.x+1)%self.n
        elif(s == 'L'):
            self.y = (self.y-1)%self.n
        elif(s == 'R'):
            self.y = (self.y+1)%self.n
        self.pos = (self.x, self.y)
        return self.pos


    def __str__(self):
        return 'O'

class Obstacle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Reward(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = random.randrange(1,9)
    def __str__(self):
        return str(self.value)


n=input('Enter the size of Grid: ')
n = int(n)
grid = Grid(n)
grid.showGrid()
player = Player(grid.start[0], grid.start[1], 2*n, n)


while(1):
    os.system('clear')
    print('Energy: '+str(player.energy))
    grid.showGrid()
    moves = input()
    moves = moves.upper()
    i = 0
    while(i < len(moves)):
        for j in range(int(moves[i+1])):
            if moves[i] in ['A', 'C']:
                if moves[i] is 'A':
                    ini = player.pos
                    grid.rotateAnticlockwise()
                    player.pos = (n-1-ini[1], ini[0])
                    player.x, player.y = player.pos[0], player.pos[1]                   
                else:
                    ini = player.pos
                    grid.rotateClockwise()
                    player.pos = (ini[1],n-1-ini[0])
                    player.x, player.y = player.pos[0], player.pos[1]                   
                player.energy -= n//3
                
            else:
                ini = player.pos
                pos = player.makeMove(moves[i])
                time.sleep(0.3)
                grid.grid[ini[0]][ini[1]],grid.grid[pos[0]][pos[1]] = grid.grid[pos[0]][pos[1]],grid.grid[ini[0]][ini[1]]                
                if grid.grid[ini[0]][ini[1]] == '#':
                    grid.grid[ini[0]][ini[1]] = '.'
                    player.energy -= 4*n
                elif grid.grid[ini[0]][ini[1]].isnumeric():
                    player.energy += n*int(grid.grid[ini[0]][ini[1]])
                    grid.grid[ini[0]][ini[1]] = '.'
                else:
                    player.energy -= 1
            time.sleep(0.3)
            os.system('clear')
            print('Energy: '+str(player.energy))
            grid.showGrid()
        i += 2
        
    
    
    if(player.pos == grid.goal):
        print("Won")
        exit()
    elif player.energy <= 0:
        print('lost')
        exit()    

    os.system('clear')