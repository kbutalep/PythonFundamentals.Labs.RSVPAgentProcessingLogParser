#The log_parser script should iterate through the file and look for any instances
# where the log level is WARNING. Anytime it encounters a WARNING entry, it should output the following:
#
# the date and time of the entry followed by a space, double dashes, and another space
# the error message. The error message should exclude the colons and everything between them.
# Example output:
#
# WARNINGS:
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.

import re

with open('data/rsvp_agent_log.dat', 'r') as warn_log:
    print('WARNINGS:')
    for line in warn_log.readlines():
        if re.search('WARNING', line):
            print(re.sub(r'WARNING:\S+:', '--', line))
