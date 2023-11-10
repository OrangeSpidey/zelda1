from pygame import *

class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = image.load(file_name).convert()
    def get_image(self, x, y, width, height):

        image = Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey((0, 137, 255))

        return image


class GmSpr(sprite.Sprite):
    def __init__(self, sprimage, x, y, speed, sizeX, sizeY):
        sprite.Sprite.__init__(self)
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.image = transform.scale(image.load(sprimage), (sizeX, sizeY))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def res(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(sprite.Sprite):
    def __init__(self, x, y, speed):
        sprite_sheet = SpriteSheet('sheeet.png')
        self.walking_frames_down = []
        image = sprite_sheet.get_image(0, 0, 50, 50)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(0, 55, 55, 55)
        self.walking_frames_down.append(image)

        self.walking_frames_right = []
        image = sprite_sheet.get_image(165, 0, 55, 55)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(165, 55, 55, 55)
        self.walking_frames_right.append(image)

        self.walking_frames_up = []
        image = sprite_sheet.get_image(110, 0, 55, 55)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(110, 55, 55, 55)
        self.walking_frames_up.append(image)

        self.walking_frames_left = []
        image = sprite_sheet.get_image(55, 0, 55, 55)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(55, 55, 55, 55)
        self.walking_frames_left.append(image)
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.numb = 0
        self.anim = True
        self.image = self.walking_frames_down[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def upd(self):
        keyy = key.get_pressed()
        if (keyy[K_LEFT] and self.rect.x >= 10) or (keyy[K_a] and self.rect.x >= 10):
            self.rect.x -= self.speed
            self.numb += 0.2
            if self.numb >= len(self.walking_frames_left):
                self.numb = 0
            self.image = self.walking_frames_left[int(self.numb)]
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        if (keyy[K_RIGHT] and self.rect.x <= 690) or (keyy[K_d] and self.rect.x <= 690):
            self.rect.x += self.speed
            self.numb += 0.2
            if self.numb >= len(self.walking_frames_right):
                self.numb = 0
            self.image = self.walking_frames_right[int(self.numb)]
            self.right = True
            self.left = False
            self.up = False
            self.down = False
        if (keyy[K_UP] and self.rect.y >= 10) or (keyy[K_w] and self.rect.y >= 10):
            self.rect.y -= self.speed
            self.numb += 0.2
            if self.numb >= len(self.walking_frames_up):
                self.numb = 0
            self.image = self.walking_frames_up[int(self.numb)]
            self.up = True
            self.down = False
            self.left = False
            self.right = False

        if (keyy[K_DOWN] and self.rect.y <= 490) or (keyy[K_s] and self.rect.y <= 490):
            self.rect.y += self.speed
            self.numb += 0.2
            if self.numb >= len(self.walking_frames_down):
                self.numb = 0
            self.image = self.walking_frames_down[int(self.numb)]
            self.down = True
            self.up = False
            self.left = False
            self.right = False
    def res(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
tre = GmSpr('naf.png', 650, 0, 0, 50, 50)
tres = sprite.Group()
tres.add(tre)

bush1 = GmSpr('bushes.png', 60, 0, 0, 60, 160)
bush2 = GmSpr('bushes.png', 120, 0, 0, 60, 160)
bush3 = GmSpr('bushes.png', 60, 300, 0, 60, 160)
bush4 = GmSpr('bushes.png', 120, 300, 0, 60, 160)
bush5 = GmSpr('bushes.png', 180, -54, 0, 60, 160)
bush6 = GmSpr('bushes.png', 240, -54, 0, 60, 160)
bush7 = GmSpr('bushes.png', 300, -54, 0, 60, 160)
bush8 = GmSpr('bushes.png', 360, 0, 0, 60, 160)
bush9 = GmSpr('bushes.png', 420, 54, 0, 60, 160)
bush10 = GmSpr('bushes.png', 420, -107, 0, 60, 160)
bush11 = GmSpr('bushes.png', 480, 54, 0, 60, 160)
bush12 = GmSpr('bushes.png', 480, -107, 0, 60, 160)
bush13 = GmSpr('bushes.png', 540, 54, 0, 60, 160)
bush14 = GmSpr('bushes.png', 540, -107, 0, 60, 160)
bush15 = GmSpr('bushes.png', 600, 54, 0, 60, 160)
bush16 = GmSpr('bushes.png', 720, 0, 0, 60, 160)
bush17 = GmSpr('bushes.png', 720, 160, 0, 60, 160)
bush18 = GmSpr('bushes.png', 720, 320, 0, 60, 160)
bush19 = GmSpr('bushes.png', 720, 480, 0, 60, 160)
bush20 = GmSpr('bushes.png', 300, 300, 0, 60, 160)
bush21= GmSpr('bushes.png', 360, 300, 0, 60, 160)
bush22 = GmSpr('bushes.png', 480, 300, 0, 60, 160)
bush23= GmSpr('bushes.png', 600, 300, 0, 60, 160)
bush24 = GmSpr('bushes.png', 0, 524,  0, 60, 160)
bush25 = GmSpr('bushes.png', 60,524, 0, 60, 160)
bush26 = GmSpr('bushes.png', 120, 524,  0, 60, 160)
bush27 = GmSpr('bushes.png', 180, 524,  0, 60, 160)
bush28 = GmSpr('bushes.png', 240, 524,  0, 60, 160)
bush29 = GmSpr('bushes.png', 300, 524,  0, 60, 160)
bush30 = GmSpr('bushes.png', 360, 524,  0, 60, 160)
bush31 = GmSpr('bushes.png',420,  524, 0, 60, 160)
bush32 = GmSpr('bushes.png',480, 524, 0, 60, 160)
bush33 = GmSpr('bushes.png', 540, 524,  0, 60, 160)
bush34 = GmSpr('bushes.png',600,  524, 0, 60, 160)
bush35 = GmSpr('bushes.png',660, 524, 0, 60, 160)
bushes = sprite.Group()
bushes.add(bush1)
bushes.add(bush2)
bushes.add(bush3)
bushes.add(bush4)
bushes.add(bush5)
bushes.add(bush6)
bushes.add(bush7)
bushes.add(bush8)
bushes.add(bush9)
bushes.add(bush10)
bushes.add(bush11)
bushes.add(bush12)
bushes.add(bush13)
bushes.add(bush14)
bushes.add(bush15)
bushes.add(bush16)
bushes.add(bush17)
bushes.add(bush18)
bushes.add(bush19)
bushes.add(bush20)
bushes.add(bush21)
bushes.add(bush21)
bushes.add(bush23)
bushes.add(bush24)
bushes.add(bush25)
bushes.add(bush26)
bushes.add(bush27)
bushes.add(bush28)
bushes.add(bush29)
bushes.add(bush30)
bushes.add(bush31)
bushes.add(bush32)
bushes.add(bush33)
bushes.add(bush34)
bushes.add(bush35)


win = display.set_mode((800,600))
display.set_caption("The Legend Of Zelda")
pl = Player(10, 10, 3)

clock = time.Clock()
game = True
finish = False

font.init()
font1 = font.SysFont('Arial', 40)
wins = font1.render("YOU WIN", True, (200, 200, 0))
loses = font1.render("YOU LOSE", True, (200, 2, 0))
trs = font1.render("(поаккуратнее с лавой)", True, (0, 0, 0))

mixer.init()
mixer.music.load('Zelda.ogg')
mixer.music.play()

fires = mixer.Sound("z1.ogg")
sss = mixer.Sound("over.ogg")

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                pl.kick()
    if not finish:
        win.fill((247, 216, 165))
        pl.res()
        pl.upd()
        tre.res()
        bushes.draw(win)
        if sprite.spritecollide(pl, bushes, False):
            win.blit(loses, (300, 250))
            win.blit(trs, (225, 300))
            mixer.music.stop()
            sss.play()
            finish = True


        if sprite.spritecollide(pl, tres, False):
            win.blit(wins, (300, 250))
            mixer.music.stop()
            fires.play()
            finish = True
        display.update()
        clock.tick(60)

