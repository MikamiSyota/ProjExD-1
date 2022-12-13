import pygame as pg, sys

def main():
    #以降ゲーム処理
    clock = pg.time.Clock() #時間用オブジェクト
    #練習１
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバー表示
    scrn_sfc = pg.display.set_mode((1600, 900)) #Surfaceクラスのオブジェクトを生成
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    pgbg_rct = pgbg_sfc.get_rect()
    
    clock.tick(1000) #1000fps
    
    #練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.update()
            

if __name__ == '__main__':
    pg.init() #pygameモジュールの初期化
    main() #main関数の呼び出し
    pg.quit() #pygameモジュール終了
    sys.exit() #プログラムの終了