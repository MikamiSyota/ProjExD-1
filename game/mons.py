import pygame as pg
import sys
import random

startFlag = False

class Screen:
    #スクリーンの描画
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        
        
def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate       


class Enemy:
    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        

class My:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy
        self.dx = -0.01
        self.dy = -0.01
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen, speed):
        global startFlag
        if speed:
            self.rct.move_ip(self.vx, self.vy)
            yoko, tate = check_bound(self.rct, scr.rct)
            if abs(self.vx) >= abs(self.dx):
                self.vx += self.dx
                self.vy += self.dy
            else:
                startFlag = False
                if self.vx > 0:
                    self.vx = 10
                elif self.vx < 0:
                    self.vx = -10
                if self.vy > 0:
                    self.vy = 10
                elif self.vy < 0:
                    self.vy = -10
            
            self.vx *= yoko
            self.vy *= tate
            self.dx *= yoko
            self.dy *= tate

        self.blit(scr)

def main():
    global startFlag
    scr = Screen("モンスト", (1600,900), "fig/pg_bg.jpg") # Screenオブジェクトのインスタンス生成
    clock = pg.time.Clock()
        
    kkt = Enemy("fig/6.png", 2.0, (900,400)) # Enemyオブジェクトのインスタンス生成
    kkt.blit(scr)
    my = My((255,0,0), 10, (10, 10), scr)
    my.blit(scr)
    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #×ボタンでゲーム終了
                return
            
            if event.type == pg.MOUSEBUTTONDOWN and startFlag == False:
                startFlag = True
               
        kkt.blit(scr)
        if startFlag:
            my.update(scr, True)
        else:
            my.update(scr, False)
        pg.display.update()
        clock.tick(1000)
    
        
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()