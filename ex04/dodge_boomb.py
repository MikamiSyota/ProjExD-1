import pygame as pg, sys

def main():
    #以降ゲーム処理
    clock = pg.time.Clock() #時間用オブジェクト
    #練習１
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバー表示
    scrn_sfc = pg.display.set_mode((1600, 900)) #Surfaceクラスのオブジェクトを生成
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    pgbg_rct = pgbg_sfc.get_rect()
    
    #練習３
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    
    #練習２
    while True:
        #以降繰り返し処理
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) #blit
        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
         
        #練習４
        key_dict = pg.key.get_pressed()
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc, tori_rct) #blit
        
        pg.display.update()
        clock.tick(1000) #1000fps
            

if __name__ == '__main__':
    pg.init() #pygameモジュールの初期化
    main() #main関数の呼び出し
    pg.quit() #pygameモジュール終了
    sys.exit() #プログラムの終了