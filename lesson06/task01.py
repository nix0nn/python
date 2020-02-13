from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = {'красный': 7, 'желтый': 2, 'зеленый': 7}

    def running(self):
        for x in cycle(self.__color):
            if x == 'красный':
                print(x)
                sleep(self.__color['красный'])
            elif x == 'желтый':
                print(x)
                sleep(self.__color['желтый'])
            elif x == 'зеленый':
                print(x)
                sleep(self.__color['зеленый'])


a = TrafficLight()
a.running()

