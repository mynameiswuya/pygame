import pygame
import sys
#将pygame的所有常量名导入
from pygame.locals import *

# 初始化game
pygame.init()
size=width,height=600,400
speed=[-1,0]
clock=pygame.time.Clock()
bg=(255,255,255)


#指定要移动的图片
pic=pygame.image.load("p1.gif")

#获取图像的位置矩形
position=pic.get_rect()


#创建指定大小的窗口
#这句是恶搞一下，把窗口大小设置的和图片一样大screen=pygame.display.set_mode(tuple(position)[2:4],RESIZABLE)
screen=pygame.display.set_mode(size,RESIZABLE)

#设置窗口标题
pygame.display.set_caption("初次见面，多多关照！")




#设置图片人物方向
l_pic=pic
r_pic=pygame.transform.flip(pic,True,False)

#设置非全屏
fullscreen=False

#获取当前显示器支持的所有分辨率
screen_mode=pygame.display.list_modes()


while True:
#检测是否关闭
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()


        #检测键盘按下并响应键盘动作
        if event.type==KEYDOWN:
            # 使用F11键进行全屏和非全屏切换
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(screen_mode[0], FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)
            if event.key==K_LEFT:
                speed=[-1,0]
                pic=l_pic
            if event.key==K_RIGHT:
                speed=[1,0]
                pic=r_pic
            if event.key==K_UP:
                speed=[0,-1]
            if event.key==K_DOWN:
                speed=[0,1]

#移动图片
    #print(position)
    position=position.move(speed)
    print('图片的坐标：%s'%position)

#检测图片是否过了左边界或右边界，如果过界则将图片反转，移动方向也反转
    if position.left<0 or position.right>width:
        pic=pygame.transform.flip(pic,True,False)
        speed[0]=-speed[0]
    if position.top<0 or position.bottom>height:
        speed[1]=-speed[1]

# 用户调整窗口大小
    if event.type == VIDEORESIZE:
        size = event.size
        width, height = size
        print('窗口的大小：', size)
        screen = pygame.display.set_mode(size, RESIZABLE)
    #if position.left<pic.get_rect


#填充背景
    screen.fill(bg)

#更新图像
    screen.blit(pic,position)

#更新界面
    pygame.display.flip()

#设置帧率为30
    clock.tick(30)