import keyboard as kb
import time

t1 = time.time()

for i in range(0, 10):
    event = kb.read_event(suppress=False)
    t2 = time.time()
    print(f'pressed {event} at {str(t2-t1)[0:5]} seconds')
