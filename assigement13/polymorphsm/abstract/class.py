from abc import ABC, abstractmethod

class vehicle(ABC):


    @abstractmethod
    def stop():
        pass


class Bike(vehicle):
    def strat(self):
        print("Bike started.")

    def stop(self):
        print("Bike stoped.")

b1 = Bike()
b1.strat()
b1.stop()
