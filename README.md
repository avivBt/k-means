# k-means
 C and Python interface implement a version of the normalized spectral clustering k-means algorithm.

Read datapoints from file in Python file and send to Cmodule
Run Jacobi algorithm in C and return k vectors to Python
Choose k rows as initial centroids with k++ algorithm and send indices to C
Find k final centroids by kmeans algorithm in C
Return to python and print
*C file can run indpendently *It is also possible to run the spk algorithm to a certain step of your choice (Weight adjacency matrix, Diagonal, Lnorm, Jacobi, and Complete spk)
