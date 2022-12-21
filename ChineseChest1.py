import pygame


class Dots(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 55
        self.row = row
        self.col = col


class Chess(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("images/chess1.png"),(45,45))
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col        
        self.rect.x = 35
        self.rect.y = 35

        
        self.isback=True
        self.isclick=False
        self.size=7

    def isClicked(self):
        self.isclick=True
        self.image=pygame.surface((0,255,0))

    def notClicked(self):
        self.isclick=False
    





# region 呼叫物件

dots = [[0]*8 for i in range(4)]
chess = [[0]*8 for i in range(4)]

all_point = pygame.sprite.Group()

for i in range(4):
    for j in range(8):
        dots[i][j] = Dots(j, i)
        dots[i][j].rect.x += 53*j
        dots[i][j].rect.y += 48*i
        all_point.add(dots[i][j])

for i in range(4):
    for j in range(8):
        chess[i][j] = Chess(j, i)
        chess[i][j].row=i
        chess[i][j].col=j
        chess[i][j].rect.x += 53*j
        chess[i][j].rect.y += 48*i
        all_point.add(chess[i][j])



# endregion



# region 主程式


def main():

    pygame.init

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("象棋")
    background_img = pygame.image.load("images/board2.jpg")

    running = True
    clock = pygame.time.Clock()
    fps = 10

    running = True

    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




# region 背景畫面
        screen.fill((0, 222, 222))
        screen.blit(background_img, (0, 0))
        all_point.draw(screen)
        pygame.display.update()
# endregion

    pygame.quit()


if __name__ == '__main__':
    main()
# endregion
