#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument(
        "-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument(
        "-l", "--lower", action="store_true", help="convert text to lowercase")
    parser.add_argument(
        "-t", "--title", action="store_true", help="convert text to titlecase")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    # the business LOGIC
    result = ns.text
    if ns.upper:
        result = result.upper()
    if ns.lower:
        result = result.lower()
    if ns.title:
        result = result.title()
    return result


if __name__ == '__main__':
    print(main(sys.argv[1:]))
