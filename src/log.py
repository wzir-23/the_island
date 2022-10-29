""" Handle the logging """
import logging
import os


def setup_logging():
    """ Setup logging to text file """
    logfile = 'logfile.txt'
    if os.path.exists(logfile):
        os.remove(logfile)
    logging.basicConfig(filename=logfile,
                        level=logging.DEBUG,
                        format='%(message)s')
