'''
Created on 2016年2月29日

@author: Wenyan Yu
'''
# -*- coding: utf-8 -*-
s1 = 72
s2 = 85
s3 = s2-s1
print('''背景：小明和老师在办公室;
小明啊，我作为一个长者得跟你谈谈''')
print('你去年成绩:%d ,今年成绩：%d' %(s1,s2))
print('你的成绩提高了%d分 ,提高了%0.2f,也就是%d%%' % (s3,s3/s1,int(s3/s1*100)))
print('''我今天是作为一个长者跟你们讲。我不是老师，但是我见得太多了。我有这个必要好告诉你们一点人生的经验
你啊，我感觉你啊还要学习一个。你们毕竟还too young.明白我的意思吧？
唉，我也替你着急啊。
好了好了，出去吧。
顺便把下一个同学叫进来。''')
print('小明：吼啊,再见，老师.')
asdddddddddddddddddddddddddddddddddd=input('Enter to continue;')
print('同学叫什么名字;')
name=input('老师，我叫：')
print('你上次考试多少分啊!')
score1=input('老师，我考了：')
score1=int(score1)
print('那你这次考多少分啊!')
score2=input('老师，我考了：')
score2=int(score2)
x=score2-score1
y=score1-score2
if x > 0:
    print('不错，继续努力。成绩提高了%0.1f%%' %(x/score1*100))
elif x < 0:
    print('干什么吃的，好好学。下降了%0.1f%%' %(y/score1*100))
else: 
    print('学如逆水行舟，不进则退，加吧劲吧')