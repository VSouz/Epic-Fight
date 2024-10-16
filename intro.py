import random
from pygame import Rect


warrior = Actor('idle1') 
warriorBox = Rect(warrior.topleft,warrior.bottomright)
floor = Actor('chao.png')
floorBox = Rect(floor.topleft,floor.bottomright)
background3= Actor('background3.png')
background2 = Actor('background2.png')
background1 = Actor('background1.png')
demon = Actor('demonidle1.png',anchor=('center', 'bottom'))
demonBox = Rect(50,120,300,300)
soundActor = Actor('soundon')
musicActor = Actor('musicon')
musicBox = Rect((514,218),(60,60))
soundBox = Rect((513,292),(60,60))
life = Actor('vida3')
final = Actor('win')

WIDTH = 900
HEIGHT = 600

floor.pos = 450,550
floorBox.x = 0
floorBox.y = 500
warriorBox.x = 0
warriorBox.y = 400
warrior.pos = 50, 440
demon.pos = 800,500
demonBox.x = 650
demonBox.y = 300


frame = 0  
jumps= 2
jumping = False
lifeWarrior = 10
lifeDemon = 30
startDemon = False
animation = True
stopedBoss = False
stopedWarrior = False
scene = 'telainicial'
pause = True
sound = True

personagem = ['idle1.png', 'idle2.png','idle2.png', 'idle3.png', 'idle4.png', 'idle4.png', 'idle4.png']
run = ['run1.png','run2.png','run3.png','run4.png','run5.png','run6.png','run7.png','run8.png']
runReverse = ['run9.png','run10.png','run11.png','run12.png','run13.png','run14.png','run15.png','run16.png']
jump = ['jump1.png','jump1.png','jump1.png','jump1.png','jump1.png','jump1.png','jump2.png','jump3.png','jump1.png','jump2.png','jump3.png']
attack = ['attack1.png','attack2.png','attack3.png','attack4.png','attack5.png','attack6.png','attack7.png','attack8.png','attack9.png','attack10.png','attack11.png','attack12.png']
dash = ['dash1.png','dash1.png','dash2.png','dash3.png','dash4.png','dash5.png','dash6.png','dash7.png']
warriorHit = ['hurt1.png','hurt1.png','hurt1.png','hurt1.png','hurt2.png']
warriorDeath = ['death1.png','death2.png','death3.png','death4.png','death5.png','death6.png','death7.png']
demonidle = ['demonidle1.png','demonidle1.png','demonidle1.png','demonidle1.png','demonidle1.png','demonidle2.png','demonidle3.png','demonidle4.png','demonidle5.png','demonidle6.png','demonidle7.png']
demonWalk = ['demonwalk1.png','demonwalk2.png','demonwalk3.png','demonwalk4.png','demonwalk5.png','demonwalk6.png','demonwalk7.png','demonwalk8.png','demonwalk9.png','demonwalk10.png','demonwalk11.png','demonwalk12.png']
demonWalkReverse = ['demonwalk13','demonwalk14','demonwalk15','demonwalk16','demonwalk17','demonwalk18.png','demonwalk19.png','demonwalk20.png','demonwalk21.png','demonwalk22.png','demonwalk23.png','demonwalk24.png']
demonHit = ['demonhit1.png','demonhit2.png','demonhit3.png']
demonDeath = ['demondeath4.png','demondeath5.png','demondeath6.png','demondeath7.png','demondeath8.png','demondeath9.png','demondeath10.png','demondeath13.png','demondeath14.png','demondeath15.png','demondeath16.png','demondeath15.png','demondeath16.png','demondeath17.png','demondeath18.png','demondeath19.png','demondeath20.png','demondeath21.png','demondeath22.png']
demonAttack = ['demonattack5.png','demonattack10.png','demonattack11.png','demonattack12.png','demonattack13.png']

musica = sounds.battle.play()


# TELAS -------
telaInicial = Actor('telainicial')
menu= Actor('menu')
teclas = Actor('teclas')




