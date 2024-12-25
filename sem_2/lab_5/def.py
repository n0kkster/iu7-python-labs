import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Defence')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TORS_LENGTH = 30
HEAD_RADIUS = 15
LEG_LENGTH = 50
ARM_LENGTH = 30


SPEED = 0.1

class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = math.pi / 4
        self.angle2 = self.angle + math.pi / 2
        self.direction = 1

    def draw(self):
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + TORS_LENGTH))
        pygame.draw.circle(screen, WHITE, (self.x, self.y - HEAD_RADIUS - 5), HEAD_RADIUS)

        leg_end_x = self.x + math.cos(self.angle) * LEG_LENGTH
        leg_end_y = self.y + TORS_LENGTH + math.sin(self.angle) * LEG_LENGTH
        pygame.draw.line(screen, WHITE, (self.x, self.y + TORS_LENGTH), (leg_end_x, leg_end_y), 5)

        leg_end_x = self.x + math.cos(self.angle2) * LEG_LENGTH
        leg_end_y = self.y + TORS_LENGTH + math.sin(self.angle2) * LEG_LENGTH
        pygame.draw.line(screen, WHITE, (self.x, self.y + TORS_LENGTH), (leg_end_x, leg_end_y), 5)

        leg_end_x = self.x + math.cos(math.pi / 4) * ARM_LENGTH
        leg_end_y = self.y + TORS_LENGTH / 4 + math.sin(math.pi / 4) * ARM_LENGTH
        pygame.draw.line(screen, WHITE, (self.x, self.y + TORS_LENGTH / 4), (leg_end_x, leg_end_y), 5)

        leg_end_x = self.x + math.cos(math.pi / 4 + math.pi / 2) * ARM_LENGTH
        leg_end_y = self.y + TORS_LENGTH / 4 + math.sin(math.pi / 4 + math.pi / 2) * ARM_LENGTH
        pygame.draw.line(screen, WHITE, (self.x, self.y + TORS_LENGTH / 4), (leg_end_x, leg_end_y), 5)

    def update(self):
        self.angle += 0.001 * self.direction
        self.angle2 += 0.001 * -self.direction

        if self.angle > math.pi / 2 or self.angle < math.pi / 5:
            self.direction = -self.direction

        self.x += SPEED
        if self.x > WIDTH:
            self.x = 0

person = Person(0, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    person.draw()
    person.update()

    pygame.display.flip()

pygame.quit()
