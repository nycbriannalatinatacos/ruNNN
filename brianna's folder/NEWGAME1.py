#Linda Lin & Brianna Yournett
#BLGAMING
#There is a a chicken and swiper. Use Mouse to throw tomato at swiper and swiper only.
#if tomato hits the chicken, time will decrease and you will lose points in your total score. You have 60 seconds.

from gamelib import *

game = Game(800,600,"RuNNN",60)
bk  = Image("BLBK.jpg",game)
bk.resizeTo(800,600)
swiper = Image("swiper.jpg",game)
swiper.resizeBy(-80)
chicken = Image("chicken.jpg",game)
chicken.resizeBy(-50)

tomato= Image("tomato.gif",game)
mouse.visible = False

logo=Image("title.png",game)



while not game.over:
    game.processInput()

    bk.draw()
    swiper.draw( )
    chicken.draw( )
    logo.draw( )
   
    swiper.move(True)
    chicken.move(True)
    chicken.resizeBy(1)
    tomato.moveTo(mouse.x,mouse.y)
    tomato.resizeTo(200,150)
   
    if swiper.collidedWith(mouse) and mouse.LeftClick:
        swiper.resizeBy(-2)
        x = randint(swiper.width,game.width-swiper.width)
        y = randint(swiper.height,game.height-swiper.height)
        swiper.moveTo(x,y)
        swiper.speed += 2        
        game.score += 10

    if chicken.width >= 250:
        chicken.resizeTo(150,150) 
        x = randint(chicken.width,game.width-chicken.width)
        y = randint(chicken.height,game.height-chicken.height)
        chicken.moveTo(x,y)
        game.score += 10
    
    if chicken.collidedWith(mouse) and mouse.LeftButton:
        game.time -= 10

    if game.time <= 0:
        game.over = True
    game.displayTime(150,5)
    game.displayScore()
    game.update(30)
game.quit()


x = randint(chicken.width,game.width-chicken.width)
y = randint(chicken.height,game.height-chicken.height)
chicken.moveTo(x,y)
game.score += 10
if chicken.collidedWith(mouse) and mouse.LeftButton:
        game.time -= 10

if game.time <= 0:
    game.over = True
    game.displayTime(150,5)
    game.displayScore()
    game.update(30)
game.quit()


        
  


  
