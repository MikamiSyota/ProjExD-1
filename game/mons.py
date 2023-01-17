import pygame as pg
import sys
import os
import math


startFlag = False #ボールが停止しているかの判定
flag = False #連続で敵キャラに当たらないようにする


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
    第1引数：マイrect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    壁との当たり判定
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate       

#土生
def check_bound_enemy(obj_rct, enm_rct):
    """
    第1引数：マイrect
    第2引数：エネミーrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < enm_rct.left or enm_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < enm_rct.top or enm_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate     


class Enemy:
    #敵キャラの描画
    def __init__(self, img_path, ratio, xy, hp):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.hp = hp #ヒットポイント

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def hit(self):
        #ボールが当たった時ヒットポイントを-1する
        self.hp -= 1
        
    def return_hp(self):
        #ヒットポイントを返す
        return self.hp



class HealthBar: #HPバーの作成
    max_hp = 5 #敵キャラのHP
    def __init__(self,img_path, hxy):
        self.sfcs = [pg.image.load(img_path) for i in range(self.max_hp)]
        self.rcts = [self.sfcs[j].get_rect() for j in range(self.max_hp)]
        for x in range(self.max_hp): #敵キャラのHP分繰り返す
            if x == 0: #バーの描画が1回目であれば
                self.rcts[x].center = hxy
            else: #バーの描画が2回目以降であれば
                self.rcts[x].centerx = self.rcts[x -1].centerx + self.rcts[x -1].width #一個前の座標の中央のx値と横幅を加算する
                self.rcts[x].centery = self.rcts[x - 1].centery #立幅は変更しないためcenteyの値は1個前の値をそのまま使用


    def blit(self, scr:Screen):
        for z in range(self.max_hp):
            scr.sfc.blit(self.sfcs[z], self.rcts[z])

    def update(self, scr:Screen):
        for y in range(self.max_hp): #敵キャラの現在のHP分繰り返す
            self.blit(scr)


class My:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 700 #スタート位置
        self.rct.centery = 700 #スタート位置
        self.vx, self.vy = vxy
        self.dx = 0.996
        self.dy = self.dx * (900/1600) #減速率に画面の縦横比を考慮する
            
    def set_vxy(self, xy): #発射角度を設定
        self.vx, self.vy = xy
    
    def return_xy(self): #ボールの座標を返す
        return (self.rct.centerx, self.rct.centery)
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen, speed):
        #國井
        global startFlag
        if speed: #ボールが止まっていなかったら
            self.rct.move_ip(self.vx, self.vy)
            yoko, tate = check_bound(self.rct, scr.rct)
            if abs(self.vx) >= abs(self.dx):
                #減速させる
                self.vx*=self.dx
                self.vy*=self.dx
            else:
                startFlag = False
            self.vx *= yoko
            self.vy *= tate
        self.blit(scr)
            
    def update2(self, enm:Enemy, speed):
        global startFlag
        if speed:
            self.rct.move_ip(self.vx, self.vy)
            yoko, tate = check_bound(self.rct, enm.rct)
            if abs(self.vx) >= abs(self.dx):
                self.vx *= self.dx
                self.vy *= self.dy
            else:
                startFlag = False
            self.vx *= yoko
            self.vy *= tate
            self.dx *= yoko
            self.dy *= tate
    
        self.blit(enm)
        

#中島     
def delection(mouse, my): #発射角度の設定
    dx = abs(mouse[0]-my[0]) #x座標の差
    dy = abs(mouse[1]-my[1]) #y座標の差
    res = dx^2 + dy^2 #斜めの距離
    res = math.sqrt(res) 
    x = dx/res #比率を求める
    y = dy/res #比率を求める
    if mouse[0] <= my[0]:#マウス座標がボールより小さいとき
        x *= -1 
    if mouse[1] <= my[1]:#マウス座標がボールより小さいとき
        y *= -1
    return (x, y)

#三上
# 音楽
main_dir = os.path.split(os.path.abspath(__file__))[0]
def music():
    if pg.mixer:
        music = os.path.join(main_dir, "../fig", "monst_bgm.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

#三上
# ゲームクリアの処理
def game_clear():
    #ゲームクリア時に画像を出力する処理
    pg.display.set_caption("こうかとん、撃破。")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    img_sfc = pg.image.load("fig/game_clear.jpg")
    img_sfc = pg.transform.scale(img_sfc, (1600, 900))
    img_rct = img_sfc.get_rect()
    scrn_sfc.blit(img_sfc, img_rct)
    pg.display.update()
    pg.time.wait(2000)


def main():
    global startFlag, flag
    start_x = 10
    start_y = 10

    scr = Screen("モンスタ", (1600,900), "fig/pg_bg.jpg") # Screenオブジェクトのインスタンス生成
    clock = pg.time.Clock()
    kkt = Enemy("fig/6.png", 2.0, (900,400), 5) # Enemyオブジェクトのインスタンス生成
    kkt.blit(scr)
    my = My((255,0,0), 25, (start_x, start_y), scr) #Myオブジェクトのインスタンス生成
    my.blit(scr)
    hpbar = HealthBar("game/hp_bar.png", (100, 10)) #HPbarオブジェクトのインスタンス生成
    hpbar.blit(scr)
    
    # 音楽関数の実行
    music()

    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #×ボタンでゲーム終了
                return
            
            if event.type == pg.MOUSEBUTTONDOWN and startFlag == False:
                mouse = pg.mouse.get_pos()#マウス座標の取得
                my_xy = my.return_xy()
                delection_xy = delection(mouse, my_xy)
                my.set_vxy(delection_xy)
                startFlag = True
                   
        kkt.blit(scr)
        
        if startFlag:
            my.update(scr, True)
        else:
            my.update(scr, False)
            
        if kkt.rct.colliderect(my.rct) and  not flag:
            kkt.hit()#hpを減らす
            HealthBar.max_hp -= 1
            if startFlag:
                my.update2(kkt, True)
            else:
                my.update2(kkt, False)
            flag = True
 
        if not kkt.rct.colliderect(my.rct):
            #flagをfalseに戻す
            flag = False

        if kkt.return_hp() > 0: #敵キャラのHPが0より大きければ
            hpbar.update(scr) #HPバーの更新

        else:
            #hpが0になったらゲームを終了する
            game_clear()
            return
        
        pg.display.update()
        clock.tick(1000)    
        
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()