#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: magic_numbers.py
Author: zlamberty
Created: 2018-10-18

Description:
    simple script to create magic numbers from gu511 student ids

Usage:
    <usage>

"""

import argparse
import hashlib
import logging
import logging.config
import os
import yaml

import numpy as np


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

HERE = os.path.dirname(os.path.realpath(__file__))
LOGGER = logging.getLogger('magic_numbers')
LOGCONF = os.path.join(HERE, 'logging.yaml')
with open(LOGCONF, 'rb') as f:
    logging.config.dictConfig(yaml.load(f))
LOGGER.setLevel(logging.INFO)


# ----------------------------- #
#   Main routine                #
# ----------------------------- #

def calc_magic_number(guid):
    """given a user's georgetown id, calculate a completely meaningless number

    args:
        guid (str): georgetown user id

    returns:
        None

    raises:
        None

    """
    h = hashlib.md5(guid.encode())
    seed = int(h.hexdigest(), 16) % (2 ** 32)
    LOGGER.info(seed)
    np.random.seed(seed)
    rands = np.random.random(20)
    LOGGER.info(rands)
    return rands.mean()


# ----------------------------- #
#   Command line                #
# ----------------------------- #

def parse_args():
    """parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--guid", help="your georgetown id", required=True)
    args = parser.parse_args()
    LOGGER.info("arguments set to {}".format(vars(args)))
    return args


if __name__ == '__main__':
    args = parse_args()
    print(calc_magic_number(args.guid))
