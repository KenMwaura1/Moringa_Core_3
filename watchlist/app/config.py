class Config:
    """
    General configuration parent class
    """
    pass


class Devconfig(Config):
    """
    Development configuration child class
    :param: Config parent configuration class with general configuration settings.
    """
    DEBUG = True


class ProdConfig(Config):
    """
    Product configuration child class
    :param: Config: parent class with general configuration settings.
    """
    pass
