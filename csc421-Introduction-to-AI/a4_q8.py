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
from matplotlib.patches import Circle, Rectangle, Polygon
from sklearn import datasets, metrics, svm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
import os
from PIL import Image
from skimage.feature import hog
import random

def main():
    #we first should define the shapes this is the example given by prarielearn
    red, blue, yellow, green = '#ff0000', '#0000ff', '#ffff00', '#00ff00'
    #our function will use one of these 4 per shape
    square = Rectangle((0.7, 0.1), 0.25, 0.25, facecolor=red)

    circle = Circle((0.8, 0.8), 0.15, facecolor=blue)
    triangle = Polygon(((0.05,0.1), (0.396,0.1), (0.223, 0.38)), fc=yellow)
    rhombus = Polygon(((0.5,0.2), (0.7,0.525), (0.5,0.85), (0.3,0.525)),  fc=green)
    shapes = [square, circle, triangle, rhombus]
    colors = [red, blue, yellow, green]
    img_size = 64

    #my computer literally cant run this so i have to do less im sorry
    #I would get rid of print statements too
    instances_of_color = 10
    #num_instances_shape = 6000
    #instances_of_color = 1000
    num_instances_shape = 60


    color_dic = {
        '#0000ff': 'Blue',
        '#00ff00': 'Green',
        '#ff0000': 'Red',
        '#ffff00': 'Yellow'
    }

    #visualizes the shapes
    def create_plot():
        print("example plot.")
        fig = plt.figure()
        ax = fig.add_subplot(111, facecolor='k', aspect='equal')
        for shape in (square, circle, triangle, rhombus):
            ax.add_artist(shape)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        plt.show()

    #creates a random sape using out visualization
    def create_random_shape():
        #set size to 64 x 64
        fig, ax = plt.subplots(figsize=(1,1), dpi = 64)
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.axis('off')

        shapes = ['square', 'circle', 'triangle', 'rhombus']
        red, blue, yellow, green = '#ff0000', '#0000ff', '#ffff00', '#00ff00'
        colors = [red, blue, yellow, green]
        shape = np.random.choice(shapes)
        color = np.random.choice(colors)
        size = np.random.uniform(.1, .3)
        x_pos = np.random.uniform(.1, .7)
        y_pos = np.random.uniform(.1, .7)

        #https://www.geeksforgeeks.org/how-to-draw-shapes-in-matplotlib-with-python/ this was a very
        #helpful article about shape plotting in matplotlib

        if shape == 'square':
            #shape = Rectangle((0.7, 0.1), 0.25, 0.25, facecolor=red)
            #rectangle at x pos, y pos with size nxn with random color
            shape_class = Rectangle((x_pos, y_pos), size, size, facecolor =color)
        elif shape == 'circle':
            #shape = Circle((0.8, 0.8), 0.15, facecolor=blue)
            shape_class = Circle((x_pos + size/2, y_pos + size/2), size / 2, facecolor = color)
            #this is the radius and center of circle
        elif shape == 'triangle':
            #1/2 base times height
            shape_class = Polygon([(x_pos,y_pos), (x_pos + size, y_pos), (x_pos + size/2, y_pos + size)], facecolor = color)
        elif shape == 'rhombus':
            shape_class = Polygon([(x_pos + size / 2, y_pos),(x_pos + size, y_pos + size / 2),(x_pos + size / 2, y_pos + size),(x_pos, y_pos + size / 2)], facecolor = color)

        ax.add_patch(shape_class)

         # Save as numpy array to prepare for processing and training
         #not doing so resulted in errors out the ying yang
        fig.canvas.draw()
        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        img = np.array(Image.fromarray(img).resize((64, 64)))
        
        plt.close(fig)
        return img, shape, color
    
    def generate_dataset(num_instances_shape, instances_of_color):
        print("generating dataset.")
        images = []
        shape_labels = []
        label_colors = []
        print("creating random shapes (this will take a while)")
        for _ in range(num_instances_shape):
            for x in range(instances_of_color):
                img, shape_label, color_label = create_random_shape()
                images.append(img)
                #we are getting the labels, so our classifier is more efficient in the end
                shape_labels.append(shape_label)
                label_colors.append(color_label)
        
        return images, shape_labels, label_colors

    #code here modified from the notebook
    def extract_hog_features(images):
        Xtrain_hog = []
        for i in range(len(images)):
            fd  = hog(images[i] , orientations=9 , pixels_per_cell = (8,8),
                    cells_per_block = (2,2) , visualize = False, channel_axis=-1)
            Xtrain_hog.append(fd)
            if ((i % 10000) == 0): 
                print(i)
        Xtrain_hog = np.array(Xtrain_hog)
        print("hog calculation complete")
        return Xtrain_hog

    class net(nn.Module):  #might need to adjust some of these hyper params
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

    
    #create_plot()
    #create_random_shape()

    create_plot() # this is our example plot

    img, shape_label, color_label = generate_dataset(num_instances_shape, instances_of_color)

    random_index = random.randint(0, len(img) - 1) #grab a random image

    random_image = img[random_index]

    print("here is a random image as requested from problem description")
    plt.imshow(random_image)
    plt.axis('off')
    plt.show()



    Xtrain_hog = extract_hog_features(img)


    #next we do svm and pca, where pca reduces dimensionality
    pca = PCA(0.8)
    Xtrain_pca = pca.fit_transform(Xtrain_hog)
    print("PCA completed")

    print(f"Xtrain_pca shape: {Xtrain_pca.shape}")
    print(f"Shape labels length: {len(shape_label)}")

    # Train our svm classifier
    shape_clf = svm.SVC(kernel='linear')
    shape_clf.fit(Xtrain_pca, shape_label)
    
    color_clf = svm.SVC(kernel='linear')
    color_clf.fit(Xtrain_pca, color_label)

    # evaluate our classifiers
    shape_preds = shape_clf.predict(Xtrain_pca)
    color_preds = color_clf.predict(Xtrain_pca)

    print("Shape Classification Report:")
    print(classification_report(shape_label, shape_preds))


    #making our labels not hex code
    color_label_names = [color_dic[color] for color in color_label]
    color_preds_names = [color_dic[color] for color in color_preds]

    print("Color Classification Report:")
    print(classification_report(color_label_names, color_preds_names))



if __name__ == "__main__":
    main()

