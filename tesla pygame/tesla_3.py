import pygame

pygame.init()

# Window dimension
window = pygame.display.set_mode((1200, 400))

# car and background
track = pygame.image.load('track3.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))

#car position
car_x = 155
car_y = 300

#variable
focal_dis = 25
direction = 'up'
clock = pygame.time.Clock()
cam_x_offset = 0
#while condtions
drive = True
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]

    print(up_px, right_px)

    # change dirction of the car
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)

    # drive
    if direction == 'up' and up_px == 255:
        car_y = car_y-2
    elif direction == 'right' and right_px ==255:
        car_x = car_x + 1
    # blit = block image transfere
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()