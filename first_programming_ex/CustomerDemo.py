# This module tests the Customer class
def demoCustomer():
    import argparse
    import textwrap
    from customer import Customer
    parser = argparse.ArgumentParser(prog='my test program',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=textwrap.dedent('''\
                                                 Customer
                                     --------------------------------
                                     A simulated marketing loyalty programm that informs wether or not the customer has a discount in his next purchase.

                                     Methods:
                                     1) makePurchase:  Makes a purchase of certain amount and prints wether or not the customer has a discount in his next purchase.
                                                       If the customer had a discount, the programm prints the new amount to be paid
                                        @param amount: amount of the purchase

                                     2) discountReached: prints wether or not the customer has a discount and resets the purchase value to 0
                                     '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                     --------------------------------
                                      Customer1 = Customer(args.init_price) # initialize a Customer
                                      Customer1.makePurchase(100) # add an item
                                      Customer1.discountReached() # Informs the amount missing until the next discount
                                     ''')
                    )

    parser.add_argument('--init_price', default=0.0, type=float)
    parser.add_argument('--run_demo', action='store_true', help='runs this demo')
    args = parser.parse_args()

    if args.run_demo:
        customer1 = Customer(args.init_price)
        customer1.makePurchase(80)
        print('Expected: No discount')
        customer1.makePurchase(80)
        print('Expected: Discount')
        customer1.makePurchase(95)
        print('Expected: New amount with discount\n', 'Expected: no new discount')

demoCustomer()