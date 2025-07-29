class ClaseA:
    def say_hello(self):
        print('>>> Hola, soy ClaseA')

class ClaseB:
     def say_hello(self):
        print('>>> Hola, soy ClaseB')

     def say_goodbay(self):
        print('>>> Adiós, soy ClaseB')

class ClaseC(ClaseA, ClaseB):
    ...

c = ClaseC()
c.say_hello()
c.say_goodbay()