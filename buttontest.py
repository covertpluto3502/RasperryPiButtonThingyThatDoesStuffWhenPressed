import gpiozero

button = gpiozero.button(4)

def it_works():
    print("THE BUTTON WORKS")
    
button.pressed = it_works
