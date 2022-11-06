import math, copy, random
from cmu_112_graphics import *

def appStarted(app):
    app.ballPy = 0
    app.ballSpeed = app.width//40
    app.ballPos = 0
    app.timerDelay = 20
    app.timePassed = 0
    app.pitch = True
    app.ratio = app.height/app.width
    app.bat = False
    app.batHeight = app.height//2
    app.expo = 2
    app.hit = 0
    app.isHit = False
    app.score = 0
    app.strikes = 0
    app.balls = 0
    app.beforeImage = app.loadImage("before_pitch.png")
    app.afterImage = app.loadImage("after_pitch.png")
    app.catcher = app.loadImage("catcher.png")
    app.catcher = app.scaleImage(app.catcher, 1/2)
    app.gameOver = False

def keyPressed(app, event):
    if event.key == "p":
        app.pitch = False
    if event.key == "r":
        app.gameOver = False
        appStarted(app)
    

def mouseMoved(app, event):
    if app.bat == True:
        return
    else:
        app.batHeight = event.y

def mousePressed(app,event):
    if event.x != 0:
        app.bat = True
        app.batHeight = event.y

def timerFired(app):
    if app.gameOver == True:
        return
    if app.balls >= 10:
        app.gameOver = True
    app.timePassed += app.timerDelay
    if app.pitch == True:
        return
    elif app.timePassed >= 40 and app.isHit == False: 
        app.timePassed = 0
        app.ballPy += random.randint(-10, 10)
        app.ballPos += app.ballSpeed * (-1)**(app.expo)
        if app.ballPos + app.width*.2*app.ratio > app.width*.85:
            app.ballPos = 0
            app.pitch = True
            app.bat = False
            app.balls += 1
            app.ballPy = 0
    if isCollision(app):
        collision(app)
    if app.isHit:
        app.ballPos += app.ballSpeed * (-1)**(app.expo)
        app.ballPy += -20
        if app.ballPos + app.width*.2*app.ratio < 0:
            app.ballPos = 0
            app.pitch = True
            app.ballPy = 0
            app.bat = False
            app.isHit = False
            app.expo = 2
            app.balls += 1

def redrawAll(app, canvas):
    drawBackground(app,canvas)
    drawPlayer(app, canvas)
    drawBaseball(app, canvas)
    drawBat(app, canvas)
    drawScoreBoard(app,canvas)
    if app.balls >= 10:
        drawGameOver(app,canvas)
        return
def drawGameOver(app,canvas):
    canvas.create_text(app.width/2,app.height/2,text = "Game Over"
    ,font = "Arial 50")
def drawScoreBoard(app,canvas):
    canvas.create_rectangle(0,0,app.width*.22,app.height*.15,
    fill = 'black')
    canvas.create_text(app.width*.11,app.height*.075,
            text = f"HomeRuns: {app.score}", fill = "white")
    canvas.create_text(app.width*.11,app.height*.092,
            text = f"Pitches {app.balls}", fill = "white")
def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width,app.height, fill = "light blue")
    canvas.create_rectangle(0, app.height*.8, app.width, app.height,
            fill = "green")
    canvas.create_arc(app.width*.1, app.height*.8, app.width*.2, 
    app.height*.95, outline="brown", width = 60, style="arc", extent=180)
    canvas.create_rectangle(app.width*.1, app.height*.8, app.width*.2, 
    app.height*.874, outline="brown", fill="brown")

def drawBaseball(app, canvas):
    canvas.create_oval(app.width*.2*app.ratio + app.ballPos, 
    app.height*.61+app.ballPy, app.width*.24*app.ratio + app.ballPos,
    app.height*.65 + app.ballPy,fill = "white")
    # drawing hitting box
    canvas.create_rectangle(app.width*.71, app.batHeight, 
            app.width*.79,  app.batHeight + app.height*.1)

def drawPlayer(app, canvas):
    canvas.create_image(app.width*.85, app.height*.7, image = ImageTk.PhotoImage(app.catcher))
    if app.pitch == True:
        canvas.create_image(app.width*.2, app.height*.7, image = ImageTk.PhotoImage(app.beforeImage))
    else:
        canvas.create_image (app.width*.2, app.height*.7, image = ImageTk.PhotoImage(app.afterImage))

def drawGameOver(app, canvas):
    canvas.create_rectangle(0, app.height *.4, app.width, app.height*.6,
             fill = "grey")
    canvas.create_text(app.width*.5,app.height*.5,
            text = "Game Over\nPress r to restart", fill = "black", font = "Arial 50")

def drawBat(app, canvas):
    if app.bat == False:
        canvas.create_oval(app.width*.8, app.batHeight - app.height*.02, app.width*.81, 
                app.batHeight + app.height*.02, fill = "brown", outline = "brown")
        canvas.create_oval(app.width*.8, app.batHeight + app.height*.08, app.width*.81, 
                app.batHeight + app.height*.12, fill = "brown", outline = "brown")
        canvas.create_rectangle(app.width*.8, app.batHeight,
                app.width*.81, app.batHeight + app.height*.1, 
                fill = "brown", outline = "brown")
        canvas.create_rectangle(app.width*.8025, app.batHeight + app.height*.1, app.width*.8075,
                app.batHeight + app.height*.17, fill = "brown", outline = "brown")

    if app.bat == True:
        canvas.create_oval(app.width*.695, app.batHeight - app.height*.01, app.width*.735, 
                app.batHeight + app.height*.01, fill = "brown", outline = "brown")
        canvas.create_oval(app.width*.765, app.batHeight - app.height*.01,
                app.width*.795, app.batHeight + app.height*.01, 
                fill = "brown", outline = "brown")
        canvas.create_rectangle(app.width*.71, app.batHeight - app.height*.01,
                app.width*.79, app.batHeight + app.height*.01, 
                fill = "brown", outline = "brown")
        canvas.create_rectangle(app.width*.79, app.batHeight - app.height*.005, 
                app.width*.82, app.batHeight + app.height*.005, fill = "brown", outline = "brown")
def isCollision(app):
    if(app.width*.71 <= app.ballPy + app.width*.2*app.ratio + app.ballPos and
            app.batHeight <= app.height*.61+app.ballPy and
            app.width*.79 >= app.width*.24*app.ratio + app.ballPos
            and app.batHeight + app.height*.1 >= app.height*.65 + app.ballPy
            and app.bat):
        app.isHit = True
        return True
    else:
        return False
def collision(app):
    app.expo = 1
    app.score += 1


runApp(width=1200, height=800)
