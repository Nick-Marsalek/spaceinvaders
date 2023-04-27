import sys
import pygame

pygame.init()
pygame.display.set_caption("Game Over")

# Set up the font
FONT_SIZE = 48
SCORE_FONT = pygame.font.Font("Assets/8bitfont.ttf", FONT_SIZE)

def get_best_scores():
    # Open the file and read the scores
    with open('scores.txt', 'r') as f:
        scores = [int(line.strip()) for line in f.readlines()]

    # Sort the scores in descending order
    scores.sort(reverse=True)

    return scores[:3]

def add_score_to_file(score):
    # Open the file and append the score
    with open('scores.txt', 'a') as f:
        f.write(str(score) + '\n')

def game_over(display_surface, score):
    # Add the current score to the file
    show_score = score
    add_score_to_file(score)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

            # Check for the exit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if exit_button_rect.collidepoint(mouse_pos):
                    sys.exit()

        display_surface.fill((0, 0, 0))

        # Display the score
        score_text = SCORE_FONT.render(f"Score: {show_score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(800 // 2, 600 // 2 - FONT_SIZE))
        display_surface.blit(score_text, score_rect)

        # Display the best scores
        best_scores = get_best_scores()
        best_scores_text = SCORE_FONT.render("Best Scores:", True, (255, 255, 255))
        display_surface.blit(best_scores_text, (50, 50))
        y = 100
        for i, score in enumerate(best_scores):
            score_text = SCORE_FONT.render(f"{i+1}. {score}", True, (255, 255, 255))
            display_surface.blit(score_text, (50, y))
            y += FONT_SIZE

        # Draw the exit button
        exit_button_text = SCORE_FONT.render("Exit", True, (255, 255, 255))
        exit_button_rect = exit_button_text.get_rect(center=(800 // 2, 600 // 2 + FONT_SIZE))
        pygame.draw.rect(display_surface, (255, 0, 0), exit_button_rect, 2)
        display_surface.blit(exit_button_text, exit_button_rect)

        pygame.display.flip()
