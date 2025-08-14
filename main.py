from djitellopy import Tello
from pynput import keyboard
import threading

tello = Tello()
tello.connect()
print(f"Battery: {tello.get_battery()}%")
# t1 = threading.Thread(target = tello.get_battery)
# t1.start()
Arrow_press_dist = 30
def controller(key):
    if key.char == "t":
        tello.takeoff()
    # elif key == keyboard.Key.up:
    #     tello.move_forward(Arrow_press_dist)
    # elif key == keyboard.Key.down:
    #     tello.move_back(Arrow_press_dist)
    # elif key == keyboard.Key.left:
    #     tello.move_left(Arrow_press_dist)
    # elif key == keyboard.Key.right:
    #     tello.move_right(Arrow_press_dist)
    elif key.char == 'u':
        tello.move_up(Arrow_press_dist)
    elif key.char == 'd':
        tello.move_down(Arrow_press_dist)
    # elif key == keyboard.Key.space:
    #     tello.land()

    else:
     if key == keyboard.Key.up:
        tello.move_forward(Arrow_press_dist)
     elif key == keyboard.Key.down:
        tello.move_back(Arrow_press_dist)
     elif key == keyboard.Key.left:
        tello.move_left(Arrow_press_dist)
     elif key == keyboard.Key.right:
        tello.move_right(Arrow_press_dist)
     elif key == keyboard.Key.space:
      tello.land()
with keyboard.Listener(on_press=controller) as listener:
    listener.join()

print("Controls:")
print("t - Takeoff")
print("Up Arrow - Forward")
print("Down Arrow - Backward")
print("Left Arrow - Left")
print("Right Arrow - Right")
print("u - Up")
print("d - Down")
print("Space - Land")