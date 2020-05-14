import configparser
import os


class _AttrDict(dict):
    """
    Changes dictionaries to an attribute of an object
    Users can call config.section.<section_name>.<section_variable> to retrieve values
    """
    def __init__(self, *args, **kwargs):
        super(_AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Config(configparser.ConfigParser):
    """
    Initialises the path to config.ini.
    Can take a custom ini file given the path.
    :param str file: Takes a ini file path
    """
    def __init__(self, file=None):

        if file is None:
            directory = os.path.dirname(os.path.realpath(__file__))
            file = os.path.join(directory, 'config.ini')

        super().__init__(dict_type=_AttrDict)
        self.read(file)

    @property
    def section(self):
        return self._sections


config = Config()
