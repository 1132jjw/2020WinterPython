import random, pygame, sys
from pygame.locals import *
# from PIL import Image
# from PIL import ImageDraw


DARKGREEN = (0,155,0)
DARKGRAY=(0,155,0)
RED = (255,0,0)
YELLOW=(255,255,10)
BLUE = (0,0,255)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)
BLACK = (0,0,0)
widthSize = 200               #맵 지역 하나의 가로길이
heightSize = 100              #맵 지역 하나의 세로길이
padWidth = widthSize*8+1        #게임판의 전체 가로의 길이를 나타냄 - (맵이 9X9 크기이므로 지역하나의 가로길이*9만큼으로 구성함)
padHeight = heightSize*8+1       #게임판의 전체 세로의 길이를 나타냄 - (맵이 9X9 크기이므로 지역하나의 세로길이*9만큼으로 구성함)
nameBlank=20                  #20픽셀아래만큼 y좌표 아래에 글자를 찍어주기위함
padx = (padWidth - 1)  #보드판의 가로길이로 초기화
pady = (padHeight - 1) #보드판의 세로길이로 초기화


dic1={'출발':0,'타이베이':1,'베이징':2,'제주':3,'황금열쇠1':4,'카이로':5,'이스탄불':6,'무인도':7,'아테네':8,\
    '코펜하겐':9,'황금열쇠2':10,'베른':11,'베를린':12,'오타와':13,'세금받기':14,'베네치아':15,'상파울로':16,\
    '부산':17,'리스본':18,'황금열쇠3':19,'마드리드':20,'우주여행':21,'도쿄':22,'파리':23,'황금열쇠4':24,'런던':25,\
    '서울':26,'국세청':27}

dic2={0:'출발' , 1: '타이베이', 2 : '베이징' , 3:'제주',4:'황금열쇠1', 5:'카이로',6: '이스탄불' , 7: '무인도',  8: '아테네' , \
    9: '원주' ,10: '코펜하겐' ,11:'미래관'  , 12: '베를린' , 13: '오타와' , 14: '세금받기' ,15 : '창조관' ,16:'상파울로' , \
    17: '부산' , 18: '리스본' , 19: '황금열쇠3' , 20: '마드리드' , 21: '우주여행' ,22: '런던' , 23: '파리' ,24: '황금열쇠4' , 25:'대학본부',\
    26: '서울' , 27:'국세청'}

distance=0

#lists=[ [0,0,0,[0,0,0],[[0,0],[0,0],[0,0]],'''플레이어 이미지1~3 x좌표,y좌표'''[[0,0],[0,0],[0,0]]  ]  ,
#        [0,0,0,[0,0,0],[[0,0],[0,0],[0,0]],'''플레이어 이미지1~3 x좌표,y좌표'''[[0,0],[0,0],[0,0]]  ]  ,
#        [0,0,0,[0,0,0],[[0,0],[0,0],[0,0]],'''플레이어 이미지1~3 x좌표,y좌표'''[[0,0],[0,0],[0,0]]  ]  , ... 등 32개의 정보저장
list=[0,0,0,[0,0,0],[[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0]]]
lists=[]

for i in range(0,29):           #토지의 정보들 삽입
    # 0:소유권 1:현재금액 2:땅금액        - 리스트안의 정수
    # 3:[별장,빌딩,호텔]                 - 리스트안의 리스트 속에 정수(건물의 가격)
    # 4:[[~건물1~ [x좌표,y좌표],[~건물2~ x좌표,y좌표],[~건물3~ x좌표,y좌표]]                  -리스트안에 리스트안에 리스트안에 정수(건물들 표시하기위한 좌표)
    # 5:[[~이미지1~ x좌표,y좌표],[~이미지2~ x좌표,y좌표],9[<~이미지3~,x좌표,y좌표]]            -리스트안에 리스트안에 리스트안에 정수(이미지 표시하기위한 좌표)
    lists.append(list)

