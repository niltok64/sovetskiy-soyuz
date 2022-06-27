def on_button_pressed_a():
    basic.show_string("sovetskiy soyuz", interval=100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_leds("""
        . # # # .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
    """)
basic.forever(on_forever)
