import pygame,random,time

pygame.init()

clock = pygame.time.Clock()
win = pygame.display.set_mode((640,600))
pygame.display.set_caption("Flappy Fish")

# partcile


# OPSTCAL
class OPS:
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        self.pipe = pygame.image.load("assets/pipe.png").convert_alpha()
        self.pipe = pygame.transform.scale(self.pipe,(34,800))
        self.pip2 = pygame.transform.flip(self.pipe,False,True)
        self.oplist = [pygame.Rect(self.x,-545,34,800),pygame.Rect(self.x,400,34,800),pygame.Rect(self.x+20,0,10,600)]
        self.make_random(self.oplist)
        self.pop = False
        
    def update(self,win,dt,rect):
        
        for o in self.oplist:
            o.x -= 1 * dt
            if o != self.oplist[-1]:
            # render ---------------------------------->
                pygame.draw.rect(win,(205,10,10),o)
                win.blit(self.pipe,(o.x,o.y))

                if o.colliderect(rect):
                    return True
            
        
    def make_random(self,l):

        pos=random.randint(100,180)
        new_arrange = l
        numb = random.choice([-1,1])
        for i in l:
            i.y -= numb * pos
            
        self.opjlist = l


def GameOverScreen(win,score):
    
    font = pygame.font.SysFont('Georgia',30,True)
    gov = 1
    while gov:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                  gov = 0
                  break


        text = font.render(str("Score : " + str(score)),1,(255,255,255))
        win.blit(text,(250,250))
        win.blit(font.render(str("YOU DIE!"),1,(255,255,255)),(250,300))
        win.blit(font.render(str("PRESS CLICK TO PLAY AGAIN"),1,(255,255,255)),(100,400))
      
        pygame.display.update()
# Fish
Fish = pygame.Rect(int(640/2 - 20),int(600/2 + 10),50,30)
run = True
gov = False

fish = pygame.image.load("assets/fish.png").convert_alpha()
fish_swim = pygame.image.load("assets/fish_swim.png").convert_alpha()
pipe = pygame.image.load("assets/pipe.png").convert_alpha()
animation = [fish_swim,fish]
cur_anim = 1

f = 0
vel = 2
timer = 300
font = pygame.font.SysFont('Arial',50,True)
opjlist = []
partclies = []
last_time = time.time()
score = 0
g = 5
touch = 0
while run:
    
    clock.tick(60)
    win.fill((42,120,124))
    #set delta time
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                touch = 1
                f = 10
                cur_anim = 0
                
    #update
    if f:
        Fish.y -= vel * f * dt
        f -= 1
    else:
        cur_anim = 1
    
   # if f <=0:
    if touch:
        Fish.y += g * dt
    else:
        Fish.y = 400
    timer += 1
    if timer >= 300:
        opjlist.append(OPS(650,0))
        timer = 0
          
    if len(opjlist):
        for o in opjlist:
            
            update = o.update(win,dt,Fish)
            if update or Fish.y > 900:
                #game over
                gov = True
                
            if o.oplist[2].colliderect(Fish):
                score += 1
                o.oplist[2].x = -200

    if gov:
        touch = 0
        gov = False
        opjlist = []
        GameOverScreen(win,score)
        score = 0
          
   
  
    
    text = font.render(str(score),1,(255,255,255))
    win.blit(text,(300,20))
    #pygame.draw.rect(win,(12,22,244),Fish,5)
    win.blit(animation[cur_anim],(Fish.x,Fish.y))
    pygame.display.update()

pygame.quit()
