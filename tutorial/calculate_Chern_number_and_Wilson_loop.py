import guan
import numpy as np
from math import *

# calculate Chern number
def hamiltonian_function(kx, ky):  # one QAH model with chern number 2
    t1 = 1.0
    t2 = 1.0
    t3 = 0.5
    m = -1.0
    hamiltonian = np.zeros((2, 2), dtype=complex)
    hamiltonian[0, 1] = 2*t1*cos(kx)-1j*2*t1*cos(ky)
    hamiltonian[1, 0] = 2*t1*cos(kx)+1j*2*t1*cos(ky)
    hamiltonian[0, 0] = m+2*t3*sin(kx)+2*t3*sin(ky)+2*t2*cos(kx+ky)
    hamiltonian[1, 1] = -(m+2*t3*sin(kx)+2*t3*sin(ky)+2*t2*cos(kx+ky))
    return hamiltonian
chern_number = guan.calculate_chern_number_for_square_lattice(hamiltonian_function, precision=100)
print('Chern number=', chern_number)

# calculate Wilson loop
wilson_loop_array = guan.calculate_wilson_loop(guan.hamiltonian_of_ssh_model)
print('Wilson loop =', wilson_loop_array)
p = np.log(wilson_loop_array)/2/pi/1j
print('p =', p, '\n')