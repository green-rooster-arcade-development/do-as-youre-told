import sys
import math
import random
import pygame
import pygame.freetype
pygame.init()
titleFont = pygame.freetype.Font("Sweetly Broken.ttf", 72)

size = width, height = 480, 320
center = centerX, centerY = int(width / 2), int(height / 2)
maxSpeed = 2
speed = [maxSpeed, maxSpeed]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.left = centerX - ballrect.width / 2
ballrect.top = centerY - ballrect.height / 2

offsetY = 5
arcThickness = 3
outerCircleColor = 70, 70, 70
outerCircleRadius = centerY - offsetY
outerCircleDiameter = outerCircleRadius * 2

offsetX = centerX - outerCircleRadius
innerQuadRect = (offsetX + arcThickness * 2, offsetY + arcThickness * 2,
                 outerCircleDiameter - arcThickness * 4, outerCircleDiameter - arcThickness * 4)

red = 247, 47, 27
blue = 0, 137, 233
yellow = 255, 245, 49
green = 59, 204, 72

dist = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # New velocity
    if (dist >= outerCircleRadius - arcThickness * 3):
        randomX = random.randint(0, maxSpeed)
        randomY = random.randint(0, maxSpeed)

        newXSpeed = 0
        newYSpeed = 0
        if (abs(speed[0]) > 0):
            if (speed[0] >= maxSpeed):
                newXSpeed = -speed[0] + randomX
            else:
                newXSpeed = -speed[0] - randomX
        else:
            if (speed[0] <= -maxSpeed):
                newXSpeed = -speed[0] - randomX
            else:
                newXSpeed = -speed[0] + randomX

        if (abs(speed[1]) > 0):
            if (speed[1] >= maxSpeed):
                newYSpeed = -speed[1] + randomY
            else:
                newYSpeed = -speed[1] - randomY
        else:
            if (speed[1] <= -maxSpeed):
                newYSpeed = -speed[1] - randomY
            else:
                newYSpeed = -speed[1] + randomY

        speed = [newXSpeed, newYSpeed]
    ballrect = ballrect.move(speed)

    # New distance
    if ballrect.left < centerX and ballrect.top < centerY:
        dist = math.hypot(ballrect.left - centerX, ballrect.top - centerY)
    elif ballrect.left < centerX and ballrect.top > centerY:
        dist = math.hypot(ballrect.left - centerX, ballrect.bottom - centerY)
    elif ballrect.left > centerX and ballrect.top < centerY:
        dist = math.hypot(ballrect.right - centerX, ballrect.top - centerY)
    else:
        dist = math.hypot(ballrect.right - centerX, ballrect.bottom - centerY)

    # Draw
    screen.fill(black)
    outerCircle = pygame.draw.circle(
        screen, outerCircleColor, center, outerCircleRadius, arcThickness * 2)
    redQuad = pygame.draw.arc(
        screen, red, innerQuadRect, 0, math.pi / 2, arcThickness)
    blueQuad = pygame.draw.arc(
        screen, blue, innerQuadRect, 3 * math.pi / 2, 0, arcThickness)
    yellowQuad = pygame.draw.arc(
        screen, yellow, innerQuadRect, math.pi, 3 * math.pi / 2, arcThickness)
    greenQuad = pygame.draw.arc(
        screen, green, innerQuadRect, math.pi / 2, math.pi, arcThickness)
    screen.blit(ball, ballrect)

    # Title Text
    titleFont.render_to(screen, (centerX - 50, centerY - 100),
                        "do", (255, 255, 255))
    titleFont.render_to(screen, (centerX - 70, centerY - 40),
                        "as you're", (255, 255, 255))
    titleFont.render_to(screen, (centerX - 40, centerY + 30),
                        "told", (255, 255, 255))

    pygame.display.flip()
