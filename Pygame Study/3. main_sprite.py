import pygame

pygame.init() # 초기화 작업 필수

screen_width = 480
screen_height = 640

#screen 변수 생성 (화면)
screen = pygame.display.set_mode((screen_width,screen_height))

#게임 타이틀
pygame.display.set_caption("게임 제목")

#배경 변수
background = pygame.image.load("C:\\study\\Python\\util\\background_sample.jpg")

#스프라이트
character = pygame.image.load("C:\\study\\Python\\util\\character.png")
#스프라이트 크기
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
#스프라이트 위치 정보
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #screen.fill((255, 255, 255))
    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update()


pygame.quit()