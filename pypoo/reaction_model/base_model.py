class BaseReactionModel:
    """Base class for reaction models."""
    def compute(self, state, parameters):
        raise NotImplementedError
