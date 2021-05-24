from machine import Pin# importng machine module
from machine import UART# importng UART(Universal Asynchronous Receiver) module
from time import sleep#importing sleep from time module
HC05=UART(0,9600)#creating an object HC05 and declaring UART communication channel,boud rate
relay_1=Pin(28,Pin.OUT)#creating an Object relay_1 and assign Pin 28 as an OUTPUT
relay_2=Pin(20,Pin.OUT)#creating an Object relay_2 and assign Pin 20 as an OUTPUT
relay_3=Pin(18,Pin.OUT)#creating an Object relay_1 and assign Pin 18 as an OUTPUT
relay_4=Pin(19,Pin.OUT)#creating an Object relay_2 and assign Pin 19 as an OUTPUT
while True:# creating an infinite loop to checking is there is any data availabel?
    if HC05.any()>0:
        data=HC05.read(1)#creating a variable(data)and saving the availabel data from Hc05.
        if "a" in data:#condition checking-if available data is (a)
            relay_1.on()#command for relay_1 ON
            #relay_1.value(1)#command for relay_1 ON
        if "b" in data:#condition checking-if available data is (b)
            relay_1.off()#command for relay_1 OFF
            #relay_1.value(0)#command relay_1 OFF
        if "c" in data:#condition checking-if available data is (c)
            relay_2.on()#command for relay_2 ON
            #relay_2.value(1)#command relay_2 ON
        if "d" in data:#condition checking-if available data is (d)
            relay_2.off()#command for relay_2 OFF
            #relay_2.value(0)#command for relay_2 OFF
        if "e" in data:#condition checking-if available data is (e)
            relay_3.on()#command for relay_3 ON
            #relay_3.value(1)#command for relay_3 ON
        if "f" in data:#condition checking-if available data is (f)
            relay_3.off()#command for relay_3 OFF
            #relay_3.value(0)#command for relay_3 OFF
        if "g" in data:#condition checking-if available data is (g)
            relay_4.on()#command for relay_4 ON
            #relay_4.value(1)#command for relay_4 ON
        if "h" in data:#condition checking-if available data is (h)
            relay_4.off()#command for relay_4 OFF
            #relay_4.value(0)#command for relay_4 OFF    
            
            
            
            
            