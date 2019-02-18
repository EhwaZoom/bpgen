#!/usr/bin/env python

from bpgen.argparser import init_argparser 
from bpgen.command_handler import handle


def main():
    parser = init_argparser()
    arguments = parser.parse_args()
    handle(arguments)


if __name__ == '__main__':
    main()
