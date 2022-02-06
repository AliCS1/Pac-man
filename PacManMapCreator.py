import pygame
import time


pygame.init()


Screen = pygame.display.set_mode((1280,640))


class Tile:
    def __init__(self,x,y):
        self.width = 40
        self.x = x
        self.y = y
        self.Wall = 1
    def Draw(self):
        if ((self.x+self.y)%2) == 0:
            pygame.draw.rect(Screen,(235, 213, 52),(self.x*self.width,self.y*self.width,self.width,self.width))
            if self.Wall == 1:
                pygame.draw.rect(Screen,(52, 125, 235),(self.x*self.width+6,self.y*self.width+6,self.width-12,self.width-12))
        else:
            pygame.draw.rect(Screen,(52, 235, 174),(self.x*self.width,self.y*self.width,self.width,self.width))
            if self.Wall == 1:
                pygame.draw.rect(Screen,(52, 125, 235),(self.x*self.width+6,self.y*self.width+6,self.width-12,self.width-12))

    def Click(self):
        self.Wall = self.Wall * -1

tile = Tile(5,4)
#BOARD = [[Tile(j,i) for i in range(0,9)] for j in range(0,33)]
BOARD = [[Tile(i,j) for i in range(0,32)] for j in range(0,16)]
#print("X value is :",BOARD[4][1].x)
#print("Y value is :",BOARD[4][1].y)

#print(BOARD)

#32x8

def PRINTLIST():
    x = 0
    y = 0
    Printer = ""
    Printer = Printer + "["
    for i in range(0,16):
        Printer = Printer + "["
        for j in range(0,32):
            Printer = Printer + "Tile"
            Printer = Printer + "("
            Printer = Printer + str(BOARD[i][j].x)
            Printer = Printer + ","
            Printer = Printer + str(BOARD[i][j].y)
            x = x + 1
            Printer = Printer + ","
            if BOARD[i][j].Wall == -1:
                Printer = Printer + "0"
            else:
                Printer = Printer + "1"
            Printer = Printer + ")"
            if x < 32:
                Printer = Printer + ","
            else:
                x = 0
        Printer = Printer + "]"
        y = y + 1
        if y < 16:
            Printer = Printer + ","
        else:
            y = 0
    Printer = Printer + "]"
    print(Printer)
POS = (-1,-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                POS = pygame.mouse.get_pos()
            for i in range(0,16):
                for j in range(0,32):
                    BOARD[i][j].Draw()
                    if BOARD[i][j].x*BOARD[i][j].width < POS[0] and BOARD[i][j].x*BOARD[i][j].width+BOARD[i][j].width > POS[0] and BOARD[i][j].y*BOARD[i][j].width < POS[1] and BOARD[i][j].y*BOARD[i][j].width+BOARD[i][j].width > POS[1]:
                        BOARD[i][j].Click()
                        POS = (-1,-1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    PRINTLIST()
            pygame.display.update()
            #print(event)
