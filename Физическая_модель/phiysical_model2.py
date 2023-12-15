import pygame
import random
RES = WIDHT, HEIGHT = 1300, 1000
FPS = 500
TILE = 4
W, H = WIDHT//TILE, HEIGHT//TILE


pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic sans MS', 30)
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

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:

                if click[0] ==1:
                    self.value_massage +=1
                    pygame.time.delay(70)

        pygame.draw.rect(surface, (203, 54, 58), (x, y, self.width, self.height))
        text = font.render(self.massage + f':{self.value_massage}', False, (100, 0, 0))
        surface.blit(text, (x, y))


Butt = Button(230, 60, (203, 54, 58), (13, 162, 58), "<Force_rad>", 45)
while go:
    surface.fill(pygame.Color("black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    rule(date, date, -3, -3, 70, 8, 65)
    rule(read, read, Butt.value_massage, 45, 70, 1, 200)
    rule(date, read, -Butt.value_massage, -75, 41, 7, 140)
    Butt.draw(850, 0)
    print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)