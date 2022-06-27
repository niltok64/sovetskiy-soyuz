input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("sovetskiy soyuz", 100)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.clearScreen()
})
basic.forever(function on_forever() {
    basic.showLeds(`
        . # # # .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
    `)
})
