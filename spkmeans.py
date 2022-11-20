from cmath import inf
import pandas as pd
import numpy as np
import random
import sys
import math
import subprocess
import myspkmeanssp as mkm




############################################

## THIS IS THE KMEANS++ FUNCTION FROM HW2 ##
 
############################################

def kmeans_pp (vectors, k): 
    np.random.seed(0)
    number_of_rows = vectors.shape[0]
    random_index = np.random.choice(number_of_rows)
    index_list = [random_index]
    first_centroid = vectors[random_index]
    initial_centroids = [first_centroid.tolist()]
    probs = [float("inf") for i in range(number_of_rows)]

    while len(initial_centroids) < k :
        for i in range (number_of_rows):
            cur_row = vectors[i]
            for c in initial_centroids:
                vectors_dist = np.linalg.norm(cur_row - c)**2
                if vectors_dist < probs[i]:
                    probs[i] = vectors_dist
        probs_sum = sum(probs)
        probs = [x/probs_sum for x in probs]
        new_index = np.random.choice(number_of_rows, p = probs)

        index_list.append(new_index)
        initial_centroids.append(vectors[new_index].tolist())
        probs = [float("inf") for i in range(number_of_rows)]

    print(*index_list, sep= ',')
    return initial_centroids


###################################

## CALCULATING VECTORS DISTANCE ##
 
###################################


def vectors_delta (vector1, vector2):
    length = len(vector1)
    delta = 0.0
    for i in range (length):
        delta += ((vector1[i]-vector2[i])**2)
    return delta


#####################################################################################

## PYTHONS MAIN PYTHON. CALLING TO FIT1, FIT2- C FUNCTIONS, AND PRINTING CENTROIDS ##
 
#####################################################################################

if __name__ == "__main__": 
    max_iter = 300
    args = sys.argv
    if len(args) != 4:
        print("Invalid Input_8!")
        exit()    
    try:
        k = int(args[1])
    except ValueError:
        print("Invalid Input_9!")
        exit()
    if k < 0:
        print("Invalid Input_10")
        exit() 
    goal = args[2]
    file_input = args[3]
    eps = 0

    new_vectors = mkm.fit1(goal, file_input,  int(k))
    
    
    if goal != "spk":
        exit(0)
   
    k = new_vectors.pop()
    n = len(new_vectors)

    new_vectors = np.array(new_vectors)

    initial_centroids = kmeans_pp(new_vectors, k)

    ans = mkm.fit2(float(eps), int(k), int(max_iter), int(k), int(n) ,int(n*k), new_vectors, initial_centroids)
    for centro in ans:
        print (*centro , sep = ",")
    
