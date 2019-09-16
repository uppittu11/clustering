import numpy as np
from clustering.utils.lipid import Lipid


class Trajectory(object):
    def __init__(self):
        self._lipids = []
    
    @property
    def lipids(self):
        return self._lipids
    
    def add_lipid(self, lipid):
        self._lipids.append(lipid)
    
    def remove_lipid(self, index):
        self._lipids.pop(index)

    def tails(self, attribute):
        try:
            assert len(self.lipids) > 0
        except AssertionError:
            raise ValueError("There are no lipids in the trajectory")

        if attribute:
            return [tail for tail in lipid.tails() 
                         for lipid in self._lipids
                         if tail.has_attribute(attribute)]
        else:
            return [tail for tail in lipid.tails()
                         for lipid in self._lipids]
    
