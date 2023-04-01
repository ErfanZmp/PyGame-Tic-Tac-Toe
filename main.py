import pygame
import base
import sys

pygame.init()

WIDTH = 600
HEIGHT = WIDTH
LINE_WIDTH = WIDTH//40
BG_COLOR = (204, 204, 255)
LINE_COLOR = (153, 153, 255)
RADIUS = WIDTH//10
MARK_WIDTH = WIDTH//60
CIRCLE_COLOR = (51, 153, 255)
CROSS_COLOR = (255, 102, 102)

BASE = base.Base()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)


def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * (HEIGHT // 3)), (WIDTH, i * (HEIGHT // 3)), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * (WIDTH // 3), 0), (i * (WIDTH // 3), HEIGHT), LINE_WIDTH)


def draw_cross(x, y):
    pygame.draw.line(screen, CROSS_COLOR, (x - RADIUS, y - RADIUS), (x + RADIUS, y + RADIUS), MARK_WIDTH + 5)
    pygame.draw.line(screen, CROSS_COLOR, (x - RADIUS, y + RADIUS), (x + RADIUS, y - RADIUS), MARK_WIDTH + 5)


def draw_marks():
    for row in range(3):
        for col in range(3):
            if BASE.get_mark(row, col) == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (row * (WIDTH // 3) + (WIDTH // 6),
                                    col * (HEIGHT // 3) + (HEIGHT // 6)),
                                   RADIUS, MARK_WIDTH)
            elif BASE.get_mark(row, col) == 'X':
                draw_cross(row * (WIDTH // 3) + (WIDTH // 6),
                           col * (HEIGHT // 3) + (HEIGHT // 6))


def draw_winner(won_player):
    won_coordinate = BASE.get_won_coordinate()
    color = CROSS_COLOR if won_player == 'X' else CIRCLE_COLOR
    pygame.draw.line(screen, color,
                     (won_coordinate[0][1] * (WIDTH // 3) + (WIDTH // 6),
                      won_coordinate[0][0] * (HEIGHT // 3) + (HEIGHT // 6)),
                     (won_coordinate[1][1] * (WIDTH // 3) + (WIDTH // 6),
                      won_coordinate[1][0] * (HEIGHT // 3) + (HEIGHT // 6)),
                     LINE_WIDTH)


draw_lines()
player = 'X'
finished = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if finished:
                BASE = base.Base()
                screen.fill(BG_COLOR)
                draw_lines()
                player = 'X'
                finished = False
                continue
            mouseX = event.pos[0] // (WIDTH // 3)
            mouseY = event.pos[1] // (HEIGHT // 3)
            if BASE.put(mouseX, mouseY, player):
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                draw_marks()
                won = BASE.get_won_player()
                if won == 'X' or won == 'O':
                    draw_winner(won)
                    finished = True
                elif BASE.is_full():
                    finished = True

    pygame.display.update()
