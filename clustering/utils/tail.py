import numpy as np
from clustering.utils.particle import Particle

class Tail(Particle):
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, position):
        try:
            assert (np.array(position).shape[-1] == 2 or
                    np.array(position).shape[-1] == 3)
            assert len(np.array(position).shape) == 2
        except AssertionError:
            raise ValueError("Expected position to have dim (N, 2/3). "
                             "Got dim {}".format(position.shape))
        self._pos = position
    
    def to_particle(self):
        particle = Particle()
        particle.from_tail(self)
        return particle