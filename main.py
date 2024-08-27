# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
b_up = Pin(32, Pin.IN, Pin.PULL_UP)
b_down = Pin(33, Pin.IN, Pin.PULL_UP)
b_enter = Pin(25, Pin.IN, Pin.PULL_UP)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

print("hola")
def mostrar(s):
    oled.fill(0)
    oled.text('Hello, World 1!', s, 0,)
    oled.text('Hello, World 2!', s, 10)
    oled.text('Hello, World 3!', s, 20)
    oled.text('Hello, World 4!', s, 30)
    oled.text('Hello, World 5!', s, 40)
    oled.text('Hello, World 6!', s, 50) 
    oled.show()

scroll = -128
while True:
    #print(b_enter.value())
    
    while b_enter.value()==True:
        scroll += 1
        if scroll > 128:
            scroll = -128
        mostrar(scroll)        
         
    
    



