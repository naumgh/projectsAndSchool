import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn import datasets, svm
from sklearn import tree
from sklearn.naive_bayes import CategoricalNB
from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB


# URL of the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"

# Column names as per the dataset description
columns = [
    "class", "cap-shape", "cap-surface", "cap-color", "bruises", "odor",
    "gill-attachment", "gill-spacing", "gill-size", "gill-color", "stalk-shape",
    "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring",
    "stalk-color-above-ring", "stalk-color-below-ring", "veil-type", "veil-color",
    "ring-number", "ring-type", "spore-print-color", "population", "habitat"
]

# Load the dataset directly into memory
#data = pd.read_csv(url, header=None, names=columns)
#data = pd.read_csv(url, header=None, names=columns)
#data.to_csv('mushroom.csv', index=False)
data = pd.read_csv('mushroom.csv')

print("please select from one of the columns avaliable:", data.columns.tolist())
selected_column = input("enter the column u want for classification: ")


#this should work for every dataset as long as the 'class' column exists
# Separate features (X) and target (y)
X = data.drop("class", axis=1)  # Features
y = data["class"]              # Target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Cap-shape Naive Bayes Categorical from scratch 
#X_train = pd.concat([X_train, y_train], axis='columns')

# put features (X) and target (y) back together 
#X_train_cap = X_train[['cap-shape', 'class']]
#classes = X_train_cap["class"].unique().tolist()  # Get unique class labels
#cap_shapes = X_train_cap["cap-shape"].unique().tolist() # Get unique attribute values 

#print('Classes', classes)
#print('Cap Shapes', cap_shapes)

#priors = {}
#likelihoods = {}

# value_counts calculates how many instances of each value are present in the data
# with the normalize flag it can convert these value counts to probabilities 
#priors = X_train_cap["class"].value_counts(normalize=True).to_dict()

# calculate the marginal probabilities for each cap-shape 
#marginals = X_train_cap["cap-shape"].value_counts(normalize=True).to_dict()

# calculate the likelihoods for each class (edible and poisonous)
# Each likihood should be a dictionary with keys being the cap_shape and
# values being the corresponding probabilities
# Important note: some cap_shapes might not have an instance in a particular class
# in which case they will not be taken into account by value_counts. You will need
# to set those to 0. 
'''
for c in classes:
    class_data = X_train_cap[X_train_cap["class"] == c]
    #likelihoods = X_train_cap["class"].value_counts(normalize=True).to_dict()
    all_cap_counts = class_data["cap-shape"].value_counts().to_dict()
    print(all_cap_counts)
    # YOUR CODE GOES HERE 
    likelihoods[c] = {}
    for cap_shape in cap_shapes:
        if cap_shape in all_cap_counts:
            likelihoods[c][cap_shape] = all_cap_counts[cap_shape] / len(class_data)
        else:
            likelihoods[c][cap_shape] = 0


print("Likelihoods ",likelihoods)
print("Priors", priors)
print("Marginals", marginals)
'''
class categoricalNaiveBayes: #init train predict
    def __init__(self):
        self.feature = None #let the user select what feature they want calculated
        self.features = [] # will store all feature names
        self.likelihoods = {} #will store conditional probabilities shape given class
        self.priors = {} #how often mushroom is edible vs poisonous
        self.marginals = {}

    def train(self, X, y, f_column):
        #classes = y_train.unique()
        #cap_shapes = X['cap-shape'].unique()

        self.feature = f_column
        data = pd.concat([X,y], axis=1) # rips column out

        classes = y.unique()
        cap_shapes = X[f_column].unique()

        self.priors = y.value_counts(normalize=True).to_dict()

        self.likelihoods = {}

        for c in classes:
            class_data = X[y == c]
            #likelihoods = X_train_cap["class"].value_counts(normalize=True).to_dict()
            all_cap_counts = class_data[f_column].value_counts().to_dict()
            print(all_cap_counts)
            # YOUR CODE GOES HERE 
            self.likelihoods[c] = {}
            for cap_shape in cap_shapes: # this isnt actually cap shape anymore, rather it can be any class
                if cap_shape in all_cap_counts:
                    self.likelihoods[c][cap_shape] = all_cap_counts[cap_shape] / len(class_data)
                else:
                    self.likelihoods[c][cap_shape] = 0

        feature_counts = X[f_column].value_counts(normalize=True).to_dict()
        self.marginals = feature_counts  
        
    
    def predict(self, X_test_cap):
        predictions = []
        for _, row in X_test_cap.iterrows():
            cap_shape = row[self.feature]

            posteriors = {}
            for c in self.priors:
                likelihood = self.likelihoods[c].get(cap_shape, 0)
                #this syntax is apparantly the same as the syntax
                #for marginal used below, but im lazy to change marginal
                prior = self.priors[c]
                marginal = self.marginals.get(cap_shape, 0)
                #incorrect values pop up if you dont check
                if marginal > 0:
                    posteriors[c] = (likelihood * prior) / marginal
                else:
                    posteriors[c] = 0.0

            predicted_class = max(posteriors, key=posteriors.get)
            predictions.append(predicted_class)

        return predictions


# calculate the posterior probabilities for each class based on cap_shape
# using Bayes Rule
# the posteriors should be a dictionary indexed by cap_shape with values
# being dictionaries indexed by class with the corresponding probabilities

#bayes rule:

#P(CLASS|CAP-SHAPE) = (P(CAP-SHAPE | CLASS) . P(CLASS))/P(CAP-SHAPE)
'''
posteriors = {}
prior = 0
for a in cap_shapes:     
    posteriors[a] = {} 
    for c in classes:
        # YOUR CODE GOES BELOW AND REPLACE THE 0.0 
        likelihood = likelihoods[c][a] # shape given class
        marginal = marginals[a] # class
        prior = priors[c] # shape

        if marginal > 0:
            posteriors[a][c] = (likelihood * prior) / marginal
        else:
            posteriors[a][c] = 0.0 

print("Posteriors", posteriors)


# cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s


prior_edible = np.round(priors['e'],2)
posterior_edible_if_bell = (np.round(posteriors['b']['e'],2))
posterior_edible_if_flat = (np.round(posteriors['x']['e'],2))

print('Prior probability the mushroom is edible : ', prior_edible)
print('Posterior probability the mushroom is edible if it has a flat cap_shape :', posterior_edible_if_flat)
print('Posterior probability the mushroom is edible if it has a bell cap_shape :', posterior_edible_if_bell)

# Load the dataset
data = pd.read_csv('mushroom.csv')

# Split the dataset into features (X) and target (y)
X = data.drop(columns=['class'])
y = data['class']
'''
# Initialize and train the Categorical Naive Bayes classifier
model = categoricalNaiveBayes()
model.train(X_train, y_train, selected_column)
predictions = model.predict(X_test)

# Print classification report
print(classification_report(y_test, predictions, target_names=y.unique()))