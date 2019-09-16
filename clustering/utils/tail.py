import numpy as np

class Tail(object):
    def __init__(self, pos, attributes=set()):
        self._pos = pos
        self._attributes = set(attributes)
    
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
    
    def remove_attribute(self, attribute):
        self._attributes.remove(attribute)
    
    def has_attribute(self, attribute):
        if type(attribute) == set:
            return attribute.issubset(self._attributes)
        else:
            return (attribute in self._attributes)

class Lipid(object):
    def __init__(self, tails=[]):
        self._validate_tails(tails)
        self._tails = tails
    
    @property
    def tails(self):
        return self._tails
    
    @tails.setter
    def tails(self, tails):
        self._validate_tails(tails)
        self._tails = tails
    
    def add_tail(self, tail):
        try:
            assert type(tail) == Tail
        except AssertionError:
            return ValueError("Expected tail to be a Tail object")
        self._tails.append(tail)
    
    def _validate_tails(self, tails):
        try:
            assert type(tails) == list
            if len(tails) > 0:
                for tail in tails:
                    assert type(tail) == Tail
        except AssertionError:
            raise ValueError("Expected tails to be a list of Tail "
                             "objects.")