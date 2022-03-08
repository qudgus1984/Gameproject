import pygame
###################################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기 설정
screen_height = 640 # 세로 크기 설정
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock(60)
###################################################################################################

# 1: 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load("/Users/ibyeonghyeon/Desktop/gameproject/Gameproject/pygame_basic/background.png")

# 캐릭터 만들기
character = pygame.image.load("/Users/ibyeonghyeon/Desktop/gameproject/Gameproject/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height



running = True 
while running:
  dt = clock.tick(30) 

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 

  # 3. 게임 캐릭터 위치 정의

  # 4. 충돌 처리
  
  # 5. 화면에 그리기
  screen.blit(background(0, 0))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update()

pygame.quit()