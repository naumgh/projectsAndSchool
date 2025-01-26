
# Modify this code as needed

import numpy as np
from scipy import stats


class Random_Variable:

    def __init__(self, name, values, probability_distribution):
        self.name = name
        self.values = values
        self.probability_distribution = probability_distribution
        if all(issubclass(type(item), np.integer) for item in values):
            self.type = 'numeric'
            self.rv = stats.rv_discrete(name = name, values = (values, probability_distribution))
        elif all(type(item) is str for item in values):
            self.type = 'symbolic'
            self.rv = stats.rv_discrete(name = name, values = (np.arange(len(values)), probability_distribution))
            self.symbolic_values = values
        else:
            self.type = 'undefined'

    def sample(self,size):
        if (self.type =='numeric'):
            return self.rv.rvs(size=size)
        elif (self.type == 'symbolic'):
            self.rv = stats.rv_discrete(name = name, values = (np.arange(len(values)), probability_distribution))
            self.symbolic_values = values
        else:
            self.type = 'undefined'

    def sample(self,size):
        if (self.type =='numeric'):
            return self.rv.rvs(size=size)
        elif (self.type == 'symbolic'):
            numeric_samples = self.rv.rvs(size=size)
            mapped_samples = [self.values[x] for x in numeric_samples]
            return mapped_samples

    def get_name(self):
        return self.name

values = np.array([1,2,3,4,5,6])
red = np.array([2,4,9])
blue = np.array([1,6,8])
green =np.array([3,5,7])

probabilities_A = np.array([1/6., 1/6., 1/6., 1/6., 1/6., 1/6.])
probabilities_B = np.array([0.0, 0.0, 0/6., 3/6., 3/6., 0/6.])
probabilities_C = np.array([2/6.,2/6.,2/6])
probabilities_D = np.array([2/6., 0/6.,0/6.,0/6.,0/6., 2/6., 0/6., 2/6., 0/6])
probabilities_E = np.array([0.0, 0/6., 2/6., 0/6., 2/6.,  0/6., 2/6., 0/6., 0/6])

dieA = Random_Variable('DieA', values, probabilities_A)
dieB = Random_Variable('DieB', values, probabilities_B)
red = Random_Variable('Red', red, probabilities_C)
blue = Random_Variable('Blue',blue, probabilities_C)
green = Random_Variable('Green',green,probabilities_C)


def dice_war(A,B, num_samples = 1000, output=True):
    # your code goes here and calculates appropriately prob
    prob = 0

    #take both numeric samples and seperate them
    a_sample = A.sample(num_samples)
    b_sample = B.sample(num_samples)

    #as per juperter code provided by prof, check to see if we get an
    #A win result. I prefer using zip to compare values in tuples
    a_win = 0
    for a,b in zip(a_sample, b_sample):
        if a > b:
            a_win += 1

    #final probability that "a" wins
    prob = a_win/num_samples

    print(prob)
    res = prob > 0.5

    #res is true if probability of a winning > 0.5
    if output:
        if res:
            print('{} beats {} with probability {}'.format(A.get_name(),
                                                           B.get_name(),
                                                           prob))
    #else we just print the opposite of "a" winning
        else:
            print('{} beats {} with probability {:.2f}'.format(B.get_name(),
                                                               A.get_name(),
                                                               1.0-prob))
    return (res, prob)



dice_war(dieA, dieB, 1000)

# Define red, green, and blue appropriately

# Uncomment the code below when the random variables for the red, green, and blue die
# have been defined

dice_war(red, green, 1000)
dice_war(green, blue, 1000)
dice_war(blue, red, 1000)





