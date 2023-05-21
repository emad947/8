let add = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    add = 5 + 10
    basic.showNumber(add)
})
