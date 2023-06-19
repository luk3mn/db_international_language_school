from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    """ Interface class from database

    """
    @abstractmethod
    def get_connect(self) -> object:
        """ connection method
        """
        raise ValueError("Connection failed!")

    @abstractmethod
    def close_connection(self) -> None:
        """ disconnection method
        """
        raise ValueError("Connection close failed!")
