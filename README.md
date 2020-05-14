# custom-config-logging
Custom Config and Logging Python Module

See example.py for usage

Logging can be imported and used as such:
    
    from logger import logger
    
    logger.critical("Critical Message")
    logger.log_level = 'INFO'
    logger.debug("This shouldn't print")

Config can be imported and used as such:
    
    from config import config
    
    if config.section.module_1.var:
        print('{var}'.format(var=config.section.module_1.var))