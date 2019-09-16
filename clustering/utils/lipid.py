import numpy as numpy
from clustering.utils.tail import Tail

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
    
    def add_attributes(self, attribute):
        for tail in self._tails:
            tail.add_attributes(attribute)
    
    def remove_attributes(self, attribute):
        for tail in self._tails:
            tail.remove_attributes(attribute)
        
    def has_attribute(self, attribute):
        for tail in self._tails:
            if not tail.has_attribute(attribute):
                return False
        return True
    
    def _validate_tails(self, tails):
        try:
            assert type(tails) == list
            if len(tails) > 0:
                for tail in tails:
                    assert type(tail) == Tail
        except AssertionError:
            raise ValueError("Expected tails to be a list of Tail "
                             "objects.")

    def get_hairpin(self, head):
        try:
            assert head.shape[-1] == 3
        except AssertionError:
            raise ValueError("Expected head to have dim (N, 2). "
                             "Got dim {}".format(head.shape))
        