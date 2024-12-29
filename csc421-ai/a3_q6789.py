from hmmlearn import hmm
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 

rng = np.random.default_rng(1)

class Random_Variable: 
    
    def __init__(self, name, values, probability_distribution): 
        self.name = name 
        self.values = values 
        self.probability_distribution = probability_distribution        
        if all(issubclass(type(item), np.integer) for item in values): 
            self.type = 'numeric'
            self.rv = stats.rv_discrete(name = name, values = (values, probability_distribution), seed=rng)
        elif all(type(item) is str for item in values): 
            self.type = 'symbolic'
            self.rv = stats.rv_discrete(name = name, values = (np.arange(len(values)), probability_distribution), seed=rng)
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
        
    def probs(self): 
        return self.probability_distribution
    
    def vals(self): 
        print(self.type)
        return self.values 

def plot_samples(samples, state2colour, title):
    colours = [state2colour[x] for x in samples]
    x = np.arange(0, len(colours))
    y = np.ones(len(colours))
    plt.figure(figsize=(10,1))
    plt.bar(x, y, color=colours, width=1)
    plt.title(title)


def markov_chain(transmat, state, state_names, samples): 
    (rows, cols) = transmat.shape 
    rvs = [] 
    values = list(np.arange(0,rows))
    
    # create random variables for each row of transition matrix 
    for r in range(rows): 
        rv = Random_Variable("row" + str(r), values, transmat[r])
        rvs.append(rv)
    
    # start from initial state and then sample the appropriate 
    # random variable based on the state following the transitions 
    states = [] 
    for n in range(samples): 
        state = rvs[state].sample(1)[0]    
        states.append(state_names[state])
    return states


# QUESTION 6 
# appropriately define the transition matrix and
# create sample a markov chain with states 'CGD' and 'CGS'
# Xmarkov should consits of 1000 samples of the markov chain

# YOUR CODE GOES HERE 

transmat1 = np.array([[0.7, 0.3], 
                    [0.2, 0.8]])

values = ['CGD', 'CGS']
Zmarkov = markov_chain(transmat1, state=0, state_names=values, samples = 1000)

print('Zmarkov[0:10]:', Zmarkov[0:10])
# output should be Zmarkov[0:10]: ['CGD', 'CGS', 'CGD', 'CGS', 'CGS', 'CGS', 'CGS', 'CGS', 'CGS', 'CGD']

# approprixately define random variables 'CGD_colors' and 'CGS_colors'
# for mapping the states to colors with the specified emission probabilities

'''
sunny_colors = Random_Variable('sunny_colors', ['y', 'r', 'b', 'g'], 
                              [0.6, 0.3, 0.1, 0.0])
cloudy_colors = Random_Variable('cloudy_colors', ['y', 'r', 'b', 'g'], 
                               [0.0, 0.1, 0.4, 0.5])
'''
'''
The observation probabilities of CGD regions are: r: 0.1, g:0.1, y: 0.4, and b:0.4. 

The observation probabilities of CGS regions are: r: 0.4, g: 0.4, y: 0.1, b: 0.1
'''

cgd_colors = Random_Variable('CGD', ['r', 'g', 'b', 'y'], [0.1, 0.1, 0.4, 0.4] )
cgs_colors = Random_Variable('CGS', ['r', 'g', 'b', 'y'], [0.4, 0.4, 0.1, 0.1] )

def emit_obs(state, sunny_colors, cloudy_colors): 
    if (state == 'CGD'):   
        obs = cgd_colors.sample(1)[0]
    else: 
        obs = cgs_colors.sample(1)[0]
    return obs 

# iterate over the sequence of states Zmarkovand emit color based on the emission probabilities 
Xmarkov = [emit_obs(s, cgd_colors, cgs_colors) for s in Zmarkov]
print('Xmarkov[0:10]:',Xmarkov[0:10])
# output should be Xmarkov[0:10]: ['b', 'y', 'y', 'g', 'g', 'g', 'g', 'r', 'g', 'b']


np.random.seed(0)



emissionprob_ = np.array([[0.1, 0.1, 0.4, 0.4], 
                           [0.4, 0.4, 0.1, 0.1]])

# QUESTION 7
# Use the hmm.CategoricalHMM to create a model for our problem
# and use it to generate samples

model = hmm.CategoricalHMM(n_components=2)

# Your code goes here 

start_prob = np.array([0.5, 0.5])

model.startprob_ = start_prob
model.transmat_ = transmat1
model.emissionprob_ = emissionprob_

print(model.emissionprob_)
                        

