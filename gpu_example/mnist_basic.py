# Using PlaidML as the backend instead of the TensorFlow back end.
# Install the plaidml backend before you import keras
import plaidml.keras
plaidml.keras.install_backend()

from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()