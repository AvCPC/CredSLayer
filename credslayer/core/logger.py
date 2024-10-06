# coding: utf-8
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger("CredSlayer")

def debug(msg, *args):
    logging.debug(f"{msg} {str(args)}")

def info(msg, *args):
    logging.info(f"{msg} {str(args)}")

def error(msg, *args):
    logging.error(f"{msg} {str(args)}")

def found(session, msg):
    logging.info("[FOUND] [{} {}] {}".format(session.protocol, str(session), msg))
