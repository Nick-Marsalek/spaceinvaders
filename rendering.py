import pygame
import pygame.image
from gamestate import GameState


# Define a Button class to create interactive buttons
class Button:
    def __init__(self, x, y, width, height, color, text, font_size, font_color):
        # Initialize button object with a rectangle, color, text, font size, and font color
        self.rect = pygame.Rect(x, y, width, height)  # Create a rectangle for the button
        self.color = color  # Set the button's color
        self.text = text  # Set the button's text
        self.font = pygame.font.Font(None, font_size)  # Load the font with the given font size
        self.font_color = font_color  # Set the font color

    def draw(self, surface):
        # Draw the button on the given surface
        pygame.draw.rect(surface, self.color, self.rect)  # Draw the button rectangle
        text = self.font.render(self.text, True, self.font_color)  # Render the text onto the button
        text_rect = text.get_rect(center=self.rect.center)  # Get the center position of the button rectangle
        surface.blit(text, text_rect)  # Blit the text onto the surface at the center position of the button rectangle

    def is_clicked(self, pos):
        # Check if the button is clicked
        return self.rect.collidepoint(pos)  # Return True if the given position is inside the button rectangle,
        # otherwise False


class Renderer:
    def __init__(self, display_surf, width, height):
        # Initialize renderer object with display surface, width and height of the screen
        self.display_surf = display_surf
        self.width = width
        self.height = height
        # Load the title and subtitle font
        self.title_font = pygame.font.Font(None, 60)
        self.subtitle_font = pygame.font.Font(None, 30)
        # Load the button font
        self.button_font = pygame.font.Font(None, 40)
        # Load the background image
        self.background_image = pygame.image.load("dog.jpg")
        # Scale the background image to fit the screen size
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        # Initialize the buttons and their rectangles
        self.play_button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 + 20, 200, 50)
        self.exit_button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 + 80, 200, 50)
        self.play_button = Button(self.play_button_rect.x, self.play_button_rect.y, self.play_button_rect.width,
                                  self.play_button_rect.height, (0, 255, 0), "Play", 40, (255, 255, 255))
        self.quit_button = Button(self.exit_button_rect.x, self.exit_button_rect.y, self.exit_button_rect.width,
                                  self.exit_button_rect.height, (255, 0, 0), "Quit", 40, (255, 255, 255))

    def render(self, state):
        # Render the menu screen
        if state == GameState.MENU:
            # Render the title and subtitle text
            title = self.title_font.render("Space Invaders", True, (255, 255, 255))
            play_button_text = self.button_font.render("Play", True, (255, 255, 255))
            exit_button_text = self.button_font.render("Exit", True, (255, 255, 255))
            # Display the background image, title and subtitle text, and buttons
            self.display_surf.blit(self.background_image, (0, 0))
            self.display_surf.blit(title, (self.width // 2 - title.get_width() // 2, self.height // 2 - 50))
            pygame.draw.rect(self.display_surf, (0, 255, 0), self.play_button_rect, 3)
            self.display_surf.blit(play_button_text,
                                   (self.width // 2 - play_button_text.get_width() // 2, self.height // 2 + 35))
            pygame.draw.rect(self.display_surf, (255, 0, 0), self.exit_button_rect, 3)
            self.display_surf.blit(exit_button_text,
                                   (self.width // 2 - exit_button_text.get_width() // 2, self.height // 2 + 95))

        elif state == GameState.GAME:
            # Render Game Stuff here later
            self.display_surf.fill((0, 0, 0))
            pass

    def handle_events(self, event):
        # Handle events such as clicking the buttons
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.play_button_rect.collidepoint(pos):
                return "play"
            elif self.exit_button_rect.collidepoint(pos):
                return "exit"
        return None