def update():
    global scene,pause
    delay()
    if scene == 'telainicial':
        
        
        updateTelaInicial()
        
    elif scene == 'menu':
        if keyboard.escape:
            updateGame()
    elif scene == 'jogo':
        if keyboard.escape:
            updateMenu()
    if scene == 'final':
        updateFinal()
        if keyboard.r:
            tentarNov()

    # movewarrior()
    # boss()


def draw():
    global pause
    screen.clear()
    if scene == 'telainicial':
        telaInicial.draw()
        screen.draw.text("Aperte ESPAÇO para iniciar", center=(WIDTH / 2, (HEIGHT / 2)+ 200), fontsize=40)
       
    if scene == 'jogo':
        pause = False
        background1.draw()
        background2.draw()
        background3.draw()
        floor.draw()
        teclas.draw()
        life.draw()
        # screen.draw.rect(warriorBox,(200,0,0))
        # screen.draw.rect(floorBox,(0,200,0))
        # screen.draw.rect(demonBox,(0,0,200))
        warrior.draw()
        demon.draw()
    if scene == 'menu':
        background1.draw()
        background2.draw()
        background3.draw()
        floor.draw()
        menu.draw()
        soundActor.draw()
        musicActor.draw()
        # screen.draw.rect(soundBox,(0,200,200))
        # screen.draw.rect(musicBox,(0,200,200))
    if scene == 'final':
        final.draw()
        screen.draw.text("Aperte R para Jogar novamente!", center=(WIDTH / 2, (HEIGHT / 2)+ 200), fontsize=30)
    



frame_delay = 1  
current_frame = 0  

def animar(ator, acao):
    global frame, current_frame
    

    
    current_frame += 1

   
    if current_frame >= frame_delay and animation:
        frame = (frame + 1) % len(acao)  
        ator.image = acao[frame] 
        current_frame = 0  

    smallDelay()
    return ator.image
    


def movewarrior():

    global jumps,jumping,lifeDemon,animation,stopedWarrior,stopedBoss,pause,sound
    

    if not stopedWarrior and not pause:

        if keyboard:
            animar(warrior,personagem)

        if keyboard.d and warrior.x < WIDTH:
            
            if not jumping:
                animar(warrior,run)
                warriorBox.x += 10
                warrior.x += 10
            
            else:
                warriorBox.x += 10
                warrior.x += 10
        
        if keyboard.a and warrior.x > 0:
            animar(warrior,runReverse)
            warriorBox.x -= 10
            warrior.x -= 10
        

        if keyboard.k:
            animar(warrior,attack)
            
            if(jumping == False):
                animar(warrior,attack)
                if sound:
                    sounds.warriorhit.play()
                if(warriorBox.colliderect(demonBox) and not startDemon):
                    animar(demon,demonHit)
                if sound:
                    sounds.demonhurt2.play()
                    lifeDemon -= 1

        if keyboard.l  and warrior.x < WIDTH:
            animar(warrior,dash)
            if sound:
                sounds.dash.play()
            warriorBox.x += 60
            warrior.x += 60

        
        if(warriorBox.colliderect(floorBox)):
            warrior.y += 0
            warrior.x += 0
            jumps = 2
            jumping = False
            
            print(warrior.colliderect(floorBox))
        else:
            warriorBox.y += 10
            warrior.y += 10
            jumping = True
            print("não colidiu")
            animar(warrior,jump)
        
        if keyboard.space and not jumping:

            warriorBox.y -= 140
            # warrior.y -=140
            for _ in range(140):
                smallDelay()
                warrior.y -= 1
            jumps -= 1
            jumping = True
            if sound:
                sounds.jump.play()
        
        if lifeWarrior == 0:
            if sound:
                sounds.warriordeath.play()
            animar(warrior,warriorDeath)
            
            stopAniamtion()
            # warrioDeath()
            clock.schedule(warrioDeath,1.0)
        
            stopedWarrior = True
            stopedBoss = True
        


def delay():
    for _ in range(2999999):  
        pass
    movewarrior()
    boss()

def smallDelay():
    for _ in range(19000):  
        pass         


demonAction = [0]*100 + [1]*20 + [2]*5 + [3]*10 + [4]*50

