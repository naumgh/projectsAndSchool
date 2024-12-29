import torch
import torchvision
import torchvision.transforms as transforms
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset



def main():

    #from csc421 notebook
    transform = transforms.Compose(
        [transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    batch_size = 32


    # CIFAR Canadian Institute for Advanced Research
    # 2009 Tiny images object classificatino - AlexNet 
    # Reported training times from 2014 - 20 minutes 


    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                            shuffle=True, num_workers=4)

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                        download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                            shuffle=False, num_workers=4)

    classes = ('plane', 'car', 'bird', 'cat',
            'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    print('Training set')
    print(f'Samples: {trainset.data.shape}')
    print(f'Labels: {len(trainset.targets)}')

    print('\nTest set')
    print(f'Samples: {testset.data.shape}')
    print(f'Labels: {len(testset.targets)}')

    print('\nClasses\n')
    print(tabulate(
        list(trainset.class_to_idx.items()), headers=['Name', 'Index'], 
        tablefmt='orgtbl'
    ))

    def imshow(img, noise):
        if noise == True:
            img = img + torch.randn(img.shape)
        img = img / 2 + 0.5     # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()

    def test_accuracy(net, testloader, device):
        correct = 0

        # since we're not training, we don't need to calculate the gradients for our outputs
        with torch.no_grad():
            net.eval()
            for images, labels in testloader:
                images, labels = images.to(device), labels.to(device)
                #  = images + 0.2 * torch.randn(images.shape).to(device)
                
                # calculate outputs by running images through the network
                outputs = net(images)

                # the class with the highest energy is what we choose as prediction
                predicted = torch.max(outputs.data, 1)[1]

                correct += (predicted == labels).sum().item()
        
        return correct / len(testloader.dataset)


    # get some random training images
    dataiter = iter(trainloader)
    images, labels = next(dataiter)

    # show images
    imshow(torchvision.utils.make_grid(images), False)
    # print labels
    print(' '.join('%5s' % classes[labels[j]] for j in range(batch_size)))


    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(3,32,5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(32, 32, 5)
            self.fc1 = nn.Linear(32 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = torch.flatten(x, 1) # flatten all dimensions except batch
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x


    torch.cuda.is_available()
   # torch.cuda.get_device_name(0)
   # print(torch.cuda.get_device_name(0))

    if torch.cuda.is_available(): 
        #dev = "cuda:0"
        dev = "cuda:0"
    else: 
        dev = "cpu" 

    #maybe fix this later
    # I dont have a gpu (i do but it's integrated), so i need to replace this to cpu if you have gpu for testing
    #just run it with cuda:0
    dev = "cpu"
    device = torch.device(dev) 
    #dev = "cuda" 
    print("device in use: ", device)

    net = Net()
    net.to(device)
    print(net)

    summary(net, (3,32,32), batch_size=32, device=dev)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    #%%time this is used for outputting jupyter notebook time
    for epoch in range(20):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data
            inputs, labels = inputs.to(device,non_blocking=True), labels.to(device, non_blocking=True)
            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            
            if i % 400 == 399:    # print every 400 mini-batches
                print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')

    dataiter = iter(testloader)
    images, labels = next(dataiter)


    #added to the test set
    added_noise = images + torch.randn(images.shape) * .2
    #added_noise = 

    #here is the origional images
    print("origional images")
    imshow(torchvision.utils.make_grid(images), False)
    print('GroundTruth: ', ' '.join('%5s' % classes[labels[j]] for j in range(8)))
    clean_accuracy = test_accuracy(net, testloader, device)
    print("the clean accuracy: ", clean_accuracy)
    #images, labels = next(dataiter)

    # here is the noisy images from added_noise var
    print("noisy images from test-set NOT training set")
    imshow(torchvision.utils.make_grid(added_noise), False)
    print('GroundTruth: ', ' '.join('%5s' % classes[labels[j]] for j in range(8)))


    #creates an identitcal copy of the dataset (test set) we had origionally, but just with the added noise
    #for some reason, both were getting the same accuracy at first
    noisy_dataset = TensorDataset(added_noise, labels)
    noisy_loader = DataLoader(noisy_dataset, batch_size=batch_size, shuffle=False)

    noisy_accuracy_added_noise = test_accuracy(net, noisy_loader, device)
    print("Accuracy on noisy images (from added_noise variable): ", noisy_accuracy_added_noise)

    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)

    print(device)
    net = Net()
    net.load_state_dict(torch.load(PATH))
    net.to(device)
    images = images.to(device)
    outputs = net(images)
    _, predicted = torch.max(outputs, 1)

    # print(outputs)
    print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                                for j in range(8)))


if __name__ == "__main__":
    main()