#! /usr/bin/env python3

import os
import re

default_header = \
    """# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host
# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost
"""

custom_header = \
    """# Hosts file generated by Adwin.
# Changes to this file will be lost.
"""

# Constant for the system hosts pah
HOSTS_PATH = os.environ["SYSTEMROOT"] + r"\System32\Drivers\etc\hosts"


def read(hosts_file):  # Read mode "r"
    hosts_list = []

    for host_line in hosts_file.readlines():
        host_line = host_line.strip()

        if host_line and not host_line.startswith("#"):
            hosts_list.append(re.split(r"\s+", host_line, 2)[1])

    return list(set(hosts_list))  # Fastest possible way to remove duplicates


def write(hosts_file, hosts_list, local=False):  # Append mode "a"
    hosts_file.seek(0)
    hosts_file.truncate()

    if hosts_list:
        hosts_file.write(custom_header)

        for host in hosts_list:
            hosts_file.write(("127.0.0.1 " if local else "0.0.0.0 ") + host +
                             ("\n::1 " if local else"\n:: ") + host + "\n")
    else:
        hosts_file.write(default_header)


def append(hosts_file, host, local=False):
    hosts_file.write(("127.0.0.1 " if local else "0.0.0.0 ") + host +
                     ("\n::1 " if local else "\n:: ") + host + "\n")


def clear(hosts_file):  # Write mode "w"
    hosts_file.write(default_header)
