import logging

logging.basicConfig(filename="Program Log.log", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("Debug msg")
logger.info("Info msg")
logger.warning("Warning msg")
logger.error("Error msg")
logger.critical("Critical msg")
