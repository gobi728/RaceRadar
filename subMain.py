import pygame
import sys
import os

location_data = [
    {"x": 651, "y": 265}, {"x": 647, "y": 258}, {"x": 420, "y": 259}, {"x": 279, "y": 175},
    {"x": 216, "y": 263}, {"x": 153, "y": 197}, {"x": 38, "y": 372}, {"x": 86, "y": 418},
    {"x": 154, "y": 520}, {"x": 228, "y": 272}, {"x": 333, "y": 346}, {"x": 554, "y": 364},
    {"x": 559, "y": 397}, {"x": 701, "y": 409}, {"x": 731, "y": 363}, {"x": 689, "y": 107},
    {"x": 666, "y": 106}, {"x": 637, "y": 80}, {"x": 623, "y": 139}
]
dir_path = os.path.dirname(os.path.realpath(__file__))

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dummy Prediction Model")

# Load background image with transparency
background_image = pygame.image.load(dir_path+"\\map.png").convert_alpha()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load sprite image (opaque)
sprite_image = pygame.image.load(dir_path+"\\sprite.png").convert_alpha()
sprite_image = pygame.transform.scale(sprite_image, (20, 20))

# Define the object class
class MovingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.center = (622, 134)  # Starting position
        self.target_position_index = 0  # Index to track current target position in location_data
        self.speed = 12.176  # Pixels per second

    def update(self, dt):  # dt is the time elapsed since the last update, in milliseconds
        # Get current target position from location_data
        target_position = location_data[self.target_position_index]
        target_x, target_y = target_position['x'], target_position['y']

        # Calculate vector from current position to target position
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        
        # Calculate distance between current and target positions
        distance = (dx ** 2 + dy ** 2) ** 0.5
        
        if distance > 0:  # Check if there is movement needed
            # Calculate movement for this frame based on speed and dt
            movement_x = dx * self.speed * (dt / 1000)  # Convert dt to seconds
            movement_y = dy * self.speed * (dt / 1000)

            # Update the sprite's position
            if abs(movement_x) > abs(dx):
                self.rect.centerx = target_x
            else:
                self.rect.centerx += movement_x

            if abs(movement_y) > abs(dy):
                self.rect.centery = target_y
            else:
                self.rect.centery += movement_y

            # Check if reached the target position
            if self.rect.center == (target_x, target_y):
                # Increment target position index, and wrap around if reached the end
                self.target_position_index = (self.target_position_index + 1) % len(location_data)

# Define Button class
class Button:
    def __init__(self, x, y, width, height, text, color=(200, 200, 200), font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, font_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Create a button
button = Button(10, HEIGHT - 60, 150, 50, "Exit")

# Create a sprite group and add the moving object
all_sprites = pygame.sprite.Group()
moving_object = MovingObject()
all_sprites.add(moving_object)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if button.is_clicked(event):
            running = False

    # Update
    dt = clock.tick(23.9764)  # Cap the frame rate at 23 FPS
    all_sprites.update(dt)

    # Render
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    button.draw(screen)
    pygame.display.flip()

# Properly quit Pygame and exit Python
pygame.quit()
sys.exit()
