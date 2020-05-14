from config import config
from logger import logger

if __name__ == "__main__":
    print(config.section.items())  # Config is just a dictionary of config items

    logger.critical("Mission critical!")  # Printing critical message

    if config.section.module_2.type == 'int':  # Checking if section is int
        logger.debug("Debugging")

    logger.log_level = 'INFO'  # Changing to INFO from DEBUG

    logger.debug("This shouldn't print!")  # Now it shouldn't print anything!
