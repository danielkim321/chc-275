import pygame
 
import sys
 
import random
pygame.init()
 
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash")
 
clock = pygame.time.Clock()
 
try:
    background_img = pygame.image.load('img/background.jpg').convert_alpha()
    background_scaled = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
except:
    background_scaled = pygame.Surface((WIDTH, HEIGHT))
    background_scaled.fill((135, 206, 235))
bg_x1 = 0
bg_x2 = WIDTH
 
#---------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 215, 0)
#-------------------------------------
 
##-----------------------------------------------------------------
player_size = 50
player_x = 100
floor_y = 512
player_y = floor_y - player_size
player_vel_y = 0
gravity = 0.4
jump_speed = -9.5
is_jumping = False
flip_angle = 0
flip_speed = 10
font = pygame.font.SysFont(None, 48)
score_font = pygame.font.SysFont(None, 36)
high_score = 0
 
#--------------------------------------------------------------------
 
 
class Obstacle:
    def __init__(self, x, obstacle_type):
        self.x = x
        self.type = obstacle_type
        self.width = 50
        self.height = 50
        self.y = floor_y - self.height
        self.scored = False
       
    def move(self, speed=5):
        self.x -= speed
   
    def draw(self, screen):
        if self.type == "spike":
            pygame.draw.polygon(screen, GRAY, [(self.x, self.y + self.height), (self.x + self.width / 2, self.y), (self.x + self.width, self.y + self.height)])
        elif self.type == "cube":
            pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def is_offscreen(self):
        return self.x <- self.width
    def is_passed(self, player_x):
        return self.x + self.width < player_x
 
def generate_obstacle_group():
    obstacle_types = ["spike", 'cube']
    num_obstacles = random.randint(1, 2)
    obstacles = []
    x_pos = WIDTH + random.randint(0, 50)
    for i in range(num_obstacles):
        obs_type = random.choice(obstacle_types)
        obstacles.append(Obstacle(x_pos, obs_type))
        x_pos += 60
    return obstacles
 
 
 
 
#------------------------------------------------------------------------------------------------------------------------------------------------------
def draw_text(text, color, x, y, font_obj  =  font):
    surface = font_obj.render(text, True, color)
    rect = surface.get_rect(center =(x, y))
    screen.blit(surface, rect)
 
def gameover(score, high_score):
    if score > high_score:
        high_score = score
    while True:
 
        screen.blit(background_scaled, (0, 0))
        draw_text("Game Over", RED, WIDTH // 2, HEIGHT // 2 - 80)
        draw_text(f"Score: {score}", BLACK, WIDTH // 2, HEIGHT // 2 - 20)
        draw_text(f"High Score: {high_score}", YELLOW, WIDTH // 2, HEIGHT // 2 + 20)
        draw_text("Press R to Restart or Q to Quit", BLACK, WIDTH // 2, HEIGHT // 2 + 80, score_font)
 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    return high_score
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
def main():
    global player_y, player_vel_y, is_jumping, flip_angle
    global bg_x1, bg_x2, high_score
    player_y = floor_y - player_size
    player_vel_y = 0
    is_jumping = False
    flip_angle = 0
    bg_x1 = 0
    bg_x2 = WIDTH
    score = 0
    obstacles = []
    obstacles.extend(generate_obstacle_group())
    min_spacing = 250
    max_spacing = 400
 
#---------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#GAme Loop
 
    running = True
    while running:
        clock.tick(60)
        bg_x1 -= 2
        bg_x2 -= 2
        if bg_x1 <= -WIDTH:
            bg_x1 = WIDTH
        if bg_x2 <= -WIDTH:
            bg_x2 = WIDTH
        screen.blit(background_scaled, (bg_x1, 0))
        screen.blit(background_scaled, (bg_x2, 0))
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if not is_jumping:
                        is_jumping = True
                        player_vel_y = jump_speed
 
        player_vel_y += gravity
        player_y += player_vel_y
 
        if is_jumping:
            flip_angle -= flip_speed
            if flip_angle <= -360:
                flip_angle += 360
 
        if player_y >= floor_y - player_size:
            player_y = floor_y - player_size
            player_vel_y = 0
            is_jumping = False
            flip_angle = round(flip_angle / 90) * 90
        player_rect = pygame.Rect(player_x, int(player_y), player_size, player_size)
        player_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
 
        pygame.draw.rect(player_surface, RED, (0, 0, player_size, player_size))
        rotated_surface = pygame.transform.rotate(player_surface, flip_angle)
        rotated_rect = rotated_surface.get_rect(center=player_rect.center)
 
        screen.blit(rotated_surface, rotated_rect.topleft)
 
        for obs in obstacles[:]:
            obs.move(5)
            obs.draw(screen)
            if not obs.scored and obs.is_passed(player_x):
                obs.scored = True
                score += 10
            if obs.is_offscreen():
                obstacles.remove(obs)
        if obstacles:
            rightmost_x = max(obs.x for obs in obstacles)
        else:
            rightmost_x = 0
        if rightmost_x < WIDTH - random.randint(min_spacing, max_spacing):
            obstacles.extend(generate_obstacle_group())
        player_collision_rect = pygame.Rect(player_x + 5, int(player_y) + 5, player_size - 10, player_size - 10)
        for obs in obstacles:
            if player_collision_rect.colliderect(obs.get_rect()):
                high_score = gameover(score, high_score)
                return
        score_text = score_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        high_score_text = score_font.render(f"High: {high_score}", True, YELLOW)
        screen.blit(high_score_text, (10, 45))
 
 
 
        pygame.display.flip()
 
while True:
    main()
 