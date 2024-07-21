from PIL import Image
import pygame
import os
# # List of image file paths
# images = ['assets/Image (10).jfif','assets/Image (11).jfif','assets/Image (12).jfif','assets/Image (13).jfif','assets/Image (14).jfif','assets/Image (15).jfif']

# # Open the images and store them in a list
# gif_images = [Image.open(image) for image in images]

# # Save the images as a GIF
# gif_images[0].save(
#     "custom.gif", save_all=True, append_images=gif_images[1:], duration=200, loop=0
# )

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets\Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets\Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets\Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets\Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets\Dino", "DinoDuck2.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
CLOUD = pygame.image.load(os.path.join("Assets\Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("Assets\Other", "Track.png"))
class Cactus:
    X_POS = 240
    Y_POS = 310
    X2_POS = 1000

    def __init__(self):
        self.small_cactus_img = SMALL_CACTUS
        self.large_cactus_img = LARGE_CACTUS
        self.image1 = self.small_cactus_img[0]
        self.image2 = self.large_cactus_img[0]
        self.cactus_rect = self.image1.get_rect()
        self.cactus_rect2 = self.image2.get_rect()
        # self.cactus_rect.x = self.X_POS
        # self.cactus_rect.y = self.Y_POS
        self.cactus_rect2.x = self.X2_POS
        self.cactus_rect2.y = self.Y_POS
    
    def draw(self, SCREEN):
        # SCREEN.blit(self.image1,(self.cactus_rect.x, self.cactus_rect.y))
        SCREEN.blit(self.image2,(self.cactus_rect2.x, self.cactus_rect2.y))

class Cloud:
    X_POS = 100
    Y_POS = 100
    Y2_POS = 50
    X2_POS = 300
    Y3_POS = 100
    X3_POS = 500

    def __init__(self):
        self.cloud = CLOUD
        self.image = self.cloud
        self.image2 = self.cloud
        self.image3 = self.cloud
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = self.X_POS
        self.cloud_rect.y = self.Y_POS
        self.cloud_rect2 = self.image2.get_rect()
        self.cloud_rect2.x = self.X2_POS
        self.cloud_rect2.y = self.Y2_POS
        self.cloud_rect3 = self.image3.get_rect()
        self.cloud_rect3.x = self.X3_POS
        self.cloud_rect3.y = self.Y3_POS
        

    def draw(self, SCREEN):
        SCREEN.blit(self.image,(self.cloud_rect.x, self.cloud_rect.y))
        SCREEN.blit(self.image,(self.cloud_rect2.x, self.cloud_rect2.y))
        SCREEN.blit(self.image,(self.cloud_rect3.x, self.cloud_rect3.y))



class Dinosour:
    X_POS = 10
    Y_POS = 310
    Y_POS_DUCK = 340

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    
    def update(self,userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_duck:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS
        self.dino_rect.x = self.Y_POS_DUCK
        self.step_index += 1
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS-50
        self.dino_rect.x = self.X_POS+50
        self.step_index += 1
        self.dino_jump = True
        self.dino_duck = False


    def draw(self, SCREEN):
        SCREEN.blit(self.image,(self.dino_rect.x, self.dino_rect.y))

class Bird:
    X_POS = 400
    Y_POS = 100

    def __init__(self):
        self.bird_img = BIRD
        self.image = self.bird_img[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.X_POS
        self.bird_rect.y = self.Y_POS
        self.bird_run = True
        self.step_index = 0
    def draw(self, SCREEN):
        SCREEN.blit(self.image,(self.bird_rect.x,self.bird_rect.y))

    def update(self):
 
        if self.bird_run:
            self.run()
        if self.step_index >= 10:
            self.step_index = 0
    def run(self):
        self.image = self.bird_img[self.step_index // 5]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.X_POS
        self.bird_rect.y = self.Y_POS
        self.step_index += 1



def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosour()
    cactus = Cactus()
    cloud = Cloud()
    bird = Bird()
    while run:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((225,225,225))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)
        cactus.draw(SCREEN)
        cloud.draw(SCREEN)
        bird.draw(SCREEN)
        bird.update()
        clock.tick(30)
        pygame.display.update()


main()

