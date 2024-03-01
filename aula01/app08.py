# LED


def main():
    x = int(input(""))
    for i in range(x):
        ledsTotal = processa()
        print(f'{ledsTotal} leds')

def entrada():
    line = input("")
    return line

def processa():
    ledsTotal = 0
    led = 0
    values = entrada()
    for value in values:
        if int(value) == 1:
            led = 2
        elif int(value) == 2:
            led = 5
        elif int(value) == 3:
            led = 5
        elif int(value) == 4:
            led = 4
        elif int(value) == 5:
            led = 5
        elif int(value) == 6:
            led = 6
        elif int(value) == 7:
            led = 3
        elif int(value) == 8:
            led = 7
        elif int(value) == 9:
            led = 6
        elif int(value) == 0:
            led = 6
        ledsTotal+=led
    return ledsTotal


main()