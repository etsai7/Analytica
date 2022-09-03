import logging

class LoggerFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629
        Taken from: https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/
        Additional Colors: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
    """

    grey = '\x1b[38;5;8m'
    blue = '\x1b[38;5;38m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def test_logger():
    # Create custom logger logging all five levels
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Define format for logs
    format = '%(asctime)s | %(levelname)8s | %(message)s'

    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(LoggerFormatter(format))

    # This is for logging to file
    # today = datetime.date.today()
    # file_handler = logging.FileHandler('my_app_{}.log'.format(today.strftime('%Y_%m_%d')))
    # file_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(logging.Formatter(fmt))

    logger.addHandler(stdout_handler)
    logger.info("testing the logger")
    logger.warning("warning with the logger")


log = None


def create_logger():
    log = logging.getLogger('log')
    log.setLevel(logging.DEBUG)
    fmt = '%(asctime)s | %(levelname)8s | %(message)s'
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(LoggerFormatter(fmt))
    log.addHandler(stdout_handler)


def get_logger():
    if log is None:
        create_logger()
    return log
