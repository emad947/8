add=0

def on_gesture_shake():
    global add
    add = 5+10
    basic.show_number(add)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)