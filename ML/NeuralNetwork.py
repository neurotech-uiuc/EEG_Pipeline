import torch
import torch.nn as nn

class TwoLayerNet(torch.nn.Module):

    def __init__(self, inputDim, outputDim, lrate):
        """
        In the constructor we instantiate two nn.Linear modules and assign them as
        member variables.
        """
        super(TwoLayerNet, self).__init__()

        # https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw#:~:text=The%20number%20of%20hidden%20neurons,size%20of%20the%20input%20layer.
        # The number of hidden neurons should be 2/3 the size of the input layer, plus the size of the output layer.
        numHiddenLayers = 2/3 * inputDim + outputDim

        self.model = nn.Sequential(
                    nn.Linear(inputDim, numHiddenLayers), # input
                    nn.ReLU(), # activation function
                    nn.Linear(numHiddenLayers, outputDim) # output
                    )

        # loss function, use Binary Cross Entropy because ouput class size is only 2?
        self.loss_fn = torch.nn.BCELoss()

        self.optimizer = optim.SGD(self.model.parameters(), lr=lrate)


    def forward(self, x):
        """ A forward pass of your autoencoder
        @param x: an (N, in_size) torch tensor
        @return y: an (N, out_size) torch tensor of output from the network
        """

        output = self.model(x)
        return output

    def step(self, x,y):
        """
        Performs one gradient step through a batch of data x with labels y
        @param x: an (N, in_size) torch tensor
        @param y: an (N,) torch tensor
        @return loss: total empirical risk (mean of losses) at this time step as a float
        """
        
        # Zero gradients, perform a backward pass, and update the weights.
        self.optimizer.zero_grad()

        y_pred = forward(x)
        loss = self.loss_fn(y_pred, y)
        loss.backward()

        optimizer.step()

        return loss
