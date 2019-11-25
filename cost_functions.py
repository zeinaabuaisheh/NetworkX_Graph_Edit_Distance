import abc
import six


@six.add_metaclass(abc.ABCMeta)
class CostFunctions(object):

    @abc.abstractmethod
    def node_substitution_cost(self, start, end):
        pass

    @abc.abstractmethod
    def node_deletion_cost(self, start):
        pass

    @abc.abstractmethod
    def node_insertion_cost(self, end):
        pass

    @abc.abstractmethod
    def edge_substitution_cost(self, start, end):
        pass

    @abc.abstractmethod
    def edge_deletion_cost(self, start):
        pass

    @abc.abstractmethod
    def edge_insertion_cost(self, end):
        pass



