"""
Command Line Interface for Shapepy
"""

import argparse


def get_args():
    """ Parse arguments from stdin with argparse """
    parser = argparse.ArgumentParser(
        description="A Python tool for programatically defining structures",
    )
    return parser.parse_args()


def handle():
    """ Execute the cli function """
    args = get_args()


if __name__ == "__main__":
    handle()