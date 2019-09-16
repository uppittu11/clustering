import numpy as np

def collect_molecules():
    molecule = {
        'ucer2':(6, [np.arange(8), np.arange(10, 15)]),
        'ecer2':(6, [np.arange(5), np.arange(7, 12)]),
        'ucer3':(9, [np.arange(8), np.arange(10, 15)]),
        'ecer3':(6, [np.arange(5), np.arange(7, 12)]),
        'ucer6':(9, [np.arange(3), np.arange(10, 15)]),
        'ecer6':(6, [np.arange(5), np.arange(7, 12)]),
        'chol' :(0, [np.arange(9)]),
        'ffa6' :(3, [np.arange(3)[::-1]]),
        'ffa16':(6, [np.arange(6)[::-1]]),
        'ffa18':(7, [np.arange(7)[::-1]]),
        'ffa20':(8, [np.arange(8)[::-1]]),
        'ffa22':(9, [np.arange(9)[::-1]]),
        'ffa24':(9, [np.arange(9)[::-1]])
        }
        
    return molecule