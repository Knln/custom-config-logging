import datetime
import enum
import inspect


class LogLevel(enum.IntEnum):
    FATAL = -1
    CRITICAL = 0
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4
    SPAM = 5


class Logger:

    def __init__(self):
        self._log_level = LogLevel.DEBUG.value

    def fatal(self, msg, *_):
        if self._log_level < LogLevel.FATAL.value:
            return
        else:
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            print('{} [{}] [{}] [{}] {}'.format(datetime.datetime.now(),
                                                LogLevel.FATAL.name,
                                                caller.filename.split('/')[-1],
                                                caller.function,
                                                msg))

    def critical(self, msg, *_):
        if self._log_level < LogLevel.CRITICAL.value:
            return
        else:
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            print('{} [{}] [{}] [{}] {}'.format(datetime.datetime.now(),
                                                LogLevel.CRITICAL.name,
                                                caller.filename.split('/')[-1],
                                                caller.function,
                                                msg))

    def error(self, msg, *_):
        if self._log_level < LogLevel.ERROR.value:
            return
        else:
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            print('{} [{}] [{}] [{}] {}'.format(datetime.datetime.now(),
                                                LogLevel.ERROR.name,
                                                caller.filename.split('/')[-1],
                                                caller.function,
                                                msg))

    def warn(self, msg, *_):
        if self._log_level < LogLevel.WARN.value:
            return
        else:
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            print('{} [{}] [{}] [{}] {}'.format(datetime.datetime.now(),
                                                LogLevel.WARN.name,
                                                caller.filename.split('/')[-1],
                                                caller.function,
                                                msg))

    def info(self, msg, *_):
        if self._log_level < LogLevel.INFO.value:
            return
        else:
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            print('{} [{}] [{}] [{}] {}'.format(datetime.datetime.now(),
                                                LogLevel.INFO.name,
                                                caller.filename.split('/')[-1],
                                                caller.function,
                                                msg))

    def debug(self, msg, *_):
        if self._log_level < LogLevel.DEBUG.value:
            return
        else:
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            print('{} [{}] [{}] [{}] {}'.format(datetime.datetime.now(),
                                                LogLevel.DEBUG.name,
                                                caller.filename.split('/')[-1],
                                                caller.function,
                                                msg))

    def spam(self, msg, *_):
        if self._log_level < LogLevel.SPAM.value:
            return
        else:
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            print('{} [{}] [{}] [{}] {}'.format(datetime.datetime.now(),
                                                LogLevel.SPAM.name,
                                                caller.filename.split('/')[-1],
                                                caller.function,
                                                msg))

    @property
    def log_level(self):
        """
        Gets current global log level
        :return str: _log_level
        """
        _log_level = LogLevel(self._log_level).name
        return _log_level

    @log_level.setter
    def log_level(self, log_level_name):
        """
        Setter to change global log levels
        :param log_level_name str: Log Level Name i.e. INFO
        """
        _log_level_name = LogLevel[log_level_name].value
        self._log_level = _log_level_name


logger = Logger()
