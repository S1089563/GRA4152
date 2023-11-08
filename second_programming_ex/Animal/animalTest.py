from animal import Animal
from dog import Dog
from cat import Cat
from BigDog import BigDog
import argparse
import textwrap


def demoAnimal():
    parser = argparse.ArgumentParser(prog='Animal test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                                      Animal
                                          --------------------------------
                                          A simulated Animal program. Prints the sound that each animal makes.
                                          Animal can be of 3 classes: Cat, Dog or BigDog

                                          Instance methods:

                                          1) greets:  returns the greet of the animal

                                          '''),
                                     epilog=textwrap.dedent('''\
                                                     Usage
                                          --------------------------------
                                           Instance methods:
                                           firulais = BigDog()
                                           firualis.greets()

                                          ''')
                                     )
    parser.add_argument('--run_demo', action='store_true', help='runs a demo')
    args = parser.parse_args()

    if args.run_demo:
        gato = Cat()
        perro = Dog()
        perrote = BigDog()
        print("\nCat:")
        gato.greets()
        print("Expected:\nmeow")
        print("\nDog:")
        perro.greets()
        print("Expected:\nwoof")
        print("\nBig Dog:")
        perrote.greets()
        print("Expected:\nwoof\nwoooof")


demoAnimal()
