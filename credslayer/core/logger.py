# coding: utf-8
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger("CredSlayer")

def debug(msg, *args):
    logger.debug(f"{msg} {' | '.join(args)}")

def info(msg, *args):
    logger.info(f"{msg} {' | '.join(args)}")

def error(msg, *args):
    logger.error(f"{msg} {' | '.join(args)}")

def found(session, msg):
    logger.info("[FOUND] [{} {}] {}".format(session.protocol, str(session), msg))
