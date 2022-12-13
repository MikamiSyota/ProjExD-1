import pygame as pg, sys, random


def check_bound(obj_rct, scr_rct):
    #範囲内:+1/範囲外:-1
    width, height = 1, 1
    if (obj_rct.left < scr_rct.left) or (obj_rct.right > scr_rct.right):
        width = -1
    if (obj_rct.top < scr_rct.top) or (obj_rct.bottom > scr_rct.bottom):
        height = -1
    return [width, height]

def main():
    #以降ゲーム処理
    clock = pg.time.Clock() #時間用オブジェクト
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
    
    #練習5
    boomb_sfc = pg.Surface((20, 20))#正方形空Surface
    boomb_sfc.set_colorkey(0, 0)#黒い部分を透明化
    pg.draw.circle(boomb_sfc, (255, 0, 0), (10, 10), 10)
    boomb_rct = boomb_sfc.get_rect()
    boomb_rct.centerx = random.randint(0, scrn_rct.width)
    boomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(boomb_sfc, boomb_rct) #blit
    
    vx, vy = 1, 1
    #練習２
    while True:
        #以降繰り返し処理
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) #blit
        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
         
        #練習４
        key_dict = pg.key.get_pressed() #キーの辞書
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        
        #練習6
        boomb_rct.move_ip(vx, vy) #vx, vyに従って移動  
        scrn_sfc.blit(boomb_sfc, boomb_rct)
        vx *= check_bound(boomb_rct, scrn_rct)[0]
        vy *= check_bound(boomb_rct, scrn_rct)[1]
        pg.display.update()
        clock.tick(1000) #1000fps
            

if __name__ == '__main__':
    pg.init() #pygameモジュールの初期化
    main() #main関数の呼び出し
    pg.quit() #pygameモジュール終了
    sys.exit() #プログラムの終了