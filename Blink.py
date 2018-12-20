import numpy as np
import math
    
def rank(links):
    
    ##Set Dimension of Graph
    n = len(links)
    
    ##Construct Initial State Vector
    x = []
    for evect in range (0, n):
        x.append(1)
    x = np.array(x)
    print("Initial State Vector:")
    print(x)
    
    ##Initialize Probability Matrix
    P = []
    for initcol in range(0, n):
        row = []
        for initrow in range(0, n):
            row.append(0)
        P.append(row)
    
    ##Generate Probability Matrix
    for i in range(0, n):
        for j in range(0, n): #iterate through each element P_ij in the matrix
            found = False #search if node i is connected to node j
            for index in range (0, len(links[i])): 
                if (links[i][index] == j):
                    found = True; 
                    break;
            if (found == True): #if node i and node j are connected
                P[i][j] = 1/len(links[i]) #set probability to 1/total number of nodes that i has
            elif (len(links[i]) == 0): #if node i is a dangling node
                P[i][j] = 1/n             
            else: #node i and j are not connected
                P[i][j] = 0
    
    P = np.matrix(P).transpose()
    print("\nFilled Probability Matrix P:")
    print(P)
    
    ##Solve Eigenvalues/Eigenvectors
    estuff = np.linalg.eig(P)
    print("\nEigenvalues of Probability Matrix P")
    print(estuff[0])
    print("\nEigenvectors of Probability Matrix P")
    print(np.matrix(estuff[1]))
    
    ##Construct Matrix S with Eigenvector Col
    S = np.matrix(estuff[1])
    print("\nFilled Matrix S:")
    print(S)
    
    try:
        Sinverse = np.linalg.inv(S)
        print("\nFilled Matrix S^-1 :")
        print(Sinverse)    
    except np.linalg.LinAlgError:
        passthe
      
    ##Construct Matrix SD^k with V1 as First Col
    SDk = np.matrix(np.zeros((n,n), dtype = complex))
    SDk[:,0] = S[:,0]
    print("\nInitialized Matrix SD^k:")
    print(SDk)
    
    ##Calculate Matrix SD^kS^-1
    print("\nCalculated SD^kS^-1")
    print(np.matmul(SDk, Sinverse))
    SDSinverse = np.matmul(SDk, Sinverse)
    
    ##Calculate Pagerank Vector SD^kS^-1x
    pagerank = np.matmul(SDSinverse, x)
    pg = np.squeeze(np.asarray(pagerank))
    print("\nPagerank Vector:")
    print(pg)
    
    ##Sort Pagerank
    enumerate(pg)
    #print(list(enumerate(pg)))
    #print([(node,value) for (value,node) in enumerate(pg)])
    sorted([(node,value) for (value,node) in enumerate(pg)])
    print("\nSorted Pages by Rank High to Low")
    enumRank = sorted([(node,value) for (value,node) in enumerate(pg)], reverse=True)
    print(enumRank)
    
    ##Return Ranks
    ranks = []
    for r in range(0, len(enumRank)):
        ranks.append(enumRank[r][1])
    print("\nFinal Rank of Pages High to Low")
    print(ranks)
    return ranks
    
##Test Cases    
#rank([[1,2,3],[3],[0,3],[0,2]])
rank([[1,2,3],[3],[0,3],[]])

#test 1!
inpt = [[1, 5], [2, 5], [1, 3, 5], [4], [1, 5], [2, 6], [0, 1]]
rank(inpt)

#test 2!
inpt2 = [[1,3,4],[0,2,4],[3,6],[2,4,6],[5,8],[4,6,8],[0,7,9],[0,6,8],[2,9],[0,2,8]]
rank(inpt2)

#rank([[1,2,3],[2,3],[0],[0,2]])


