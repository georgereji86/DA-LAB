import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
       
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)

    def feedforward(self, X):
        
        self.hidden_layer_activation = np.dot(X, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_activation)

        self.output_layer_activation = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.output = sigmoid(self.output_layer_activation)
        return self.output

    def backpropagate(self, X, y, learning_rate):
       
        output_loss = self.output - y
        output_gradient = output_loss * sigmoid_derivative(self.output)

        
        hidden_loss = output_gradient.dot(self.weights_hidden_output.T)
        hidden_gradient = hidden_loss * sigmoid_derivative(self.hidden_layer_output)

        
        self.weights_hidden_output -= self.hidden_layer_output.T.dot(output_gradient) * learning_rate
        self.weights_input_hidden -= X.T.dot(hidden_gradient) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            self.feedforward(X)
            self.backpropagate(X, y, learning_rate)
            if epoch % 1000 == 0:  
                loss = mse_loss(y, self.output)
                print(f"Epoch {epoch}, Loss: {loss}")


if __name__ == "__main__":
    
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])  

   
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    
    nn.train(X, y, epochs=10000, learning_rate=0.1)

