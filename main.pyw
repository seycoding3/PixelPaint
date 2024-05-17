import pygame as pg
import platform,subprocess
pg.init()
ext = True
w = pg.display.set_mode((500,500))
pg.display.set_caption("PixelPaint")
platfo = platform.system()
if platfo == "Windows":
    imgw = pg.image.load("assets\\images\\pixel.png")
    pg.display.set_icon(imgw)
    print("Platform:Windows")
elif platfo == "Linux":
    imgl = pg.image.load("assets/images/pixel.png")
    pg.display.set_icon(imgl)
    print("Platform:Linux")
else:
    print("Error!")
    pg.quit()
    
    
    
while ext:
    for ev in pg.event.get():
        pg.display.update()
        if ev.type == pg.QUIT:
            ext = False
            pg.quit()
        elif ev.type == pg.MOUSEMOTION:
            if platfo == "Windows":
                imgw = pg.image.load("assets\\images\\pixel.png")
                print("Platform:Windows")
                w.blit(imgw,(ev.pos[0],ev.pos[1]))
            elif platfo == "Linux":
                imgl = pg.image.load("assets/images/pixel.png")
                w.blit(imgl,(ev.pos[0],ev.pos[1]))
                print("Platform:Linux")
                
                
            else:
                ext = False
                print("Error!")
                pg.quit()
                
                
              
    
   
    