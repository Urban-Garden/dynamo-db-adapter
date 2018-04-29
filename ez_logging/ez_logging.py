import logging
import logging.handlers
from pathlib import Path


def set_logging():
  ''' Sets logging module settings. 
  Run function at beginning of main function for uniform logging formatting.
  '''
  logging.basicConfig(filename='/dev/null', level=logging.DEBUG)
  log_formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

  debug_log = logging.handlers.RotatingFileHandler(str(Path.home()) + '/urban-garden.debug.log',maxBytes=65536,backupCount=5)
  debug_log.setLevel(logging.DEBUG)
  debug_log.setFormatter(log_formatter)

  info_log = logging.handlers.RotatingFileHandler(str(Path.home()) + '/urban-garden.info.log',maxBytes=65536,backupCount=5)
  info_log.setLevel(logging.INFO)
  info_log.setFormatter(log_formatter)

  logging.getLogger('').addHandler(debug_log)
  logging.getLogger('').addHandler(info_log)

