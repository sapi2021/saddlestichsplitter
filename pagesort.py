from abc import ABCMeta, abstractclassmethod

class PageSort (metaclass=ABCMeta):
    @abstractclassmethod
    def sort(cls, lhs):
        pass

