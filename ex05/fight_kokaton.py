import pygame as pg
import random
import sys

bkd_list = [] # 爆弾のインスタンスを保存するリスト
frame_count = 0 # フレーム数をカウントする変数

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


class Bird:
    #こうかとんの描画
    key_delta = {
        #各キーに対応する移動方向
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:
    #爆弾の描画
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


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


def main():
    global frame_count, bkd_list
    clock =pg.time.Clock()

    # 練習１
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg") # Screenオブジェクトのインスタンス生成

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900,400)) # Birdオブジェクトのインスタンス生成
    kkt.update(scr) 
    
    # 練習２
    while True:        
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #×ボタンでゲーム終了
                return
            
        kkt.update(scr)
        if frame_count%5000 == 0:
            # 5秒経過ごとにで爆弾のインスタンスを増やす
            bkd_list.append(Bomb((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 10, (+1, +1), scr))
            # 爆弾の色をランダムに設定
        for i in bkd_list:
            i.update(scr) # 爆弾のアップデート
            if kkt.rct.colliderect(i.rct): #すべての爆弾に当たり判定を適応
                #爆弾が当たったらゲーム終了
                return
            
        pg.display.update()
        clock.tick(1000)
        frame_count += 1 # フレーム数を1増やす


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()