import numpy as np

#This Function defines an inner product
def inner_product(u,v):
    return np.dot(u,v)
    
#This function defines projection of v onto u
def proj(u,v): 
    return (inner_product(v,u) / inner_product(u,u))*u

def gs_process(vectors):
    n = len(vectors)     # number of vectors in a list
    vectors = np.array(vectors) # convert vectors into a numpy array
    m = max(vectors.shape)  # number of entries in each vector
    u = np.zeros((n,m))     # creates an array of shape n by m
    
    u[0] = vectors[0]

    for i in range(1,n):
        sum_vector = np.zeros(m)
        for j in range(0,i):
            sum_vector = sum_vector + proj(u[j],vectors[i])
        u[i] = vectors[i] - sum_vector
    return u

vectors = [[1,-1,1,-1],[1,1,3,-1],[-3,7,1,3]]
print(gs_process(vectors))
