import pygame

pygame.init()

# Window dimension
window = pygame.display.set_mode((1200, 400))

# car and background
track = pygame.image.load('track2.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))

#car position
car_x = 150
car_y = 300
#focal distance
focal_dis = 25
clock = pygame.time.Clock()
#while condtions
drive = True
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    cam_x = car_x + 15
    cam_y = car_y + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    print(up_px)
    if up_px == 255:
        car_y = car_y-2
    # blit = block image transfere
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()