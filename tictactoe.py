import sys 
import pygame
import numpy as np
from constants import *

#Pygame Setup and Screen
pygame.init() #initializing pygame
screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) #Creating the window for the game
pygame.display.set_caption('TIC TAC TOE v/s AI') 
screen.fill(BG_COLOR)

class Board:
    def __init__(self) -> None:
        self.squares = np.zeros((ROWS,COL))
        self.empty_sqrs = self.squares
        self.mark_sqrs = 0

    def final_state(self):
        '''
        
        '''

        #vertical wins
        for col in range (COL):
            if self.square[0][col] == self.square[1][col] == self.squares[2][col] != 0:
              return self.square[0][col]

        #Horizontal wins
        for row in range (ROWS):
            if self.square[0][row] == self.square[1][row] == self.squares[2][row] != 0:
              return self.square[row][0]

        #Desc Diagonal
        if self.square[0][0] == self.squares[1][1] == self.square[2][2] != 0:
            return self.square[1][1]

        #Asc Diagonal
        if self.square[2][0] == self.squares[1][1] == self.square[0][2] != 0:
            return self.square[1][1] 
        
        #No wins yet
        return 0   

    def mark_square(self,row,col,player):
        self.squares[row][col] = player
        self.marked_sqrs += 1
    
    def empty_square(self,row,col):
        return self.squares[row][col] == 0
    
    def get_empty_square(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COL):
                if self.empty_square(row,col):
                        empty_sqrs.append((row,col))
        return empty_sqrs
    
    def isfull(self):
        return self.mark_sqrs == 9
    
    def isempty(self):
        return self.mark_sqrs == 0


class Game:

    def __init__(self):
        self.board = Board()
        # self.ai = AI()
        self.player = 1 #player1 - zero, player2 - cross
        self.gamemode = 'PVP'
        self.running = True
        self.showlines()

    def showlines(self):
        #vertical lines
        pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HEIGHT),LINE_WIDTH)

        #Horizontal Lines
        pygame.draw.line(screen,LINE_COLOR,(0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(0,HEIGHT-SQSIZE),(WIDTH,HEIGHT-SQSIZE),LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1 #Changing to next player 

    def draw_fig(self,row,col):

        if self.player == 1:

            #Descending Line
            start_dec = (col*SQSIZE+OFFSET, row*SQSIZE+OFFSET)
            end_dec = (col*SQSIZE+SQSIZE-OFFSET, row*SQSIZE+SQSIZE-OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_dec,end_dec,CROSS_WIDTH)

            #Ascending Line
            start_asc = (col*SQSIZE+OFFSET, row*SQSIZE+SQSIZE-OFFSET)
            end_asc = (col*SQSIZE+SQSIZE-OFFSET, row*SQSIZE+OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_asc,end_asc,CROSS_WIDTH)


        elif self.player == 2:
           center = (col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2)
           pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH) 


def main():

    game = Game()
    board = game.board
    #mainloop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit() 
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Changed coordinates from pixels to rows and cols
                pos = event.pos
                row = pos[1]//SQSIZE
                col = pos[0]//SQSIZE

                if board.empty_square(row,col):
                    board.mark_square(row,col,game.player)
                    game.draw_fig(row,col)
                    game.next_turn()

        pygame.display.update()
main()