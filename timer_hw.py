import time
from datetime import datetime


# 1-Creating a class
class Timer:
    # 2-Implementing the __init__ method to initialize all specified fields
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.started_at = datetime.now()

    # 3-Implementing the __str__ method so that it returns a friendly message in the format:
    def __str__(self):
        return f'Timer \033[92m{self.name}\033[0m set for \033[92m{self.duration}\033[0m minutes (started at : \033[92m{self.started_at}\033[0m) '

    # 4-Implement the __repr__ method so that it returns Python code that can recreate the object.
    def __repr__(self):
        return f"Timer('{self.name}',{self.duration})"

    # 5-Implementing the __del__ method so that once the object is deleted, a message will appear
    def __del__(self):
        print(f'goodbye \033[92m{self.name}\033[0m')


timer1 = Timer("Workout", 45)
timer2 = Timer("Study", 30)

print(f'(\033[35m question 6: \033[0m)')
print()
# 6-Add an attribute dynamically (e.g. paused = False) and then remove it from the object.
timer1.paused =  False
print(f"Paused attribute added to {timer1.name}: {timer1.paused}")
print()
del timer1.paused

try:
    print(timer1.paused)
except AttributeError:
    print(f"'paused' attribute was removed from {timer1.name}.")
print()
print(f'(\033[34m question 7: \033[0m)')
# 7-Save all timers in the list and print it. Make sure that the use of __repr__ is automatically enabled when printing the list.
timers = [timer1, timer2]
print(timers)
print()
# ----------------------------------------------#
print(f'\033[36m --Bonus Challenge-- \033[0m')
# ----------------------------------------------#
print()
print(f'(\033[52m question 1 - Bonus : \033[0m)')
print()
# 1-Using time.sleep(1) to simulate a running timer
time.sleep(1)
print("1 second passed...")
time.sleep(1)
print("2 seconds passed...")
print()
print(f'(\033[52m question 2 - Bonus : \033[0m)')
print()
# 2-Calculate and print how many seconds have passed since the timer started
seconds_passed = (datetime.now() - timer1.started_at).total_seconds()
print(f"{int(seconds_passed)} seconds since timer started.")
print()
print(f'(\033[52m question 3 - Bonus : \033[0m)')
print()
# 3-Replicating a timer using eval(repr(t)) and checking that the replica is identical
clone = eval(repr(timer1))
print(f"Clone created: {clone}")
print("Same name:", clone.name == timer1.name)
print("Same duration:", clone.duration == timer1.duration)
