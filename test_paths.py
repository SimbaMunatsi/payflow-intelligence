from src.utils.logger import get_logger

logger = get_logger()

logger.info("Pipeline started.")

logger.info("Loading transactions.csv")

logger.warning("Duplicate transaction detected.")

logger.error("Unable to connect to database.")