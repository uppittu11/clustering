import numpy as np
import mdtraj as md
from clustering.utils.molecules import collect_molecules

def _is_lipid(resname):
    """ Determine whether a residue name is an analyzeable lipid

    Parameters:
    -----------
    resname : string
        name of the residue to check

    Returns:
    --------
    boolean
        True if resname is in molecule. False otherwise
    """
    molecule = collect_molecules()
    return (resname in molecule)

def get_residuename(residue):
    name = None
    atoms = [atom.name for atom in residue.atoms]
    if 'chead' in atoms:
        name = 'chol'
    elif 'head' in atoms:
        if len(atoms) == 9:
            name = 'ffa24'
        elif len(atoms) == 6:
            name = 'ffa16'
    elif 'oh4' in atoms:
        if 'ter2' in atoms:
            name = 'ucer6'
        else:
            name = 'ecer6'
    elif 'oh3' in atoms:
        if 'ter2' in atoms:
            name = 'ucer3'
        else:
            name = 'ecer3'
    elif 'oh2' in atoms:
        if 'ter2' in atoms:
            name = 'ucer2'
        else:
            name = 'ecer2'
    elif 'water' in atoms:
        name = 'water'
    if name == None:
        raise KeyError("Residue {} ".format(residue.name) +
                        "is not in the database")
    return name

def get_standard_topology(traj):
    """ Load system information into a trajectory.
    CG systems: Based on the number and name of CG beads in a residue, 
    load in the correct residue name

    AA systems: Validate that all residue names are in the molecule
    list.

    Parameters:
    -----------
    traj : md.Trajectory
        Trajectory in which system information is loaded.

    Returns:
    --------
    traj : md.Trajectory
        Trajectory with information loaded.
    """

    for i, residue in enumerate(traj.top.residues):
        name = get_residuename(residue)
        traj.top.residue(i).name = name

    return traj

def get_tails(residue):
    tails = []
    molecules = collect_molecules()
    atom_indices = np.array(
                    [atom.index for atom in residue.indices])
    for tail in molecules[residue.name][1]:
        tails.append(atom_indices.take(tail))
    return tails
