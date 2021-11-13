import pygame

pygame.init()

window = pygame.display.set_mode((650, 550))

pygame.display.set_caption("Dino Game 🦕")

walk_right = [pygame.image.load("dinopng/dino1.png"), 
pygame.image.load("dinopng/dino2.png"), pygame.image.load("dinopng/dino3.png"), pygame.image.load("dinopng/dino4.png")]

walk_left = [pygame.image.load("dinopng/dino1rev.png"),
pygame.image.load("dinopng/dino2rev.png"), pygame.image.load("dinopng/dino3rev.png"), pygame.image.load("dinopng/dino4rev.png")]

player_stand = pygame.image.load("dinopng/dino1.png")
bg = pygame.image.load("dinopng/jurassic.png")


clock = pygame.time.Clock()
# left_x = 50
# top_y = 485
left_x = 10
top_y = 350
width = 300
height = 200
speed = 10
run = True

isJump = False
jumpCount = 10

left = False
right = False
animation_count = 0
last_move = "right"
bullets = []


class Bimba():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing
    

    def drawing(self, win):
        self.win = win
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def draw_window():
    global animation_count

    window.blit(bg, (0,0))

    if animation_count +1 >= 20:
        animation_count = 0

    if left:
        new_walk_left = pygame.transform.scale(walk_left[animation_count//5], (width, height))
        new_walk_left.set_colorkey((255,255,255))
        window.blit(new_walk_left, (left_x, top_y))
        animation_count += 1
        #window.blit(new_walk_left, (left_x, top_y))
    elif right:
        new_walk_right = pygame.transform.scale(walk_right[animation_count//5], (width, height))
        new_walk_right.set_colorkey((255,255,255))
        window.blit(new_walk_right, (left_x, top_y))
        animation_count += 1
        # window.blit(new_walk_right, (left_x, top_y))
    else:
        new_player_stand = pygame.transform.scale(player_stand, (width, height))
        new_player_stand.set_colorkey((255,255,255))
        window.blit(new_player_stand, (left_x, top_y))
        # window.blit(new_player_stand, (left_x, top_y))
    
    for bullet in bullets:
        bullet.drawing(window)
        #print(bullet)

    pygame.display.update()


while run:
    #pygame.time.delay(50)
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    for bullet in bullets:
        if bullet.x < 650 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()


    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_f]:
        if last_move =="right":
            facing = 1
        else:
            facing = -1
        
        if len(bullets) < 5:
            bullets.append(Bimba(round(left_x + width //2), round(top_y + height //2), 7, (255, 0, 0), facing ))

    if keys[pygame.K_LEFT] and left_x > 0:
        left_x -= speed
        left = True
        right = False
        last_move = "left"

    elif keys[pygame.K_RIGHT] and left_x < 650 -width:
        left_x += speed
        left = False
        right = True
        last_move = "right"

    else:
        left = False
        right = False
        animation_count = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    
        # if keys[pygame.K_UP] and top_y > 20:
        #     top_y -= speed

        # if keys[pygame.K_DOWN] and top_y < 550 -20 -height:
        #     top_y += speed
        
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                #print(top_y)
                top_y += (jumpCount **2) /2
            else:
                #print(top_y)
                top_y -= (jumpCount **2) /2
            # print(jumpCount)
            # print(top_y)
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    draw_window()

pygame.quit()