def boss():

    global lifeDemon,startDemon,frame,lifeWarrior,stopedBoss,stopedWarrior,pause,sound

    action = random.choice(demonAction)

    if not stopedBoss and not pause:
        if(action==3 and not startDemon):
            
            animar(demon,demonAttack)
            if sound:
                sounds.demonhit.play()
            if(demonBox.colliderect(warriorBox) and warrior.x < WIDTH and not stopedWarrior):
                
                if sound:
                    sounds.warriorhurt.play()
                warrior.x -=100
                warriorBox.x -=100
                animar(warrior,warriorHit)
                lifeWarrior -=1
                lifeBar()


        if(action==0 and not startDemon):
            animar(demon,demonidle)
            
            
        if(action==1  and demon.x > 0 and not startDemon):
            animar(demon,demonWalk)
            demonBox.x -= 20
            demon.x -= 20
            
        if(action==2  and demon.x < WIDTH and not startDemon):
            animar(demon,demonWalkReverse)
            if sound:
                sounds.bosshaha.play() #
            demonBox.x += 50
            demon.x += 50
            animar(demon,demonidle)
        
        
        if(lifeDemon == 0 and not startDemon):
            animar(demon,demonDeath)
            startDemon = True 
            stopedBoss = True      
            clock.schedule(bossDeath,3.0)
            if sound:
                sounds.demonroar.play()

def lifeBar():
    global lifeWarrior

    if lifeWarrior>= 10:
        life.image = 'vida3'
    elif 4 < lifeWarrior <= 7:
        life.image = 'vida2'
    elif 0 < lifeWarrior <= 5:
        life.image = 'vida1'
    elif lifeWarrior == 0:
        life.image = 'vida'

def bossDeath():
    demon.image ='vazio'
    sounds.demonroar.play()
    clock.schedule(updateFinal,2.0)

def warrioDeath():
    warrior.image = 'death11.png'
    clock.schedule(updateFinal,2.0)

def stopAniamtion():
    global animation
    animation = False 

def pause():
    global stopedBoss,stopedWarrior

    if (stopedWarrior and stopedBoss):
        stopedBoss = False
        stopedWarrior = False
    else:
        stopedWarrior = True
        stopedBoss = True

def updateTelaInicial():

    if keyboard.space:
        global scene
        scene = 'jogo'
        print('apertous')

def updateGame():
    global scene,pause
    
    pause = False
    scene = 'jogo'

def updateMenu():
    global scene, pause

    pause = True
    scene = 'menu'


def on_mouse_down(pos):
    print("Mouse button clicked at", pos)
    if scene == 'menu':
        if musicBox.collidepoint(pos):
            global music
            if musicActor.image == 'musicon':
                musicActor.image = 'musicoff'
                musica.stop()
            elif musicActor.image == 'musicoff':
                musicActor.image = 'musicon'
                sounds.battle.play()
        
        if soundBox.collidepoint(pos):
            global sound
            if soundActor.image == 'soundon':
                soundActor.image = 'soundoff'
                sound = False
                
            elif soundActor.image == 'soundoff':
                soundActor.image = 'soundon'
                sound = True

def updateFinal():
    
    global scene,pause
    pause = True
    scene = 'final'
    if lifeDemon == 0:
        final.image = 'win'

    if lifeWarrior == 0:
        final.image = 'lose'

def tentarNov():
    floor.pos = 450,550
    floorBox.x = 0
    floorBox.y = 500
    warriorBox.x = 0
    warriorBox.y = 400
    warrior.pos = 50, 440
    demon.pos = 800,500
    demonBox.x = 650
    demonBox.y = 300

    global frame,jumps,jumping,lifeWarrior,lifeDemon,startDemon,animation,stopedBoss,stopedWarrior,scene,pause,sound,life,final

    frame = 0  
    jumps= 2
    jumping = False
    lifeWarrior = 10
    lifeDemon = 30
    startDemon = False
    animation = True
    stopedBoss = False
    stopedWarrior = False
    scene = 'telainicial'
    pause = True
    sound = True
    life = Actor('vida3')
    final = Actor('win')
    