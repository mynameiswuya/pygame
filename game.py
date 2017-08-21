import pygame
import sys

# 初始化game
pygame.init()
size=width,height=600,400
speed=[-2,1]
bg=(0,0,0)
#创建指定大小的窗口
screen=pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption("初次见面，多多关照！")
pic=pygame.image.load("p1.gif")
#获取图像的位置矩形
position=pic.get_rect()

while True:
#检测是否关闭
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
#移动图片
    position=position.move(speed)

#检测图片是否过了左边界或右边界，如果过界则将图片反转，移动方向也反转
    if position.left<0 or position.right>width:
        pic=pygame.transform.flip(pic,True,False)
        speed[0]=-speed[0]
    if position.top<0 or position.bottom>height:
        speed[1]=-speed[1]
#填充背景
    screen.fill(bg)
#更新图像
    screen.blit(pic,position)
#更新界面
    pygame.display.flip()
#延迟10毫秒
    pygame.time.delay(10)