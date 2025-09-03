import turtle
import time
import random

posponer = 0.1

score = 0
high_score = 0

en_pausa = False

wn = turtle.Screen()
wn.title("Aventura de Matias")
wn.bgcolor("grey")
wn.setup(width = 600, height = 620)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("yellow")
comida.penup()
comida.goto(0,100)

segmentos = []
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0     High Score: 0", align = "center", font =("Courier", 24, "normal"))

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def Pause():
    global en_pausa
    en_pausa = True
    texto.goto(0, 0)
    texto.write("PAUSA", align="center", font=("Courier", 36, "bold"))

def Resume():
    global en_pausa
    en_pausa = False
    texto.clear()
    texto.goto(0, 260)
    texto.write(f"Score: {score}    High Score: {high_score}", align = "center", font =("Courier", 24, "normal"))

wn.update()

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
    
while True:
    wn.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        for segmento in segmentos:
            segmento.goto(1000,1000)

            segmento.clear()

        score = 0
        texto.clear()   
        texto.write("Score: {}     High Score: {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
    
    if cabeza.distance(comida) < 20: 
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("red")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score += 1
         
        if score > high_score: 
           high_score = score 

        texto.clear()   
        texto.write("Score: {}    High Score: {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
    
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            for segmento in segmentos:
                segmento.goto(1000,1000)

            segmentos.clear()

            score = 0
            texto.clear()   
            texto.write("Score: {}    High Score: {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
        
    time.sleep(posponer)

    