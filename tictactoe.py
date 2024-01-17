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
        

    def mark_square(self,row,col,player):
        self.squares[row][col] = player

    
    def empty_square(self,row,col):
        return self.squares[row][col] == 0

class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1 #player1 - zero, player2 - cross
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