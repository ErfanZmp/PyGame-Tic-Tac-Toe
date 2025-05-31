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
CIRCLE_COLOR2 = (104, 144, 184)
CROSS_COLOR = (255, 102, 102)
CROSS_COLOR2 = (173, 120, 120)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def config_screen():
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 50)
    title_text = font.render("Select Game Mode", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - HEIGHT // 5))
    
    # Define buttons for game modes
    button_classic = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 25, WIDTH // 2, 50)
    button_advanced = pygame.Rect(WIDTH // 4, HEIGHT // 2 + HEIGHT // 10 - 25, WIDTH // 2, 50)
    
    # Render button texts
    btn_classic_text = font.render("Classic", True, (0, 0, 0))
    btn_advanced_text = font.render("Advanced", True, (0, 0, 0))
    classic_text_rect = btn_classic_text.get_rect(center=button_classic.center)
    advanced_text_rect = btn_advanced_text.get_rect(center=button_advanced.center)
    
    selecting = True
    chosen_mode = None

    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button_classic.collidepoint(pos):
                    chosen_mode = "classic"
                    selecting = False
                elif button_advanced.collidepoint(pos):
                    chosen_mode = "advanced"
                    selecting = False

        # Get current mouse position for hover detection
        mouse_pos = pygame.mouse.get_pos()

        # Redraw background and title
        screen.fill(BG_COLOR)
        screen.blit(title_text, title_rect)

        # Draw buttons with hover effect
        if button_classic.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (92, 92, 181), button_classic)
        else:
            pygame.draw.rect(screen, LINE_COLOR, button_classic)

        if button_advanced.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (92, 92, 181), button_advanced)
        else:
            pygame.draw.rect(screen, LINE_COLOR, button_advanced)

        # Blit texts on top of buttons
        screen.blit(btn_classic_text, classic_text_rect)
        screen.blit(btn_advanced_text, advanced_text_rect)

        pygame.display.update()

    return chosen_mode

def draw_board():
    screen.fill(BG_COLOR)
    draw_lines()


def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * (HEIGHT // 3)), (WIDTH, i * (HEIGHT // 3)), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * (WIDTH // 3), 0), (i * (WIDTH // 3), HEIGHT), LINE_WIDTH)


def draw_cross(x, y, color=CROSS_COLOR):
    pygame.draw.line(screen, color, (x - RADIUS, y - RADIUS), (x + RADIUS, y + RADIUS), MARK_WIDTH + 5)
    pygame.draw.line(screen, color, (x - RADIUS, y + RADIUS), (x + RADIUS, y - RADIUS), MARK_WIDTH + 5)


def draw_marks():
    for row in range(3):
        for col in range(3):
            if BASE.get_mark(row, col) == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (row * (WIDTH // 3) + (WIDTH // 6),
                                    col * (HEIGHT // 3) + (HEIGHT // 6)),
                                   RADIUS, MARK_WIDTH)
            elif BASE.get_mark(row, col) == 'o':
                pygame.draw.circle(screen, CIRCLE_COLOR2,
                                   (row * (WIDTH // 3) + (WIDTH // 6),
                                    col * (HEIGHT // 3) + (HEIGHT // 6)),
                                   RADIUS, MARK_WIDTH)
            elif BASE.get_mark(row, col) == 'X':
                draw_cross(row * (WIDTH // 3) + (WIDTH // 6),
                           col * (HEIGHT // 3) + (HEIGHT // 6))
            elif BASE.get_mark(row, col) == 'x':
                draw_cross(row * (WIDTH // 3) + (WIDTH // 6),
                           col * (HEIGHT // 3) + (HEIGHT // 6),
                           color=CROSS_COLOR2)


def set_won(won_player):
    won_coordinate = BASE.get_won_coordinate()
    color = CROSS_COLOR if won_player == 'X' else CIRCLE_COLOR
    pygame.draw.line(screen, color,
                     (won_coordinate[0][1] * (WIDTH // 3) + (WIDTH // 6),
                      won_coordinate[0][0] * (HEIGHT // 3) + (HEIGHT // 6)),
                     (won_coordinate[1][1] * (WIDTH // 3) + (WIDTH // 6),
                      won_coordinate[1][0] * (HEIGHT // 3) + (HEIGHT // 6)),
                     LINE_WIDTH)
    font = pygame.font.Font(None, 80)
    text = font.render(f"{won_player} wins!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.set_caption(f"Tic Tac Toe - {won_player} won!")

def set_draw():
    font = pygame.font.Font(None, 80)
    text = font.render("It's a draw!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.set_caption("Tic Tac Toe - Draw")
    
def refresh_player(player):
    pygame.display.set_caption(f"Tic Tac Toe - {player}'s turn")

mode = config_screen()
BASE = base.Base(mode=mode)
draw_board()
player = 'X'
finished = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if finished:
                mode = config_screen()
                BASE = base.Base(mode=mode)
                draw_board()
                player = 'X'
                refresh_player(player)
                finished = False
                continue
            mouseX = event.pos[0] // (WIDTH // 3)
            mouseY = event.pos[1] // (HEIGHT // 3)
            if BASE.put(mouseX, mouseY, player):
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                refresh_player(player)
                draw_board()
                draw_marks()
                won = BASE.get_won_player()
                if won == 'X' or won == 'O':
                    set_won(won)
                    finished = True
                elif BASE.is_full():
                    set_draw()
                    finished = True

    pygame.display.update()
