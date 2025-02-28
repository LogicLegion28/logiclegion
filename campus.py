import pygame
import speech_recognition as sr
import pyttsx3
import time

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Audio-Guided Maze")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Maze Grid
maze = [
    ["S", " ", " ", "X", " "],  # S = Start (Class 1)
    ["X", "X", " ", "X", " "],
    [" ", " ", " ", " ", " "],
    ["X", "X", "X", "X", " "],
    [" ", " ", " ", "X", "E"]  # E = End (Library)
]

# Block size
BLOCK_SIZE = WIDTH // len(maze[0])

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
    "Move 1 step forward",
    "Move 1 step forward",
    "Move 1 step right",
    "Move 1 step forward",
    "Move 1 step forward to reach the library"
]

# Player Position
player_x, player_y = 0, 0

# Game Loop
running = True
step_count = 0
while running:
    screen.fill(WHITE)

    # Draw maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = WHITE if maze[row][col] == " " else BLACK
            if maze[row][col] == "S":
                color = BLUE
            elif maze[row][col] == "E":
                color = RED
            pygame.draw.rect(screen, color, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x * BLOCK_SIZE, player_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()

    if step_count < len(instructions):
        speak(instructions[step_count])
        print(f"Instruction: {instructions[step_count]}")

        while not listen_for_reached():  # Wait until user says "Reached"
            print("Please say 'Reached' to continue.")

        step_count += 1

        # Move player in the grid
        if step_count == 1 or step_count == 2 or step_count == 4:
            player_y += 1  # Move forward
        elif step_count == 3:
            player_x += 1  # Move right

    else:
        speak("You have reached the library. Navigation complete.")
        time.sleep(2)
        running = False

pygame.quit()
