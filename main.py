import keyboard as kb
import time

start = time.time()
t1 = time.time()
end = t1 + 60

while True:
    event = kb.read_event(False)
    print(
         f'{event} pressed {event.name} at {str(event.time - t1)[0:6]}')
    start = time.time()
    if end <= start:
        break
