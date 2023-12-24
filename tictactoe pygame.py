import pygame


class tictactoe:
    def __init__(self):
        pygame.init()
        
        
        

        self.start = False
        self.turn = "playero"
        self.font1 = pygame.font.SysFont("Arial", 24)
        self.font2 = pygame.font.SysFont("Arial", 50)
        self.font3 = pygame.font.SysFont("Arial", 17)
        starttext = self.font2.render("Press Enter to start the game", True, (0, 0, 0))
        starttext2 = self.font1.render("Pick places with mouse", True, (0, 0, 0))
        starttext3 = self.font1.render("Player o is 1st player", True, (0, 0, 0))
        starttext4 = self.font1.render("Player x is 2nd player", True, (0, 0, 0))
        self.slots = [(225, 225), (400, 225), (575, 225), (225, 400), (400, 400), (575, 400), (225, 575), (400, 575), (575, 575)]
        self.areas_x = [(225, 150), ]
        self.numbers = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

        win1 = [(225, 225), (400, 225), (575, 225)]
        win2 = [(225, 400), (400, 400), (575, 400)]
        win3 = [(225, 575), (400, 575), (575, 575)]
        win4 = [(225, 225), (400, 400), (575, 575)]
        win5 = [(575, 225), (400, 400), (225, 575)]
        win6 = [(225, 225), (225, 400), (225, 575)]
        win7 = [(400, 225), (400, 400), (400, 575)]
        win8 = [(575, 225), (575, 400), (575, 575)]
        self.wins = [win1, win2, win3, win4, win5, win6, win7, win8]


        sqr1 = pygame.Rect(150, 150, 130, 130)
        sqr3 = pygame.Rect(520, 150, 130, 130)
        sqr2 = pygame.Rect(325, 150, 150, 130)
        sqr4 = pygame.Rect(150, 320, 130, 160)
        sqr6 = pygame.Rect(520, 320, 130, 160)
        sqr5 = pygame.Rect(325, 320, 150, 160)
        sqr7 = pygame.Rect(150, 520, 130, 130)
        sqr9 = pygame.Rect(520, 520, 130, 130)
        sqr8 = pygame.Rect(325, 520, 150, 130)

        self.squares = [(sqr1, 0), (sqr2, 1), (sqr3, 2), (sqr4, 3), (sqr5, 4), (sqr6, 5), (sqr7, 6), (sqr8, 7), (sqr9, 8)]

        

        self.disp = pygame.display.set_mode((800, 800)) 
        pygame.display.set_caption("tic tac toe")

        while self.start == False:
            self.disp.fill((120, 120, 120))
            self.disp.blit(starttext, (70, 160))
            self.disp.blit(starttext2, (70, 300))
            self.disp.blit(starttext3, (70, 330))
            self.disp.blit(starttext4, (70, 360))
            
            
            
            pygame.display.flip()
 
            for tapahtuma in pygame.event.get():
                    if tapahtuma.type == pygame.KEYDOWN:
                        if tapahtuma.key == pygame.K_RETURN:
                            self.start = True
                            break
                    if tapahtuma.type == pygame.QUIT:
                        exit()
    
        self.gameboard()


    def gameboard(self):
        self.o = []
        self.x = []

        while True:
            self.disp.fill((120, 120, 120))
            pygame.draw.line(self.disp, (0, 0, 0), (500, 150), (500, 650), 8)
            pygame.draw.line(self.disp, (0, 0, 0), (300, 150), (300, 650), 8)
            pygame.draw.line(self.disp, (0, 0, 0), (150, 500), (650, 500), 8)
            pygame.draw.line(self.disp, (0, 0, 0), (150, 300), (650, 300), 8)

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i in self.squares:
                        if i[0].collidepoint(pos):
                            if self.turn == "playero":
                                    if not self.slots[i[1]] in self.x:
                                        self.o.append(self.slots[i[1]])
                                        self.turn = "playerx"

                            elif self.turn == "playerx": 
                                if not self.slots[i[1]] in self.o:
                                    self.x.append(self.slots[i[1]])
                                    self.turn = "playero"    
                    
               
            if self.o != []:
                for i in self.o:
                    self.circle(i)
            if self.x != []:
                for i in self.x:
                    self.cross(i)
            
            pygame.display.flip()
            if len(self.o) >= 5:
                    pygame.time.delay(4000), tictactoe()
            self.winning()

    def winning(self):
        win_o = self.font2.render("Player o wins!", True, (255, 0, 0))
        win_x = self.font2.render("Player x wins!", True, (0, 0, 0))
        for i in self.wins:
            if i[0] in self.o:
                if i[1] in self.o:
                    if i[2] in self.o:
                        self.disp.blit(win_o, (260, 70))
                        pygame.display.flip()
                        pygame.time.delay(4000), tictactoe()
            if i[0] in self.x:
                if i[1] in self.x:
                    if i[2] in self.x:
                        self.disp.blit(win_x, (260, 70))
                        pygame.display.flip()
                        pygame.time.delay(4000), tictactoe()
    
    def cross(self, coordinates: tuple):
        pygame.draw.line(self.disp, (0, 0, 0), (coordinates[0]-50, coordinates[1]-50), (coordinates[0]+50, coordinates[1]+50), 12)
        pygame.draw.line(self.disp, (0, 0, 0), (coordinates[0]+50, coordinates[1]-50), (coordinates[0]-50, coordinates[1]+50), 12)
        

    def circle(self, coordinates: tuple):
        pygame.draw.circle(self.disp, (255, 0, 0), coordinates,  60, 8)


tictactoe()