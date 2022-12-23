import pygame
import random

size=4
pygame.image.load("images/chess"+str(size)+".png")

a = ["A", "B", "C", "D"]

# 隨機抽取 2 個元素（取後放回）
x = random.choices(a, k=2)
print(a)