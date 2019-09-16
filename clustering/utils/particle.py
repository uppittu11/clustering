import numpy as np


class Particle(object):
    def __init__(self, pos=[[0, 0]], attributes=set()):
        self._pos = pos
        self._attributes = set(attributes)
        self._label = ""
    
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, position):
        try:
            assert np.array(position).shape[-1] == 2
            assert len(np.array(position).shape) == 2
        except AssertionError:
            raise ValueError("Expected position to have dim (N, 2). "
                             "Got dim {}".format(position.shape))
        self._pos = position

    def attributes(self):
        return self._attributes
    
    def add_attributes(self, attribute):
        if type(attribute) == set:
            self._attributes.update(attribute)
        else:
            self._attributes.update(set(attribute))
    
    def remove_attributes(self, attribute):
        if type(attribute) == set:
            self._attributes = self._attributes - attribute
        else:
            self._attributes.remove(attribute)
    
    def has_attribute(self, attribute):
        if type(attribute) == set:
            return attribute.issubset(self._attributes)
        else:
            return (attribute in self._attributes)
    
    def from_tail(self, tail):
        pos = tail.pos[:,:2]
        self._pos = pos
        self._attributes = tail.attributes()
    
    @property
    def label(self):
        return self._label
    
    @label.setter
    def label(self, l):
        self._label = str(l)
