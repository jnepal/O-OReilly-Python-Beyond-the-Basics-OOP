import logging

logging.basicConfig(level=logging.INFO,
                    filename='example.log',
                    filemode='a', # default is append
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                    ) # default level is WARNING

logging.debug('This message will be ignored') # will not be printed as anything below INFO will be ignored
logging.info('This should be logged')
logging.warning('And, this too')