def showStartScreen():
    fontObj = pygame.font.Font('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/NanumGothic.ttf', 100)
    textSurfaceObj = fontObj.render('BLUEMABLE', True, WHITE, DARKGREEN)
    textRectObj = textSurfaceObj.get_rect()
    # titleFont = pygame.font.Font('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/PySpaceship/NanumGothic.ttf', 100)
    # titleSurf1 = titleFont.render('BlueMarble!', True, WHITE, DARKGREEN)
    # titleRect1 = titleSurf1.get_rect()
    #digree #각도 지정해주면 돌아가는 게 원래 코드

    while True:
        #Gamepad.fill(WHITE) ## 배경 색 채우기 안채워도 돌아감
        # rotatedSurf1 = pygame.transform.rotate(titleSurf1, digree) #원래 각도에따라 돌아가는 코드, 정지된 상태로 있게끔 digree부분 0 으로 만들고, 위치 중앙으로 옮기려 했더니 튜플이라서 자리 바꿀 수 없다고 나옴, 밑에있던 텍스트부분과 완전히 같은 코드라서 가져와서 돌려보니 위치 이동 가능해짐.
        # rotatedRect1 = rotatedSurf1.get_rect()
        # Gamepad.blit(rotatedSurf1, rotatedRect1)
        textRectObj.center = (padWidth / 2 , padHeight / 2)
        Gamepad.blit(textSurfaceObj, textRectObj)

        drawPressKeyMsg() ## 아래쪽에 presskeytoplay 나오게끔 한다.

        if checkForKeyPress(): ## 키입력시 다음 화면으로 넘어가게끔 해주는 함수
            pygame.event.get()
            cln()
            return
        pygame.display.update()

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def terminate():
    pygame.quit()
    sys.exit()

def drawPressKeyMsg(): # 왼쪽 하단에 press a key to play 나오게 하는 함수
    pressKeySurf = pygame.font.Font('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/NanumGothic.ttf', 22)
    pressKeySurfObj = pressKeySurf.render('Press key to start', True, BLACK)
    pressKeyRect = pressKeySurfObj.get_rect()
    pressKeyRect.center = (padWidth / 1.1, padHeight/1.1)
    Gamepad.blit(pressKeySurfObj, pressKeyRect)

#def showGameOverScreen(): # 게임종료 화면 구성하고 키가 입력되면 다시 캐릭터 선택창으로 돌아가게끔 하는 부분인데 현재는 게임 루프가 안끝나서 실행 안됨

#     gameOverFont = pygame.font.Font('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/PySpaceship/NanumGothic.ttf', 150)
#     gameSurf = gameOverFont.render('승리한 사람', True, WHITE)
#     overSurf = gameOverFont.render('승리한 사람 이름', True, WHITE)
#     gameRect = gameSurf.get_rect()
#     overRect = overSurf.get_rect()
#     gameRect.midtop = (WINDOWWIDTH / 2, 10)
#     overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
#
#     Gamepad.blit(gameSurf, gameRect)
#     Gamepad.blit(overSurf, overRect)
#     drawPressKeyMsg()
#     pygame.display.update()
#     pygame.time.wait(500)
#     checkForKeyPress() # clear out any key presses in the event queue
#
#     while True:
#         if checkForKeyPress():
#             pygame.event.get() #
#             return


def cln(): # 게임판을 정해진 색으로 덮어버리는 거, 화면을 재구성하고 싶을때 사용가능
    Gamepad.fill(WHITE)

def drawObject(obj, x, y):  #obj를 받아와서 화면상에 x,y에 뿌려주겠다.
    global Gamepad          #보드판 전역변수로 사용함
    Gamepad.blit(obj,(x,y)) #보드판에 그림같은 객체의 정보를받아 x,y좌표에 뿌려서 출력해줌

