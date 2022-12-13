import pygame as pg, sys, random


def check_bound(obj_rct, scr_rct):
    #範囲内:+1/範囲外:-1
    width, height = 1, 1
    if (obj_rct.left < scr_rct.left) or (obj_rct.right > scr_rct.right): #左右の画面範囲
        width = -1
    if (obj_rct.top < scr_rct.top) or (obj_rct.bottom > scr_rct.bottom): #上下の画面範囲
        height = -1
    return width, height

def main():
    #以降ゲーム処理
    clock = pg.time.Clock() #時間用オブジェクト
    vx, vy = 1, 1
    boomb_list = []
    #練習１
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバー表示
    scrn_sfc = pg.display.set_mode((1600, 900)) #Surfaceクラスのオブジェクトを生成
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    pgbg_rct = pgbg_sfc.get_rect()
    
    #練習３
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    
    
    count = 0 #フレーム数をカウントする
    #練習２
    while True:
        #以降繰り返し処理
        count += 1
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) #blit
        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
         
        #練習４
        key_dict = pg.key.get_pressed() #キーの辞書
        if key_dict[pg.K_UP]: tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]: tori_rct.centery += 1
        if key_dict[pg.K_LEFT]: tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT]: tori_rct.centerx += 1
        if key_dict[pg.K_r]: #Rキーを押下するとリセットする
            count = 0
            boomb_list.clear()

        #練習７
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dict[pg.K_UP]: tori_rct.centery += 1
            if key_dict[pg.K_DOWN]: tori_rct.centery -= 1
            if key_dict[pg.K_LEFT]: tori_rct.centerx += 1
            if key_dict[pg.K_RIGHT]: tori_rct.centerx -= 1  
        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        
        #練習6
        for bomb in boomb_list: 
            bomb[1].move_ip(bomb[2], bomb[3]) #vx, vyに従って移動
            scrn_sfc.blit(bomb[0], bomb[1])
            bomb[2] *= check_bound(bomb[1], scrn_rct)[0]
            bomb[3] *= check_bound(bomb[1], scrn_rct)[1]
                    
        if count%1000 == 1: #１秒ごとにボールを追加する
            if random.randint(1, 4) == 2: #一定確率で大きい爆弾
                boomb_sfc = pg.Surface((40, 40))#正方形空Surface
                boomb_sfc.set_colorkey(0, 0)#黒い部分を透明化
                pg.draw.circle(boomb_sfc, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (20, 20), 30) #色をランダムに決定する
            else:
                boomb_sfc = pg.Surface((20, 20))#正方形空Surface
                boomb_sfc.set_colorkey(0, 0)#黒い部分を透明化
                pg.draw.circle(boomb_sfc, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (10, 10), 10) #色をランダムに決定する
            boomb_rct = boomb_sfc.get_rect()
            boomb_rct.centerx = random.randint(1, scrn_rct.width) #範囲を1からにすることでバグ修正
            boomb_rct.centery = random.randint(1, scrn_rct.height) #範囲を1からにすることでバグ修正
            scrn_sfc.blit(boomb_sfc, boomb_rct) #blit
            if random.randint(1, 6) == 3: vx, vy = 2, 2 #20%の確率で速い爆弾が生まれる
            boomb_list.append([boomb_sfc, boomb_rct, vx, vy]) #爆弾のboomb_sfc, boomb_rct, vx, vyをリストで管理する
            vx, vy = 1, 1
        
        
        #練習８
        for boomb in boomb_list:
            if tori_rct.colliderect(boomb[1]):
                #こうかとんがいずれかの爆弾に当たった場合、while文を終了する
                return
        pg.display.update()
        clock.tick(1000) #1000fps
            

if __name__ == '__main__':
    pg.init() #pygameモジュールの初期化
    main() #main関数の呼び出し
    pg.quit() #pygameモジュール終了
    sys.exit() #プログラムの終了