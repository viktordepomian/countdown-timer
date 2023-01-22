import time

# Set the countdown timer for 10 seconds
countdown_timer = int(input('Please input a number to start the counter: '))

while countdown_timer > 0:
    print(countdown_timer)
    countdown_timer -= 1
    time.sleep(1)

print("Time's up!")
