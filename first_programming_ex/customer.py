# This module defines the customer class. Models a customer loyalty campaign
# that gives a $10 discount after the customer has spend more than a $100
class Customer:
    
    ## Contructor method for the class Customer with an optional initial purchase.
    ## @param initialPurchase: amount of the first purchase
    def __init__(self, initialPurchase=0):
            self._amountPurchase = initialPurchase
            self._discount = False
            self.discountReached()
    
    ## Makes a purchase of certain amount and prints wether or not the customer has a discount in his next purchase
    ## If the client had a discount, the program prints the new value to pay.
    ## @param amount: amount of the purchase
    def makePurchase(self, amount):
         if self._discount:
              print('You had a $10 discount, the new amount to pay is: $' + str(max(0,amount-10)))
              self._discount = False
              self._amountPurchase += max(0, amount - 10)
         else:
              self._amountPurchase += amount
         self.discountReached()

    ## Prints wether or not the customer has a discount and resets the purchase value to 0
    def discountReached(self):
        if self._amountPurchase >= 100:
            print('Congratulations, you have earned a $10 discount on your next purchase!')
            self._discount = True
            self._amountPurchase = 0
        else:
             print('You need to spend: ', '$'+str(100 - self._amountPurchase), ' to earn a discount on your next purchase')