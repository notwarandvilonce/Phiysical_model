import sys

import pygame
import random
RES = WIDHT, HEIGHT = 1300, 1000
FPS = 500
TILE = 4
W, H = WIDHT//TILE, HEIGHT//TILE


pygame.init()
surface = pygame.display.set_mode(RES)
#screen = pygame.display.set_caption()

clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic sans MS', 22)
font2 = pygame.font.SysFont('Comic sans MS', 32)
font3 = pygame.font.SysFont('Comic sans MS', 92)
go = True

date = [[random.randint(0, WIDHT), random.randint(0, HEIGHT), 0, 0, 0, 0, (255, 190, 0, 200) ] for i in range(200)]
read = [[random.randint(0, WIDHT), random.randint(0, HEIGHT), 0, 0, 0, 0, (255, 90, 90, 200) ] for i in range(70)]


def rule(L, D, k, k2, r1, r2, R):
    dt = 0.05
    ceil = 20

    for i in range(len(L)):
        L[i][4] =0
        L[i][5]=0

        if L[i][0] <0 and L[i][2]<0:
            L[i][2] *= -1
            L[i][0] += ceil
        if L[i][1] <0 and L[i][3]<0:
            L[i][3] *= -1
            L[i][1] += ceil
        if L[i][0] > WIDHT and L[i][2]>0:
            L[i][2] *= -1
            L[i][0]-=ceil
        if L[i][1] > HEIGHT and L[i][3]>0:
            L[i][3] *= -1
            L[i][1] -=ceil

    if D != L:
        for i in range(len(D)):
            D[i][4] =0
            D[i][5]=0

            if D[i][0] <0 and D[i][2]<0:
                D[i][2] *= -1
                D[i][0] += ceil
            if D[i][1] <0 and D[i][3]<0:
                D[i][3] *= -1
                D[i][1] += ceil
            if D[i][0] > WIDHT and D[i][2]>0:
                D[i][2] *= -1
                D[i][0] -=ceil
            if D[i][1] > HEIGHT and D[i][3]>0:
                D[i][3] *= -1
                D[i][1] -= ceil

    for i in range(len(L)):

        for j in range(len(D)):
            x = L[i][0] - D[j][0]
            y = L[i][1] - D[j][1]
            d = (x*x + y*y)**0.5

            if j != i and x !=0 and y!=0 and d <R :
                L[i][4] += -k*x/d
                L[i][5] += -k * y/d
                D[j][4] += k2 * x /d
                D[j][5] += k2 * y /d

                if d < r1 and d > r2 :
                    L[i][2] = (L[i][2] - (L[i][2] + D[j][2])/2)/1.1 + (L[i][2] + D[j][2])/2
                    D[j][2] = (D[j][2] - (L[i][2] + D[j][2])/2)/1.1 + (L[i][2] + D[j][2])/2
                    L[i][3] = (L[i][3] - (L[i][3] + D[j][3]) / 2) / 1.1 + (L[i][3] + D[j][3]) / 2
                    D[j][3] = (D[j][3] - (L[i][3] + D[j][3]) / 2) / 1.1 + (L[i][3] + D[j][3]) / 2


    for i in range(len(L)):
        dx = L[i][2]*dt
        dy = L[i][3]*dt
        dvx = L[i][4]*dt
        dvy = L[i][5]*dt

        L[i][2] = (dvx + L[i][2])
        L[i][3] = (dvy + L[i][3])
        L[i][0] = (dx + L[i][0])
        L[i][1] = (dy + L[i][1])
        pygame.draw.rect(surface, pygame.Color(L[i][6]), (L[i][0], L[i][1], TILE, TILE))

    for i in range(len(D)):
        dx = D[i][2]*dt
        dy = D[i][3]*dt
        dvx = D[i][4]*dt
        dvy = D[i][5]*dt

        D[i][2] = (dvx + D[i][2])
        D[i][3] = (dvy + D[i][3])
        D[i][0] = (dx + D[i][0])
        D[i][1] = (dy + D[i][1])
        pygame.draw.rect(surface, pygame.Color(D[i][6]), (D[i][0], D[i][1], TILE, TILE))


