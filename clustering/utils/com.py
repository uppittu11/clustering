import numpy as np
import mdtraj as md

def compute_com(xyz, masses):
    try:
        assert len(xyz.shape) == 3
        assert xyz.shape[-1] == 3
    except (AssertionError):
        raise ValueError("Found array with dim {}.".format(xyz.shape) +
                         " Expected (N, M, 3).")
    try:
        assert masses.shape[0] == xyz.shape[0]
    except (AssertionError):
        raise ValueError("Masses and xyz must have the same length")
    
    com = np.mean(xyz * masses[:,None], axis=0)

    return com

def tail_com(traj, indices):
    xyz = traj.xyz[:,indices,:]
    masses = [traj.top.atom(i).element.mass for i in indices]
    masses = np.array(masses)
    com = compute_com(xyz, masses)
    return com