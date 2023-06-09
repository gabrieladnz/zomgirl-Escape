import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

# estilo do texto
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 22
FONT_STYLE = "freesansbold.ttf"


# função da mensagem com seus parâmetros
def draw_message_component(
    message,
    screen,
    font_color=FONT_COLOR,
    font_size=FONT_SIZE,
    # coordenada vertical e mantém no centro da tela
    pos_y_center=SCREEN_HEIGHT // 2,
    # coordenada horizontal
    pos_x_center=SCREEN_WIDTH // 2
):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    # exibe a mensagem
    screen.blit(text, text_rect)
