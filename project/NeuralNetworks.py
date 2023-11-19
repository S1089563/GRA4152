import tensorflow as tf
from keras import layers
from keras import Sequential


class NeuralNetwork(tf.keras.Model):
    """
    The NeuralNetwork is created to extend the tf.keras.Model class
    The NeuralNetwork superclass has 2 subclasses FullyConNN and ConvNN, these are different neural network model.
    The NeuralNetwork class inherits from the tf.keras.Model class
    """

    def __init__(self, neurons):
        """
        The constructor of the superclass inherits the constructor from the tf.keras.Model class In addition,
        the constructor creates hidden, cls, params and neurons instance variables. Neurons instance variable is
        created in the superclass because we need the parameter both for the classifier and hidden_layer method.
        Hidden_layer method is only implemented in the subclass. @params: -neurons: the number of neurons for each
        layer in the hidden layers and the classifier
        """
        super().__init__()
        self._hidden = object()
        self._cls = object()
        self._params = None
        self._neurons = neurons

    def __repr__(self):
        """
        This method prints information about the class. This is an abstract method, implemented later in the subclass.
        """
        raise NotImplementedError

    def _hidden_layer(self):
        """
        This method returns the hidden layers for a neural network. This is an abstract method, implemented later in the
        subclass.
        """
        raise NotImplementedError

    def _call(self, inputs):
        """
        This method returns the loss function based on the hidden and cls and the input values.
        @params: inputs (x,y) tuple where x is the input data and y is the result.
        @returns: the hidden layer object
        """
        hidden = self._hidden
        cls = self._cls
        x, y = inputs
        out = hidden(x)
        out = cls(out)
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, out))
        return loss

    def _classifier(self, y_dim=10):
        """
        This method defines the classifier layer in the neural network. This layer is the same for both subclasses.
        @params: y_dim the number of classes in the classification task
        @returns: the classifier layer object.
        """
        cls = Sequential([layers.InputLayer(input_shape=self._neurons),
                          layers.Dense(y_dim, activation='softmax')])
        return cls

    def train(self, inputs, optimizer=tf.keras.optimizers.Adam(learning_rate=5e-4)):
        """
        The train helps to train the model with the training data.
        @params:
            inputs: (x_tr, y_tr) x training, y training data pairs to train the model.
            optimizer: optimizer algorithm to improve the weights in the neural networks. The default is Adam.
        @returns: the loss function of the neural network
        """
        params = self._params
        with tf.GradientTape() as tape:
            loss = self._call(inputs)
        gradients = tape.gradient(loss, params)
        optimizer.apply_gradients(zip(gradients, params))
        return loss

    def test(self, x):
        """
        The test method returns the estimated class and the probability for each class based on the trained model and the
        x_te input
        @params: x is the matrix with the test input values.
        @return:
            pi_hat: the probability vector for each class
            y_hat: the estimated category by the model.
        """
        out = self._hidden(x)
        out = self._cls(out)
        pi_hat = out
        y_hat = tf.math.argmax(out, 1)
        return pi_hat, y_hat

    def _set_hidden(self, set_hidden):
        """
        This method sets the hidden instance variable to a new object.
        @params: set_hidden the new object the user wants to have as hidden layer.
        """
        self._hidden = set_hidden

    def _set_params(self, set_param):
        """
        This method sets the params instance variable to a new value. This is necessary to train the model.
        @params: -set_param the new object for params.
        """
        self._params = set_param

    def _set_cls(self, set_cls):
        """
        This method sets the cls instance variable to a new object.
        @params: set_cls the new object the user wants to have as classifier layer.
        """
        self._cls = set_cls


class FullyConNN(NeuralNetwork):
    """
    The FullyConNN is the subclass of the NeuralNetwork class. The abbreviation stands for fully connected neural network.
    The FullyConNN class inherits from the NeuralNetwork class.
    """

    def __init__(self, neurons=50, input_shape=28 * 28):
        """
        In the constructor the FullyConNN class inherits the superclass' constructor. Moreover, the hidden layer, cls
        and params instance variable get the class specific value.

        @params:
            neurons: the number of neurons for each layer in the hidden layers and the classifier
            input_shape: the shape of the input parameters
        """
        super().__init__(neurons)
        hidden_layer = self._hidden_layer(input_shape=input_shape)
        self._set_hidden(hidden_layer)
        self._set_cls(self._classifier())
        self._set_params(self._cls.trainable_variables + self._hidden.trainable_variables)

    def __repr__(self):
        """
        This method returns some text with the name of the class.
        @returns: text with the class name
        """
        return f"The neural network is a fully connected neural network"

    def _hidden_layer(self, input_shape):
        """
        This method overrides the abstract method in the superclass. Creates a fully connected neural network hidden
        layer.
        @params: input_shape the shape of the input x variables
         @return: a sequential hidden layer object
         """
        return Sequential(
            [layers.InputLayer(input_shape=input_shape), layers.Dense(self._neurons), layers.Dense(self._neurons)])


class ConvNN(NeuralNetwork):
    """
    The ConvNN is the subclass of the NeuraLNetwork class. The abbreviation stands for convolutional neural network.
    The ConvNN class inherits from the NeuralNetwork class.
    """

    def __init__(self, neurons=50, input_shape=(32, 32, 3), filters=32, kernel_size=3, strides=(2, 2)):
        """
        In the constructor the ConvNN class inherits the superclass' constructor. Moreover, the hidden layer, cls and
        params instance variable get the class specific value.

        @params:
            neurons: the number of neurons for each layer in the hidden layers and the classifier
            input_shape: the shape of the input parameters
            filter: hyperparameter of the convolutional neural network
            kernel_size: hyperparameter of the convolutional neural network
            strides: hyperparameter of the convolutional neural network
        """
        super().__init__(neurons)
        hidden_layer = self._hidden_layer(input_shape=input_shape, filters=filters, kernel_size=kernel_size,
                                          strides=strides)
        self._set_hidden(hidden_layer)
        self._set_cls(self._classifier())
        self._set_params(self._cls.trainable_variables + self._hidden.trainable_variables)

    def __repr__(self):
        """
        This method returns some text with the name of the class.
        @returns: text with the class name
        """
        return "The neural network is a convolutional neural network."

    def _hidden_layer(self, input_shape, filters, kernel_size, strides):
        """
        This method overrides the abstract method in the superclass. Creates a fully connected neural network hidden
        layer.
         @params:
             input_shape: the shape of the input x variables
             filter: hyperparameter of the convolutional neural network
             kernel_size: hyperparameter of the convolutional neural network
             strides: hyperparameter of the convolutional neural network
         @return: a sequential hidden layer object
         """
        return Sequential([layers.InputLayer(input_shape=input_shape),
                           layers.Conv2D(filters=filters, kernel_size=kernel_size, strides=strides),
                           layers.Conv2D(filters=2 * filters, kernel_size=kernel_size, strides=strides),
                           layers.Conv2D(filters=self._neurons, kernel_size=kernel_size, strides=(5, 5)),
                           layers.Flatten()])
