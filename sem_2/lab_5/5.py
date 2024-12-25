import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

# Параметры окна
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Lab05')

# Загрузка изображений фонов
background_layers = [
    pygame.image.load(f'img/bg_{i+1}.png').convert_alpha() for i in range(10)
][::-1]

# Скорости для каждого слоя (можно настроить как нужно)
layer_speeds = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5]

# Ширина изображения фона (предполагается, что все изображения одинаковой ширины)
bg_width = background_layers[0].get_width()

# Начальные позиции для каждого слоя
x_positions = [[0, bg_width] for _ in range(10)]

# Загрузка спрайтов персонажа для анимации ходьбы
character_running_sprites = [
    pygame.transform.scale(pygame.image.load(f'img/char_{i+1}.png').convert_alpha(), (2 * 64, 3.5 * 64)) for i in range(8)
]

character_idle_sprites = [
    pygame.transform.scale(pygame.image.load(f'img/idle_{i+1}.png').convert_alpha(), (2 * 64, 3.5 * 64)) for i in range(4)
]

character_dying_sprites = [
    pygame.transform.scale(pygame.image.load(f'img/die_{i+1}.png').convert_alpha(), ((2 + i / 5) * 64, (3.5 - i / 5) * 64)) for i in range(8)
]


character_width = character_running_sprites[0].get_width()
character_height = character_running_sprites[0].get_height()

# Начальная позиция персонажа
character_x = -character_width
character_y = screen_height - character_height

# Параметры движения персонажа
character_speed = 5
character_stop_x = screen_width // 2 + 100  # Позиция, где персонаж остановится

# Параметры анимации персонажа
animation_speed = 0.1  # Скорость анимации (чем меньше значение, тем быстрее анимация)
current_frame = 0
last_frame_time = time.time()

# Флаги состояния
character_running = False
character_idle = False
character_dying = False
character_dead = False

background_running = True
background_slowing_down = False

# Время старта фона
start_time = time.time()

# Главный цикл
running = True
clock = pygame.time.Clock()

while running:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление позиций слоёв
    if background_running:
        for i in range(10):
            x_positions[i][0] -= layer_speeds[i]
            x_positions[i][1] -= layer_speeds[i]

            # Если один из изображений полностью ушёл за экран, перемещаем его вправо
            if x_positions[i][0] <= -bg_width:
                x_positions[i][0] = x_positions[i][1] + bg_width
            if x_positions[i][1] <= -bg_width:
                x_positions[i][1] = x_positions[i][0] + bg_width
    else:
        for i in (5, 7):
            x_positions[i][0] -= layer_speeds[i]
            x_positions[i][1] -= layer_speeds[i]

            # Если один из изображений полностью ушёл за экран, перемещаем его вправо
            if x_positions[i][0] <= -bg_width:
                x_positions[i][0] = x_positions[i][1] + bg_width
            if x_positions[i][1] <= -bg_width:
                x_positions[i][1] = x_positions[i][0] + bg_width


    # Запуск персонажа через 7 секунд
    if elapsed_time >= 7 and not character_running and background_running:
        character_running = True

    # Движение персонажа
    if character_running and character_x < character_stop_x:
        character_x += character_speed
        if character_x + 100 >= character_stop_x:
            background_slowing_down = True

    # Плавная остановка персонажа и фона
    if background_slowing_down:
        character_speed *= 0.95
        for i in range(10):
            if i in (5, 7):
                continue
            layer_speeds[i] *= 0.95

        if character_speed < 0.02 and character_running:
            character_speed = 0
            character_running = False
            character_idle = True

        if any(speed < 0.01 for speed in layer_speeds):
            background_slowing_down = False
            background_running = False

    # Обновление кадра анимации персонажа
    if character_running or character_speed > 0:
        if current_time - last_frame_time >= animation_speed:
            current_frame = (current_frame + 1) % len(character_running_sprites)
            last_frame_time = current_time

    if character_idle and not character_dying:
        if current_time - last_frame_time >= animation_speed * 2:
            current_frame = (current_frame + 1) % len(character_idle_sprites)
            last_frame_time = current_time
        
        if elapsed_time > 17:
            character_idle = False
            character_dying = True
            current_frame = 0

    # Рендеринг слоёв фона
    for i in range(10):
        screen.blit(background_layers[i], (round(x_positions[i][0]), 0))
        screen.blit(background_layers[i], (round(x_positions[i][1]), 0))

        # Отрисовка персонажа за текстурами фона
        if i == 7:
            if character_running:
                screen.blit(character_running_sprites[current_frame], (round(character_x), character_y))
            elif character_idle:
                screen.blit(character_idle_sprites[current_frame % len(character_idle_sprites)], (round(character_x), character_y))
            elif character_dying or character_dead:
                screen.blit(character_dying_sprites[current_frame], (round(character_x), character_y))

    if character_dying:
        if current_time - last_frame_time >= animation_speed * 2 and not character_dead:
            current_frame += 1
            last_frame_time = current_time

        if current_frame >= len(character_dying_sprites):
            character_dying = False
            character_dead = True
            current_frame -= 1


    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
