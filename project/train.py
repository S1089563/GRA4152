from NeuralNetworks import NeuralNetwork, ConvNN, FullyConNN
from dataloader import DataLoader, MNIST, CIFAR10
from sklearn.metrics import roc_auc_score
import argparse

parser = argparse.ArgumentParser(description="Program test of Neural Networks and Data Loader classes")

# Parser that gives documentation of specific classes
doc_group = parser.add_argument_group('Documentation Options')
doc_group.add_argument('--doc', action='store_true', help='Retrieves the documentation for the class')
doc_group.add_argument('--class_name', choices=['NeuralNetwork', 'DataLoader', 'MNIST', 'ConvNN', 'FullyConNN', 'CIFAR10'],
                    help='Display the docstring of a specified class')
doc_group.add_argument('--methods', action='store_true', help='Shows the documentation for each method')


# Parser group used to test the functionality of the program
test_group = parser.add_argument_group('Test Options')
test_group.add_argument('--test', action='store_true', help='Runs the test with specified parameters')
test_group.add_argument('--dset', choices=['cifar10', 'mnist'], help="Choose dataset for the training and testing")
test_group.add_argument('--nn_type', choices=['FullyConNN', 'ConvNN'],
                        help="Choose the model type for the classification task")
test_group.add_argument('--epochs', default=10, type=int, help="Select the number of epochs to train the model")
test_group.add_argument('--neurons', default=50, type=int,
                        help="Choose the number of neurons in the hidden layers of the model.")
test_group.add_argument('--batch_size', default=256, type=int, help="Choose the batch_size for model training.")

# Argument parser
args = parser.parse_args()


# Function to display the class documentation
def docstring(class_name, method):
    try:
        cls = globals()[class_name]
        print(f'Documentation of {class_name}:{cls.__doc__}\n')
        if method:
            for attr_name in dir(cls):
                attr = getattr(cls, attr_name)
                if not attr_name.startswith('_'):
                    print(f"Documentation of the method {attr_name}: {attr.__doc__}\n")

        for subclass in cls.__subclasses__():
            docstring(subclass.__name__, method)

    except KeyError:
        print('Class not found.')


# Function to test the program functionality
def test(dset, nn_type, epochs, neurons, batch_size):
    # Choosing the correct dataset
    if dset == 'cifar10':
        data = CIFAR10()
    elif dset == 'mnist':
        data = MNIST()

    # Loading the batches of data
    slices = data.loder(batch_size)

    # Choosing the correct class to create
    if nn_type == "ConvNN":
        model = ConvNN(neurons=neurons)
    elif nn_type == "FullyConNN":
        model = FullyConNN(neurons=neurons)

    # Training the model
    step = 0
    while step < epochs:
        for i, data_batch in enumerate(slices):
            losses = model.train(data_batch)
        step += 1

    # Evaluating model results
    pi_hat, y_hat = model.test(data.x_te)
    auc = roc_auc_score(data.y_te, pi_hat)
    print('Final AUC: %0.4f' % auc)


# Parser documentation
if args.doc:
    docstring(args.class_name, args.methods)

# Parser testing
if args.test:
    test(dset=args.dset, nn_type=args.nn_type, epochs=args.epochs, neurons=args.neurons, batch_size=args.batch_size)
