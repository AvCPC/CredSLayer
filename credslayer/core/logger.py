# coding: utf-8
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger("CredSlayer")

def debug(msg, *args):
    logging.debug(msg, *args)

def info(msg, *args):
    logging.info(msg, *args)

def error(msg, *args):
    logging.error(msg, *args)

def found(session, msg):
    logging.info("[FOUND] [{} {}] {}".format(session.protocol, str(session), msg))