class Button:
    def __init__(self, width, heigth, on_color, off_color, massage, value_massege):
        self.width = width
        self.height = heigth
        self.on_color = on_color
        self.off_color = off_color
        self.massage = massage
        self.value_massage = value_massege

    def draw(self, x, y,  action= None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if y < mouse[1] < y + self.height:
            if x + self.width*0.5  < mouse[0] < x + self.width:

                pygame.draw.rect(surface, self.off_color, (x, y, self.width, self.height))
                pygame.draw.rect(surface, self.on_color, (x + self.width*0.5, y, self.width*0.5 , self.height))
                text = font.render(self.massage + f':{self.value_massage}', False, (100, 0, 0))
                surface.blit(text, (x, y))

                if click[0] ==1:
                    self.value_massage +=1
                    pygame.time.delay(70)

            elif x  < mouse[0] < x + self.width*0.5:
                pygame.draw.rect(surface, self.off_color, (x, y, self.width, self.height))
                pygame.draw.rect(surface, self.on_color, (x, y, self.width*0.5, self.height))
                text = font.render(self.massage + f':{self.value_massage}', False, (100, 0, 0))
                surface.blit(text, (x, y))

                if click[0] ==1:
                    self.value_massage -=1
                    pygame.time.delay(70)

            else:
                pygame.draw.rect(surface, self.off_color, (x, y, self.width, self.height))
                text = font.render(self.massage + f':{self.value_massage}', False, (100, 0, 0))
                surface.blit(text, (x, y))


        else:

            pygame.draw.rect(surface, self.off_color, (x, y, self.width, self.height))
            text = font.render(self.massage + f':{self.value_massage}', False, (100, 0, 0))
            surface.blit(text, (x, y))


class Button_2:
    def __init__(self, width, heigth, on_color, off_color, massage):
        self.width = width
        self.height = heigth
        self.on_color = on_color
        self.off_color = off_color
        self.massage = massage

    def draw(self, x, y, X, x1, Y, y1, Z, z, H, h, G, g, F, f):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if y < mouse[1] < y + self.height:
            if x   < mouse[0] < x + self.width:

                pygame.draw.rect(surface, self.off_color, (x, y, self.width, self.height))

                text = font2.render(self.massage , False, (100, 0, 0))
                surface.blit(text, (x, y))

                if click[0] ==1:
                    X.value_massage = x1
                    Y.value_massage = y1
                    Z.value_massage = z
                    H.value_massage = h
                    G.value_massage = g
                    F.value_massage = f

                    pygame.time.delay(70)

            else:

                text = font2.render(self.massage , False, (200, 200, 200))
                surface.blit(text, (x, y))

        else:

            text = font2.render(self.massage , False, (200, 200, 200))
            surface.blit(text, (x, y))


class Button_FPS:
    def __init__(self, width, heigth,  massage, value, f):
        self.width = width
        self.height = heigth
        self.value = value
        self.massage = massage
        self.f = f
    def draw(self, x, y ):
        if self.value == 40:
            self.value =0
            self.f = clock.get_fps()//1

        self.value +=1
        text = font2.render(self.massage + ":" +f':{self.f}', False, (200, 200, 200))
        surface.blit(text, (x, y))

class Button_3:
    def __init__(self, width, heigth, on_color, off_color, massage, action):
        self.width = width
        self.height = heigth
        self.on_color = on_color
        self.off_color = off_color
        self.massage = massage
        self.action = action

    def draw(self, x, y):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if y < mouse[1] < y + self.height:
            if x   < mouse[0] < x + self.width:

                pygame.draw.rect(surface, self.off_color, (x, y, self.width, self.height))

                text = font3.render(self.massage , False, (100, 0, 0))
                surface.blit(text, (x, y))

                if click[0] ==1:
                    self.action = False
                    pygame.time.delay(70)

            else:

                text = font3.render(self.massage , False, (200, 20, 20))
                surface.blit(text, (x, y))

        else:

            text = font3.render(self.massage , False, (200, 20, 20))
            surface.blit(text, (x, y))


Butt9 = Button_3(180, 60, (200, 154, 158), (230, 222, 158), "Start", True)

Butt = Button(280, 50, (200, 154, 188), (230, 222, 158), "<   Force_rad   >", 45)
Butt2 = Button(280, 50, (200, 154, 158), (230, 222, 158), "<Force_yellow-rad>", 45)
Butt3 = Button(280, 50, (200, 154, 158), (230, 222, 158), "<Force_yellow-yellow>", -3)

Butt4 = Button(280, 50, (200, 154, 158), (230, 222, 158), "<Radius_yellow-yellow>", 65)
Butt5 = Button(280, 50, (200, 154, 158), (230, 222, 158), "<  Radius_rad-rad  >", 200)
Butt6 = Button(280, 50, (200, 154, 158), (230, 222, 158), "< Radius_yellow-rad >", 140)

Butt7 = Button_2(180, 60, (200, 154, 158), (230, 222, 158), "< Update >")

Butt8 = Button_FPS(200, 50, "FPS", 0, 0)


def intro():
    global Butt9
    went = True
    img = pygame.image.load('C:\pythonProject5\Физическая_модель\molekyle.png')
    font3 = pygame.font.SysFont("stxingkai", 210)
    text_welcome = font3.render("Welcome!", True, (220, 20, 20))

    while went:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        surface.blit(pygame.transform.scale(img, [1400, 1000]), [10, 10])
        surface.blit(text_welcome, (300, 500))

        Butt9.draw(500, 100)
        pygame.display.update()
        if Butt9.action == False:
            went = False


intro()



while go:
    surface.fill(pygame.Color("black"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False

    rule(date, date, Butt3.value_massage, -3, 70, 8, Butt4.value_massage)
    rule(read, read, Butt.value_massage, 45, 70, 1, Butt5.value_massage)
    rule(date, read, -Butt2.value_massage, -75, 41, 7, Butt6.value_massage)

    Butt.draw(1000, 0)
    Butt2.draw(1000, 50)
    Butt3.draw(1000, 100)

    Butt4.draw(1000, 150)
    Butt5.draw(1000, 200)
    Butt6.draw(1000, 250)

    Butt7.draw(1100, 800, Butt, 45, Butt2, 45, Butt3, -3, Butt4, 65, Butt5, 200, Butt6, 140)

    Butt8.draw(10, 10)
    print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)