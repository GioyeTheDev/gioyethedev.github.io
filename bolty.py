import pygame
import requests
from io import BytesIO
import time

pygame.init()
SW, SH = 800, 600
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Astero's Adventures")
W, B, BS, GS, BC, BC2 = (255, 255, 255), (0, 0, 0), (135, 206, 235), (34, 177, 76), (150, 150, 150), (100, 100, 255)
px, py, pvel, jmp, jc, grav, gl, pd = 100, 400, 3, False, 8, 1, 500, 1
SF, lb, rb, jb, eb, lwt, cf = 4, pygame.Rect(50, SH + 50, 100, 50), pygame.Rect(200, SH + 50, 100, 50), pygame.Rect(350, SH + 50, 100, 50), None, 0, 0
pi, pw1, pw2 = None, None, None

clouds = [pygame.Rect(50, 100, 150, 50), pygame.Rect(300, 150, 150, 50), pygame.Rect(600, 80, 150, 50)]
trees = [pygame.Rect(150, gl - 60, 50, 60), pygame.Rect(500, gl - 60, 50, 60)]
building = pygame.Rect(250, gl - 200, 200, 200)
door = pygame.Rect(building.centerx - 50, building.bottom - 120, 100, 120)

inside_building = False
npc_image = pygame.image.load(BytesIO(requests.get("https://gioyethedev.github.io/p.png").content)).convert_alpha()
npc_image = pygame.transform.scale(npc_image, (64, 64))
npc_rect = npc_image.get_rect(topleft=(300, gl - 64))
npc_velocity = [pvel, -10]

furniture = []

def l_img(url): 
    response = requests.get(url)
    image = pygame.image.load(BytesIO(response.content)).convert_alpha()
    return image

def load_ps(): 
    global pi, pw1, pw2
    if not pi:
        pi, pw1, pw2 = l_img("https://files.catbox.moe/nkff2k.png"), l_img("https://files.catbox.moe/sdgl07.png"), l_img("https://files.catbox.moe/ztsj74.png")
        pi, pw1, pw2 = pygame.transform.scale(pi, (pi.get_width() * SF, pi.get_height() * SF)), pygame.transform.scale(pw1, (pw1.get_width() * SF, pw1.get_height() * SF)), pygame.transform.scale(pw2, (pw2.get_width() * SF, pw2.get_height() * SF))

def sky(): 
    surface = pygame.Surface((SW, SH))
    surface.fill(BS if not inside_building else (101, 67, 33))
    return surface

def grd(): 
    surface = pygame.Surface((SW, 60))
    surface.fill(GS if not inside_building else (139, 69, 19))
    return surface

def walk_anim(): 
    if cf == 1: 
        return pw1
    elif cf == 2:
        return pw2
    else:
        return pi

def walk_anim_update():
    global lwt, cf
    if time.time() - lwt >= 0.25:
        cf = (cf + 1) % 3
        lwt = time.time()

def can_jump(): 
    return py >= gl - 64

def jump():
    global jmp, jc, py, grav
    if jmp:
        if jc >= -8:
            neg = 1 if jc >= 0 else -1
            py -= (jc ** 2) * 0.5 * neg
            jc -= 1
        else:
            jmp = False
            jc = 8

def reset_player_on_ground():
    global py
    if py > gl - 64:
        py = gl - 64

def move_npc():
    global npc_rect, npc_velocity
    npc_rect.x += npc_velocity[0]
    npc_rect.y += npc_velocity[1]

    if npc_rect.bottom < gl:
        npc_velocity[1] += 1
    else:
        npc_rect.bottom = gl
        npc_velocity[1] = -10

    if npc_rect.left <= 0 or npc_rect.right >= SW:
        npc_velocity[0] *= -1

def check_building_interaction():
    global inside_building, px, py, eb
    if door.collidepoint(px + 32, py + 64) and jmp:
        if not inside_building:
            inside_building = True
            px, py = 100, gl - 64
            eb = pygame.Rect(700, SH + 50, 100, 50)
        else:
            inside_building = False
            px, py = building.left - 40, gl - 64
            eb = None

while True:
    load_ps()
    screen.fill(B)
    sky_surface = sky()  
    for x in range(0, SW, sky_surface.get_width()):
        screen.blit(sky_surface, (x, 0))
    
    grd_surface = grd()
    for x in range(0, SW, grd_surface.get_width()):
        screen.blit(grd_surface, (x, gl))
        screen.blit(grd_surface, (x, gl + 60))

    if not inside_building:
        for cloud in clouds:
            pygame.draw.ellipse(screen, (255, 255, 255), cloud)

        for tree in trees:
            pygame.draw.rect(screen, (139, 69, 19), tree)
            pygame.draw.circle(screen, (0, 128, 0), (tree.centerx, tree.top), 30)

        pygame.draw.rect(screen, (105, 105, 105), building)
        pygame.draw.rect(screen, (0, 0, 0), door)

    if inside_building:
        move_npc()

        for i in range(5):
            screen.blit(npc_image, (npc_rect.x + 100 * i, npc_rect.y))

        if eb:
            pygame.draw.rect(screen, BC2, eb)
            screen.blit(pygame.font.SysFont(None, 36).render('Exit', True, W), (eb.x + 30, eb.y + 15))

    pygame.draw.rect(screen, BC2, lb)
    pygame.draw.rect(screen, BC2, rb)
    pygame.draw.rect(screen, BC2, jb)

    font = pygame.font.SysFont(None, 36)
    screen.blit(font.render('Left', True, W), (lb.x + 30, lb.y + 15))
    screen.blit(font.render('Right', True, W), (rb.x + 25, rb.y + 15))
    screen.blit(font.render('Jump', True, W), (jb.x + 25, jb.y + 15))

    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: quit()

    mx, my = pygame.mouse.get_pos()
    mpressed = pygame.mouse.get_pressed()

    if lb.collidepoint(mx, my) and mpressed[0]: 
        px -= pvel * 6
        pd = -1
        walk_anim_update()

    if rb.collidepoint(mx, my) and mpressed[0]: 
        px += pvel * 6
        pd = 1
        walk_anim_update()

    if jb.collidepoint(mx, my) and mpressed[0]: 
        if not jmp:
            jmp = True
            jc = 8
        check_building_interaction()

    if eb and eb.collidepoint(mx, my) and mpressed[0]: 
        inside_building = False
        px, py = building.left - 40, gl - 64
        eb = None

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]: 
        px -= pvel * 6
        pd = -1
        walk_anim_update()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
        px += pvel * 6
        pd = 1
        walk_anim_update()

    if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]: 
        if not jmp:
            jmp = True
            jc = 8
        check_building_interaction()

    jump()
    reset_player_on_ground()

    if pd == 0:
        screen.blit(pi, (px, py))
    else:
        screen.blit(pygame.transform.flip(walk_anim(), True, False) if pd == -1 else walk_anim(), (px, py))

    pygame.display.flip()
    pygame.time.Clock().tick(15)