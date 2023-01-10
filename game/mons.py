import pygame as pg
import sys


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
        

def main():
    scr = Screen("モンスト", (1600,900), "fig/pg_bg.jpg") # Screenオブジェクトのインスタンス生成
    clock = pg.time.Clock()
    
    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #×ボタンでゲーム終了
                return
            
        pg.display.update()
        clock.tick(1000)
    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()