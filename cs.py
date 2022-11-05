import math, copy, random
from cmu_112_graphics import *

def appStarted(app):
    app.ballSpeed = app.width//50
    app.ballPos = 0
    app.ballPY = app.height*.38
    app.timerDelay = 20
    app.timePassed = 0
    app.pitch = True
    app.ratio = app.height/app.width
    app.bat = False
    app.batHeight = app.height//2

def keyPressed(app, event):
    if event.key == "p":
        app.pitch = False

def mouseMoved(app, event):
    if app.bat == True:
        return
    else:
        app.batHeight = event.y
        app.batPositionY = event.y
        app.batPositionX = event.x
def isCollision(app):
    if (app.batHeight <= app.ballPos + 10 and app.batHeight >= app.ballPos - 10
    ):
        print("True")
        return True
    else: 
        return False

def collision(app):
    app.ballPos -= app.ballSpeed*(random.randint(1,10))

    

def mousePressed(app,event):
    if event.x != 0:
        app.bat = True
        app.batHeight = event.y

def timerFired(app):
    app.timePassed += app.timerDelay
    if app.pitch == True:
        return
    elif app.timePassed >= 40: 
        app.timePassed = 0
        app.ballPos += app.ballSpeed
        if app.ballPos + app.width*.2*app.ratio > app.width:
            app.ballPos = 0
            app.pitch = True
            app.bat = False
    if isCollision(app):
        collision(app)


def redrawAll(app, canvas):
    drawBackground(app,canvas)
    drawBaseball(app, canvas)
    drawBat(app, canvas)

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width,app.height, fill = "blue")
    canvas.create_rectangle(0, app.height*.8, app.width, app.height,
            fill = "green")
    canvas.create_arc(app.width*.1, app.height*.8, app.width*.2, 
    app.height*.95, outline="brown", width = 60, style="arc", extent=180)

def drawBaseball(app, canvas):
    canvas.create_oval(app.width*.2*app.ratio + app.ballPos, app.height*.38, 
            app.width*.24*app.ratio + app.ballPos, app.height*.42,
            fill = "white")

def drawBat(app, canvas):
    if app.bat == False:
        canvas.create_rectangle(app.width*.8, app.batHeight,
                app.width*.81, app.batHeight + app.height*.1, 
                fill = "grey")
    if app.bat == True:
        canvas.create_rectangle(app.width*.7, app.batHeight,
                app.width*.8, app.batHeight + app.height*.02, 
                fill = "grey")

runApp(width=1200, height=800)