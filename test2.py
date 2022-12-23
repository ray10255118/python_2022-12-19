import pygame
import random

size=4
pygame.image.load("images/chess"+str(size)+".png")

a = ["A", "B", "C", "D"]

# 隨機抽取 2 個元素（取後放回）
x = random.choices(a, k=2)
print(a)

from random import shuffle

suit = ["♠️", "♥️", "♦️", "♣️"]
order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = []
for i in suit:
    for j in order:
        deck.append(i + j)

shuffle(deck)


if pygame.mouse.get_pressed()[0]:
    print(pygame.mouse.get_pressed()[0])
