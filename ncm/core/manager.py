# coding: utf-8

import time

from pyshark.packet.packet import Packet

from ncm.core import logger, utils, extract
from ncm.parsers import parsers
import pyshark


def _process_packet(packet: Packet):

    # We drop non-tcp packets (for now)
    if "tcp" not in packet:
        return

    emails_found = extract.extract_emails(packet)
    credit_cards_found = extract.extract_credit_cards(packet)

    for email in emails_found:
        logger.info("Found email address: " + email)

    for credit_card in credit_cards_found:
        logger.info("Credit card '{}' found: '{}'".format(credit_card.name, credit_card.number))

    if len(packet.layers) > 3:  # == tshark parsed something else than ETH, IP, TCP
        for layer in packet.layers[3:]:
            layer_name = layer.layer_name

            if layer_name in parsers:
                creds = parsers[layer_name].analyse(packet)

                if creds:
                    logger.found(layer_name.upper(), creds)


def process_pcap(filename: str):

    pcap = pyshark.FileCapture(filename)
    logger.debug("Processing packets in '{}'".format(filename))

    start_time = time.time()

    # TODO: at given time (every INACTIVE_SESSION_DELAY seconds ?) clean inactive sessions, log uncomplete credentials ?

    for packet in pcap:
        _process_packet(packet)

    logger.debug("Processed in {0:.3f} seconds.".format(time.time() - start_time))


def active_processing(interface: str):
    logger.info("Listening on {}...".format(interface))
