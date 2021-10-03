class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class PokemonNotFoundError(Error):
    """Exception raised for pokemon not found.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message = 'id or name is not found.'):
        self.expression = expression
        self.message = message

class ServerError(Error):

    def __init__(self, expression, message = 'server error, please try again later.'):
        self.expression = expression
        self.message = message