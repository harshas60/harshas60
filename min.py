import random
import pyautogui as pg
import time

# List of animals
animals = ('monkey', 'cat', 'donkey')

# Wait 8 seconds to give time to switch to the target window
time.sleep(8)

# Number of messages to send
messages_to_send = 10  # Reduce from 500 for safer testing

for i in range(messages_to_send):
    try:
        animal = random.choice(animals)
        pg.write(f"You are a {animal}")
        pg.press('enter')
        time.sleep(0.5)  # Add delay between messages
    except Exception as e:
        print(f"An error occurred: {e}")
        break