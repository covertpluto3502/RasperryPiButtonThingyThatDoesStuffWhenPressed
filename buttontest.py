import gpiozero

button = gpiozero.Button(4)

def it_works():
    print("THE BUTTON WORKS")
    
button.when_pressed = it_works
