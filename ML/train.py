import NeuralNetwork

def train(train_set,train_labels, dev_set, dev_labels):
   
    # n_iter = 100
    # batch_size = 100
    lrate,loss_fn,in_size,out_size
    inputDim, outputDim, lrate
    net = NeuralNet(400, 2, 1e-4)

    for observation, label in zip(train_set, train_labels):
        net.step(observation, label)
    

