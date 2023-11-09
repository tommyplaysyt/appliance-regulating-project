let reading = 0
let temp_c = 0
basic.forever(function () {
    reading = pins.analogReadPin(AnalogPin.P1)
    temp_c = Math.idiv(reading * 75, 1000) - 14
    basic.showNumber(temp_c)
    basic.pause(500)
})