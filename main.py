import machine
import time
 
led1 = machine.Pin(16, machine.Pin.OUT)
led2 = machine.Pin(14, machine.Pin.OUT)
led3 = machine.Pin(13, machine.Pin.OUT)

botao = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
botao3 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
 
 
while (True):
    estado1 = botao.value()
    estado2 = botao2.value()
    estado3 = botao3.value()
 
    if estado1 == 0:
       led1.on()
    else:
       led1.off()


    if estado2 == 0:
       led2.on()
    else:
       led2.off()


    if estado3 == 0:
       led3.on()
    else:
       led3.off()
    
    time.sleep (0.15)