# Code for plotting
'''
X, Z = model.sample(100)
samples = [item for sublist in X for item in sublist]
states2colour = {0: 'red', 1: 'green', 2: 'blue', 3: 'yellow'}
plot_samples(samples[0:100], states2colour, 'Observations (ACTG)')
obj2colour = {0: 'black', 1: 'white'}
plot_samples(Z[0:100], obj2colour, 'States (CGD and CGS)')
plt.show()
'''
X, Z = model.sample(n_samples=10000)
#print(X)




# QUESTION 8 
# Every time that you can the fit function of the CategoricalHMM
# you get a different estimation of the HMM parameters. 
# learn a good model by trying 100 fits and selecting the best one
# based on score. Store the "best" model in estimated_model 

print("X shape:", X.shape)
print("X values:", np.unique(X))

# learn a new model
#print("Unsupervised Estimated Emission Matrix (Before Rounding):")
#print(estimated_model.emissionprob_)
#best_score = estimated_model.score(X)

#X = np.array(samples).reshape(-1, 1)

best_model=None
best_score = model.score(X)

for i in range(100):
    estimated_model = hmm.CategoricalHMM(n_components=2).fit(X)
    score = estimated_model.score(X)
    print(score)
    if score > best_score:
        best_score = score
        best_model = estimated_model

estimated_model = best_model
print(estimated_model.transmat_)

# Uncomment the code below when things are working

original_transmat = np.copy(model.transmat_)
original_emission_probs = np.copy(model.emissionprob_)

print("Original Transition Matrix:")
print(original_transmat)
print("Original Emission Matrix:")
print(original_emission_probs)

unsupervised_transmat = np.round(estimated_model.transmat_, 2)
unsupervised_emission_probs = np.round(estimated_model.emissionprob_,2)
print("Unsupervised Estimated Transition Matrix:")
print(unsupervised_transmat)
print("Unsupervised Estimated Emission Matrix:")
print(unsupervised_emission_probs)


# QUESTION 9

# Write a function train_hmm_supervised that takes
# as input both the state sequence Z and the associated
# observations X. Estimate the transition matrix
# from the data essentially by counting and normalizing transitions
# and then the emmision probabilities by appropriately counting
# observations for each state. 

from collections import defaultdict

def train_hmm_supervised(Z, X, num_states, num_observations):
    supervised_transmat = np.zeros((num_states, num_states))
    emmision_counts = np.zeros((num_states, num_observations))
    supervised_transmat_sum = np.zeros((num_states, 1))
    emission_counts_sum = np.zeros((num_states, 1))


    print(num_states)
    print(num_observations)

    for i in range(0, len(Z)-1):
        supervised_transmat[Z[i], Z[i+1]] += 1

    for i in range(0,len(Z)):
        emmision_counts[Z[i], X[i]] += 1

    for x in range(0, len(supervised_transmat)):
        for y in range(0, len(supervised_transmat[x])):
            #print(supervised_transmat[x][y])
            supervised_transmat_sum[x] += supervised_transmat[x][y]

    for x in range(0, len(emmision_counts)):
        for y in range(0, len(emmision_counts[x])):
            #print(supervised_transmat[x][y])
            emission_counts_sum[x] += emmision_counts[x][y]



    for x in range(0, len(supervised_transmat)):
        for y in range(0, len(supervised_transmat[x])):
            #print(supervised_transmat[x][y])
            #supervised_transmat_sum[x] += supervised_transmat[x][y]
            supervised_transmat[x][y] = supervised_transmat[x][y]/supervised_transmat_sum[x]


    for x in range(0, len(emmision_counts)):
        for y in range(0, len(emmision_counts[x])):
            #print(supervised_transmat[x][y])
            emmision_counts[x][y] = emmision_counts[x][y]/emission_counts_sum[x]

   # print(supervised_transmat_sum)
    #print(emission_counts_sum)

    #print(supervised_transmat[0][0])
    #print(emmision_counts)

   # for i in range(0, len(Z)-1):
    #    supervised_transmat[Z[i], Z[i+1]] = supervised_transmat[Z[i], Z[i+1]] / len(Z)

    #for i in range(0, len(Z)):
    #    emmision_counts[Z[i], X[i]] = emmision_counts[Z[i], X[i]] / len(Z)


   # print(supervised_transmat)
   # print(emmision_counts)

    return(supervised_transmat, emmision_counts)
   # pass




num_states = 2
num_observations = 4

# Uncomment the code below once things are working

supervised_transmat, supervised_emission_probs = train_hmm_supervised(Z, X, num_states, num_observations)
supervised_transmat = np.round(supervised_transmat,2)
supervised_emission_probs = np.round(supervised_emission_probs, 2)

print("Supervised Transition Probabilities:\n", supervised_transmat)
print("Supervised Emission Probabilities:\n", supervised_emission_probs)