def TextsInput(num_x,num_y,i):
    fontObj = pygame.font.Font('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/NanumGothic.ttf',heightSize // 5)  # 파이썬에서 한글폰트 미사용시 한글이 출력되자않음!
    textSurfaceObj = fontObj.render(dic2[i], True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (num_x, num_y)
    Gamepad.blit(textSurfaceObj, textRectObj)

def putTheLandName():
    global Gamepad             #실습실경로  C:/Users/nicen/python/파이썬폰트/sw폰트/PySpaceship/NanumGothic.ttf                  /  노트북 경로...C:/Windows/파이썬폰트/sw폰트/PySpaceship/NanumGothic.ttf
    fontObj = pygame.font.Font('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/NanumGothic.ttf',heightSize//5)    #파이썬에서 한글폰트 미사용시 한글이 출력되자않음!
    nx = 0
    ny = 0
    for i in range(0,28):       #오른쪽아래 맨아래의 START 지점부터 맵의 지역이름을 반시계방향으로 넣어주기위함
        num_x=padx
        num_y=pady
        if (i>=0 and i<=7) or (i>=14 and i<=21):        #맨 아래와 맨 위의 좌우로 지역들에 대해 글자를 채워줌.
            for k in range(0,4):                        #이지역들은 공통적으로 x좌표를 획득(아래 START는 오른쪽 아래이므로 좌표를 전체 보드판의 크기에서 한번 빼주는 작업이 필요)
                num_x=num_x//2                         #전체 보드판의 가로의 길이를 2로 4번 나누어줌
            if i >= 0 and i <= 7:                     #맨 오른쪽 아래 지역  <-------------방향으로
                num_x = padx - num_x-(nx*widthSize)                #전체 보드판의 가로의 길이에서 이 길이만큼 빼주면 START 지점의 x좌표 기준점이됨
                nx+=1
                num_y=pady-(heightSize-nameBlank)  #보드판의 세로의길이-(맵 세로의 길이-공백의길이) 를 하면 START지점의 y좌표가됨
            if i>=14 and i<=21 :       #맨 왼쪽 위 ---------> 방향으로
                num_x=num_x+nx*widthSize
                nx+=1
                num_y=nameBlank
        elif (i>=8 and i<=13) or (i>=22 and i<=27):   #(i>=8 and i<=13) or 21>=i and i<=27
            for k in range(0,3):   #공통적으로 y좌표를 획득
                num_y=num_y//2
            if(i>=8 and i<=13):     # 맨 왼쪽 6개의 땅에대해 이름을 채워줌
                for k in range(0,4):
                    num_x=num_x//2
                num_y=pady-(num_y-nameBlank)-heightSize-heightSize*ny
                ny+=1
                # TextsInput(num_x, num_y,i)
            if(i>=22 and i<=27):                   #맨 오른쪽 6개의 땅에대해 이름을 채워줌
                for k in range(0,4):
                    num_x=num_x//2
                num_x=padx-num_x
                # TextsInput(num_x, num_y,i)
                num_y=num_y+nameBlank+heightSize*ny
                ny+=1
        else:                                     #print 되면 이상한 로직임
            print("Program is not working well!!!")
        if(nx==8):      # 순차적으로 (한칸의 길이) *0 *1 *2에 사용되는연산
            nx=0
        if(ny==6):
            ny=0
        textSurfaceObj = fontObj.render(dic2[i], True, BLACK,WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (num_x, num_y)
        Gamepad.blit(textSurfaceObj, textRectObj)

    #
    # textSurfaceObj = fontObj.render('출발합니다', True, BLACK, WHITE)
    # textSurfaceObj2 = fontObj.render('홍콩', True, BLUE, WHITE)
    # textRectObj = textSurfaceObj.get_rect()
    # textRectObj2 = textSurfaceObj2.get_rect()
    #
    # textRectObj.center = (100, nameBlank+100)
    # # textRectObj = (100,10)
    # textRectObj2.center = (300,nameBlank+100)
    #
    # Gamepad.blit(textSurfaceObj, textRectObj)
    # Gamepad.blit(textSurfaceObj2, textRectObj2)



def drawingLand():
    thick = 2  # 박스의 테두리 크기를 결정하는 변수
    for i in range(0, 9):
        pygame.draw.rect(Gamepad,BLUE, [i * widthSize + 2, 0, widthSize + 2, heightSize])  # 맨위의 좌우로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad,DARKGRAY, [0, i * heightSize + 2, widthSize + 2, heightSize])  # 맨왼쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad,YELLOW,[widthSize * 7 + 2, i * heightSize + 2, widthSize, heightSize])  # 맨오른쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad,RED,[i * widthSize + 2, heightSize * 7 + 2, widthSize, heightSize])  # 맨아래 좌우로 9칸 직사각형 그림
    for i in range(0, 9):
        pygame.draw.rect(Gamepad, BLACK, [i * widthSize, 0, widthSize, heightSize], thick)  # 맨위의 좌우로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad, BLACK, [0, i * heightSize, widthSize, heightSize], thick)  # 맨왼쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad, BLACK, [widthSize * 7, i * heightSize, widthSize, heightSize],thick)  # 맨오른쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad, BLACK, [i * widthSize, heightSize * 7, widthSize, heightSize],thick)  # 맨아래 좌우로 9칸 직사각형 그림

                           #실습실경로:C:/Users/nicen/python/파이썬폰트/swpic/spaceship.png                      /     #노트북경로:  C:/Windows/파이썬폰트/swpic/spaceship.png
    Plane = pygame.image.load('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/spaceship.png')  # 파일 경로로가서 이미지를 불러와 Plane에 저장
    Plane1 = pygame.image.load('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/spaceship.png')  # 파일 경로로가서 이미지를 불러와 Plane에 저장
    Plane1=pygame.transform.scale(Plane1,(25,25))



def initGame():     #메인함수라고 생각하면됨.
    global Gamepad,clock,car1,car2,car3,car4
    pygame.init()
    Gamepad = pygame.display.set_mode((padWidth, padHeight))  # 보드판 생성 1600*800
    Gamepad.fill(WHITE)
    pygame.display.set_caption('MarbleGame')  # 게임의 제목 MarbleGame
    car1 = pygame.image.load('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/car1.png')
    car2 = pygame.image.load('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/car2.png')
    car3 = pygame.image.load('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/car3.png')
    car4 = pygame.image.load('C:/Users/nicen/OneDrive/바탕 화면/sw폰트/image/car4.png')

    showStartScreen()
    drawingLand()
    putTheLandName()
    Rungame()
    #showGameOverScreen() # 게임 종료시 다시 캐릭터선택창

def Rungame():
    global Gamepad,clock,Plane,car1,car2,car3,car4

    clock = pygame.time.Clock()
    p1 = 0;
    p2 = 0;
    p3 = 0;
    p4 = 0

    car1_x = 1410
    car2_x = 1440
    car3_x = 1410
    car4_x = 1440
    car1_y = 740
    car2_y = 740
    car3_y = 770
    car4_y = 770
    i = 0
    crashed = False
    while not crashed:
        # Gamepad.fill(WHITE)
        drawingLand()
        putTheLandName()
        d = random.randint(1, 6)
        for event in pygame.event.get():
            if i % 4 == 0:
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN:  # 플레이어 1 이동
                    if event.key == pygame.K_SPACE:
                        if 0 <= p1 < 7:
                            if p1 + d <= 7:
                                car1_x -= d * 200
                            else:
                                car1_x -= 200 * (7 - p1)
                                car1_y -= 100 * (d - (7 - p1))
                        elif 7 <= p1 < 14:
                            if p1 + d <= 14:
                                car1_y -= d * 100
                            else:
                                car1_y -= 100 * (14 - p1)
                                car1_x += 200 * (d - (14 - p1))
                        elif 14 <= p1 < 21:
                            if p1 + d <= 21:
                                car1_x += d * 200
                            else:
                                car1_x += 200 * (21 - p1)
                                car1_y += 100 * (d - (21 - p1))
                        elif 21 <= p1 < 28:
                            if p1 + d <= 28:
                                car1_y += d * 100
                            else:
                                car1_y += 100 * (28 - p1)
                                car1_x -= 200 * (d - (28 - p1))
                        if p1 + d < 28:
                            p1 += d
                        else:
                            p1 = p1 + d - 28
                        i += 1
            elif i % 4 == 1:
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN:  # 플레이어 2 이동
                    if event.key == pygame.K_SPACE:
                        if 0 <= p2 < 7:
                            if p2 + d <= 7:
                                car2_x -= d * 200
                            else:
                                car2_x -= 200 * (7 - p2)
                                car2_y -= 100 * (d - (7 - p2))
                        elif 7 <= p2 < 14:
                            if p2 + d <= 14:
                                car2_y -= d * 100
                            else:
                                car2_y -= 100 * (14 - p2)
                                car2_x += 200 * (d - (14 - p2))
                        elif 14 <= p2 < 21:
                            if p2 + d <= 21:
                                car2_x += d * 200
                            else:
                                car2_x += 200 * (21 - p2)
                                car2_y += 100 * (d - (21 - p2))
                        elif 21 <= p2 < 28:
                            if p2 + d <= 28:
                                car2_y += d * 100
                            else:
                                car2_y += 100 * (28 - p2)
                                car2_x -= 200 * (d - (28 - p2))
                        if p2 + d < 28:
                            p2 += d
                        else:
                            p2 = p2 + d - 28
                        i += 1
            elif i % 4 == 2:
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN:  # 플레이어 3 이동
                    if event.key == pygame.K_SPACE:
                        if 0 <= p3 < 7:
                            if p3 + d <= 7:
                                car3_x -= d * 200
                            else:
                                car3_x -= 200 * (7 - p3)
                                car3_y -= 100 * (d - (7 - p3))
                        elif 7 <= p3 < 14:
                            if p3 + d <= 14:
                                car3_y -= d * 100
                            else:
                                car3_y -= 100 * (14 - p3)
                                car3_x += 200 * (d - (14 - p3))
                        elif 14 <= p3 < 21:
                            if p3 + d <= 21:
                                car3_x += d * 200
                            else:
                                car3_x += 200 * (21 - p3)
                                car3_y += 100 * (d - (21 - p3))
                        elif 21 <= p3 < 28:
                            if p3 + d <= 28:
                                car3_y += d * 100
                            else:
                                car3_y += 100 * (28 - p3)
                                car3_x -= 200 * (d - (28 - p3))
                        if p3 + d < 28:
                            p3 += d
                        else:
                            p3 = p3 + d - 28
                        i += 1
            elif i % 4 == 3:
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN:  # 플레이어 4 이동
                    if event.key == pygame.K_SPACE:
                        if 0 <= p4 < 7:
                            if p4 + d <= 7:
                                car4_x -= d * 200
                            else:
                                car4_x -= 200 * (7 - p4)
                                car4_y -= 100 * (d - (7 - p4))
                        elif 7 <= p4 < 14:
                            if p4 + d <= 14:
                                car4_y -= d * 100
                            else:
                                car4_y -= 100 * (14 - p4)
                                car4_x += 200 * (d - (14 - p4))
                        elif 14 <= p4 < 21:
                            if p4 + d <= 21:
                                car4_x += d * 200
                            else:
                                car4_x += 200 * (21 - p4)
                                car4_y += 100 * (d - (21 - p4))
                        elif 21 <= p4 < 28:
                            if p4 + d <= 28:
                                car4_y += d * 100
                            else:
                                car4_y += 100 * (28 - p4)
                                car4_x -= 200 * (d - (28 - p4))
                        if p4 + d < 28:
                            p4 += d
                        else:
                            p4 = p4 + d - 28
                        i += 1
        drawObject(car1, car1_x, car1_y)
        drawObject(car2, car2_x, car2_y)
        drawObject(car3, car3_x, car3_y)
        drawObject(car4, car4_x, car4_y)
        pygame.display.update()
        # # clock.tick(30)
    pygame.quit()

    """위는 도시카드, 밑은 소유권표시"""
    # pygame.draw.rect(Gamepad, BLACK, [170, 0, 30, 10], 2)
    # pygame.draw.rect(Gamepad, BLACK, [270, 0, 30, 10], 2)
    # pygame.draw.rect(Gamepad, BLACK, [370, 0, 30, 10], 2)
    # pygame.draw.rect(Gamepad, BLACK, [570, 0, 30, 10], 2)
    """밑에 말"""



initGame()
