# “Blink”: A Backlinks-Based Page Rank Algorith

#### Carnegie Mellon 21-241 Matrix Algebra Final Project by Kayla Leung and Amy Lu

Our program was coded in Python Version 3.4.6. The NumPy 1.15.4 scientific computing package was used for a
number of mathematical calculations, specifically for the use of finding the eigenvalues and eigenvectors of a matrix
as well as finding the inverse and transpose of a matrix.
The algorithm for our program, Blink, is based on the premise that the importance of any webpage can be determined
by the number of other external pages that link to it (i.e. the most amount of backlinks).

### Terminology

* Markov chains: A sequence of random variables that that follow the Markov property, i.e. a linked chain of
events in which what happens next depends only on the current system state.
* Perron-Frobenius Theorem: A real positive square matrix with positive entries has a unique maximal eigenvalue of multiplicity 1 and a corresponding eigenvector with positive entries.
2/6
* Column-stochastic matrix: A matrix is column-stochastic if all of its entries are nonnegative and the entries in
each column sum to one.
* Transition matrix: Define a_ij to be the probability of the system being in state i after it was in state j ( at any
observation ). The matrix A = (a_ij) is called the Transition matrix
* Dangling node: A node, representing a webpage in a graph, is a dangling node if it does not contain any
outgoing link.
* Independent Eigenvector Theorem: If A is an N x N complex matrix with N distinct eigenvalues, then any set
of N corresponding eigenvectors form a basis for C_N.
