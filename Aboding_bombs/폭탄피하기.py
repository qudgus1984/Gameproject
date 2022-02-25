import pygame
import random
###################################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기 설정
screen_height = 720 # 세로 크기 설정
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("BH Game")

# FPS
clock = pygame.time.Clock()
###################################################################################################

# 1: 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)


background = pygame.image.load("C:/Users/mom/Desktop/Gameproject/Aboding_bombs/space.jpg")

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("C:/Users/mom/Desktop/Gameproject/Aboding_bombs/spaceship.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당되는 곳에 위치 (세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 미사일 좌표
e_to_x = 0
e_to_y = 0

# 이동 속도
character_speed = 0.5
enemy_speed = 0.3

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/mom/Desktop/Gameproject/Aboding_bombs/bomb.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = 0 # 화면 세로 크기 가장 아래에 해당되는 곳에 위치 (세로)

running = True 
while running:
  dt = clock.tick(60) 

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 

    if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
      if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
        to_x -= character_speed # to_x = to_x - 5
      elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
        to_x += character_speed
      elif event.key == pygame.K_UP: # 캐릭터를 위로
        to_y -= character_speed
      elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
        to_y += character_speed

    if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0

    if event.type == pygame.KEYUP: # 게임이 시작되었을 때
      e_to_y += enemy_speed

    if enemy_y_pos == screen_height - character_height:
      pass

      

  character_x_pos += to_x * dt
  character_y_pos += to_y * dt

  enemy_x_pos += e_to_x * dt
  enemy_y_pos += e_to_y * dt

   # 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width

  # 세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height


  # 충돌 처리를 위한 rect 정보 업데이트
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos

  # 충돌 체크
  if character_rect.colliderect(enemy_rect):
    print("우주선이 폭파되었습니다.")
    running = False

  # 3. 게임 캐릭터 위치 정의

  # 4. 충돌 처리
  
  # 5. 화면에 그리기

  screen.blit(background, (0, 0))
  screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

  pygame.display.update()

pygame.quit()