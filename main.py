import pygame
import sys
from gamestate import GameState
from rendering import Renderer, Button


def on_cleanup():
    # Clean up the Pygame library when the game is done
    pygame.quit()


class Game:
    def __init__(self):
        # Initialize the Pygame library and set the window caption
        pygame.init()
        pygame.display.set_caption("Space Invaders")

        # Set the window icon
        icon = pygame.image.load("Assets/enemy2.png")
        pygame.display.set_icon(icon)

        # Set the width and height of the game window
        self.width = 800
        self.height = 600

        # Create a display surface object to draw on
        self._display_surf = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)

        # Set the initial game state to the menu screen
        self.state = GameState.MENU

        # Create a renderer object to draw the game
        self.renderer = Renderer(self._display_surf, self.width, self.height)

    def on_event(self, event):
        # Handle events such as quitting the game
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.state == GameState.MENU:
                    # Check if play or quit button is clicked
                    x, y = event.pos
                    if self.renderer.play_button.is_clicked((x, y)):
                        # If play button is clicked, start the game
                        self.state = GameState.LEVEL_ONE
                    elif self.renderer.quit_button.is_clicked((x, y)):
                        # If quit button is clicked, exit the game
                        sys.exit()

    def on_render(self):
        # Render the current game state using the renderer
        self.renderer.render(self.state)

        # Update the display surface to show the new frame
        pygame.display.flip()

    def run_game(self):
        # Main game loop
        while True:
            # Handle events such as quitting the game
            for event in pygame.event.get():
                self.on_event(event)

            # Render the current game state
            self.on_render()

        # Clean up the Pygame library when the game is done
        on_cleanup()


if __name__ == "__main__":
    # Create a new game object and run the game
    theGame = Game()
    theGame.run_game()
