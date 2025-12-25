"""
This implementation is a reconstructed reference version of the original
experiment, based on handwritten derivations and a recorded presentation.
The mathematical model and numerical behavior match the original work. 
The original notebook environment is no longer available; 
this is a reconstructed reference implementation based on the paper 
and recorded presentation Use the video presentation as reference
to confirm the validity of code.
"""
import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

#------------------------------------------------

# - variables
h_bar = 1             # reduced plank constant
b = 1                 # abstraction of product of reduced plank constant, gamma gyromagnetic ratio, and B(magentic field).
t_h = np.pi * h_bar/b  # The time required for the Hadamard to perform pi rotation when applied
t_z = np.pi * h_bar/b  # The time required for the Z-gate to perform pi rotation when applied
gamma = 0.1            # relaxation rate
#------------------------------------------------

 # Hamiltonians to realize quantum gates

H_12 = (-b/4) * np.array([[1,1,1,1],     # Modified Hadamard gate hamiltonian for two qubit system
                          [1,-1,1,-1],   # targets both qubits when applied
                          [1,1,-1,-1],
                          [1,-1,-1,1]])

H_z2 = (b/2) * np.array([[1,0,0,0],      # Modified Z gate hamiltonian for two qubit system     
                         [0,-1,0,0],     # targets second qubit when applied
                         [0,0,1,0],
                         [0,0,0,-1]
                         ])
#--------------------------------------------------

# initial rho density matrix that will be used in the experiment
rho_initial_00 = np.array([ [1,0,0,0],     # initial rho density matrix for state |00>
                           [0,0,0,0],
                           [0,0,0,0],
                           [0,0,0,0]

])

#---------------------------------------------------

# Lindblad operator
sigma_plus = np.array([[0,1],
                       [0,0]]) # Lowering operator as used by course convention.

I = np.array([[1,0],
              [0,1]]) # Identity matrix

L = np.kron(I,sigma_plus) # Tensor product to target second qubit

#-----------------------------------------------------

"""
Define oracle function 
as a function that performs
matrix operations to alter density matrix
 to |01> if balanced is true, otherwise
 dont alter the rho density matrix.
"""

def oracle(rho,balanced):

    unitary_time_op_z = expm(-1j * H_z2 * t_z * (1/h_bar)) # unitary time operator for z gate

    if balanced:
        print("Balanced")
        flipped_rho = unitary_time_op_z @ rho @ unitary_time_op_z.conj().T # apply Z gate to flip second qubit-choice is arbitrary
        return flipped_rho
    else:
        print("Constant")
        return rho  # return unchanged rho if balanced is false
    
# Implementation of Deutsch Jozsa algorithm
def deutsch_jozsa_algorithm(rho,balanced):
    total_time_evolution = 1 # total time evolution for the injection of noise in seconds-arbitrary choice
    delta_t = 1 # time increment

    unitary_time_op = expm(-1j * H_12 * t_h * (1/h_bar)) # unitary time operator for Hadamard gate
    h_rho = unitary_time_op @ rho @ unitary_time_op.conj().T # apply hadamard gate

    oracle_rho = oracle(h_rho,balanced) # execute oracle and return evaluated rho

    final_rho = unitary_time_op @ oracle_rho @ unitary_time_op.conj().T # apply final Hadamart gate
    

    # calculate T1 noise using Lindblad equation
    t1_noise = gamma * ((L @ final_rho @ L.conj().T) - (0.5 * L.conj().T @ L @ final_rho + 0.5 * final_rho @ L.conj().T @ L ))

    # apply T1 noise
    for current_second in range(total_time_evolution):

        #update rho
        final_rho += t1_noise * delta_t

        # normalize rho via normalization constant
        final_rho /= np.trace(final_rho)

        delta_t += current_second

    return final_rho


# Here is the matrix implementation of Deutsch Jozsa
balanced = False
# balanced = True

# apply DJ algo with rho initial |00>
rho_after_applied_algo = deutsch_jozsa_algorithm(rho_initial_00,balanced)

"""
 Use probabilities to plot- This is essentially a trace
 of the final rho density matrix after returned
 from the Deutsch Jozsa algorithm function matrix version
"""

trace = np.real(np.diag(rho_after_applied_algo))

# this will be used in the plot labels
basis_states = ['00','01','10','11']
plt.bar(basis_states,trace)
plt.xlabel('Basis states')
plt.ylabel('Probability')
plt.title('Final Algorithm State')
plt.show()


