from abc import ABC, abstractmethod
class car (ABC):
    def paySlip(self, amount):
        print("your purchase amount: " ,amount)
#this function is telling us to pass in an argument but we wont tell you
#how or what kind of data it will be.

    @abstractmethod
    def payment(self, amount):
        pass
class DebitCardPayment(car):
#here we define how to implement thr payment function from its parent paySlip class.
     def payment (self, amount):
         print('your purchase amount of {} exceeded your$200 limit'.format(amount))

obj=DebitCardPayment()
obj.paySlip('$400')
obj.payment('$400')
