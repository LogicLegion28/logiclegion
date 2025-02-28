import pygame
import speech_recognition as sr
import pyttsx3
import time

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = WIDTH // 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Audio-Guided Maze")

# Colors
WHITE = (255, 255, 255)  # Walkable area
GREEN = (0, 255, 0)  # Start (Class 1)
RED = (255, 0, 0)  # End (Appears after reaching final position)
BLUE = (0, 0, 255)  # Player

# Maze Grid (No Obstacles)
maze = [
    ["S", " ", " ", " ", " "],  # S = Start (Class 1)
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]  # End will be placed at the final stop
]

# Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen_for_reached():
    """Use voice recognition to detect 'Reached'."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'Reached' to continue...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            if "reached" in command:
                return True
        except sr.UnknownValueError:
            print("Didn't catch that. Try again.")
        except sr.RequestError:
            print("Could not connect to recognition service.")
    return False

# Navigation Instructions
instructions = [
    "Move forward one step",
    "Move forward one step",
    "Move forward one step",
    "Move right one step",
    "Move forward one step"
]

# Player Position
player_x, player_y = 0, 0
library_x, library_y = None, None  # Library appears at last "Reached" position

# Game Loop
running = True
step_count = 0
font = pygame.font.Font(None, 36)

while running:
    screen.fill(WHITE)  # Background color

    # Draw maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = WHITE
            if maze[row][col] == "S":
                color = GREEN
            if (col, row) == (library_x, library_y):  # Show red box only after reaching
                color = RED
            pygame.draw.rect(screen, color, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

    # Draw player
    pygame.draw.circle(screen, BLUE, (player_x * BLOCK_SIZE + BLOCK_SIZE // 2, player_y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 3)

    # Display instruction
    if step_count < len(instructions):
        text_surface = font.render(f"Instruction: {instructions[step_count]}", True, (0, 0, 0))
        screen.blit(text_surface, (20, HEIGHT - 50))
    
    pygame.display.flip()

    if step_count < len(instructions):
        speak(instructions[step_count])
        print(f"Instruction: {instructions[step_count]}")

        while not listen_for_reached():  # Wait until user says "Reached"
            print("Please say 'Reached' to continue.")

        # Move player based on step count
        if step_count in [0, 1, 2, 4]:  # Forward movement
            player_y += 1
        elif step_count == 3:  # Right movement
            player_x += 1

        step_count += 1
    else:
        # Set library position at final player position
        library_x, library_y = player_x, player_y
        speak("You have reached your final position. Navigation complete.")
        pygame.display.flip()
        time.sleep(2)
        running = False

pygame.quit()
