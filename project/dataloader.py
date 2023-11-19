import tensorflow as tf
import numpy as np


class DataLoader:
    """
    Superclass in which the data loading and transformation is implemented.
    """

    def __init__(self):
        """
        Constructor method for the class
        This is an abstract method that is going to be overriden by the subclasses.
        Depends on the data set that is going to be used
        Data will always be tuple with two tuples inside
        """
        self._data = None

    @property
    def data(self):
        """
        Method to access the data
        the @property decorator is used so the data can be access easily with self.data.

        @:returns data as a tuple with two tuples inside
        """
        return self._data

    @property
    def x_tr(self):
        """
        Method to access the training dataset of the x variables
        This dataset con be found in the first position of the first tuple of data
        the method takes the loaded dataset normalizes it dividing it by 255 and finally converts it to float32 type
        the @property decorator is used so the data can be access easily with self.x_tr

        @:return training dataset of the independent variables X
        """
        x_tr = np.float32(np.asarray(self._data[0][0]) / 255)
        return x_tr

    @property
    def y_tr(self):
        """
        Method to access the training dataset of the dependent variable y
        This dataset con be found in the second position of the first tuple of data
        the method takes the loaded dataset and transforms it to a categorical variable with 10 categories
        the @property decorator is used so the data can be access easily with self.y_tr

        @:return training dataset of the dependent variable Y
        """
        y_tr = tf.keras.utils.to_categorical(self._data[0][1], 10)
        return y_tr

    @property
    def x_te(self):
        """
        Method to access the test dataset of the x variables
        This dataset con be found in the first position of the second tuple of data
        the method takes the loaded dataset normalizes it dividing it by 255 and finally converts it to float32 type
        the @property decorator is used so the data can be access easily with self.x_te

        @:return test dataset of the independent variables X
        """
        x_te = np.float32(np.asarray(self._data[1][0]) / 255)
        return x_te

    @property
    def y_te(self):
        """
        Method to access the test dataset of the dependent variable y
        This dataset con be found in the second position of the second tuple of data
        the method takes the loaded dataset and transforms it to a categorical variable with 10 categories
        the @property decorator is used so the data can be access easily with self.y_te

        @:return test dataset of the dependent variable X
        """
        y_te = tf.keras.utils.to_categorical(self._data[1][1], 10)
        return y_te

    def loder(self, batch_size):
        """
        Method that creates the batches of data to be trained in the neural network. This method splits X and Y training
        datasets in the specified number of batches that receives as an input and returns a list of tuples with those
        batches.

        @:param batch_size number of batches the dataset

        @:return list of tuples with length = batch_size with the corresponding X and Y training sets.
        """
        tf_dl = tf.data.Dataset.from_tensor_slices((self.x_tr, self.y_tr)).shuffle(self.x_tr.shape[0]).batch(batch_size)
        return tf_dl


class MNIST(DataLoader):
    """
    Subclass of dataloader. This class inherits all the methods of dataloader, and it's used to load and transform the
    MNIST dataset from keras.
    """

    def __init__(self):
        """
        Constructor method of the class MNIST. This method overrides the one in the superclass DataLoader and extends
        the functionality in order to load the MNIST dataset.
        """
        super().__init__()
        self._data = tf.keras.datasets.mnist.load_data()

    @property
    def x_tr(self):
        """
        Method to access the training dataset of the x variables. This method overrides the method in DataLoader and
        extends its functionality by flattening the array that its return.
        This dataset con be found in the first position of the first tuple of data
        the method takes the loaded dataset normalizes it dividing it by 255 and finally converts it to float32 type.
        Finally, this method flattens the array of 28*28 to return a one dimensional 784 array.
        the @property decorator is used so the data can be access easily with self.x_tr

        :return: flatten training dataset of the dependent variable X.
        """
        x_tr = np.reshape(super().x_tr, (60000, 784))
        return x_tr

    @property
    def x_te(self):
        """
        Method to access the test dataset of the x variables. This method overrides the method in DataLoader and
        extends its functionality by flattening the array that its return.
        This dataset con be found in the first position of the second tuple of data
        the method takes the loaded dataset normalizes it dividing it by 255 and finally converts it to float32 type.
        Finally, this method flattens the array of 28*28 to return a one dimensional 784 array.
        the @property decorator is used so the data can be access easily with self.x_te

        :return: flatten test dataset of the dependent variable X.
        """
        x_te = np.reshape(super().x_te, (10000, 784))
        return x_te


class CIFAR10(DataLoader):
    """
    Subclass of dataloader. This class inherits all the methods of dataloader, and it's used to load the CIFAR10 dataset
    from keras.
    """

    def __init__(self):
        """
        Constructor method of the class CIFAR10. This method overrides the one in the superclass DataLoader and extends
        the functionality in order to load the CIFAR10 dataset.
        """
        super().__init__()
        self._data = tf.keras.datasets.cifar10.load_data()
