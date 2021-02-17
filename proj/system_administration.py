"""
project administration system

this project consist of:
    - retrieves data with psutil library
    - data insertion to a file
    - data insertion to the database
"""

import time
import datetime
from functions import *


def main():
    """
    saves all the data changes into a file
    """
    #
    # open a file data.txt with writable property to save the data that was asked to be written such as:
    # cpu usage: percentage, user, system, idle
    # memory usage: percentage, used, available
    # disc usage: percentage, free, used
    # and network usage
    #
    file = open(r"data.txt", "a")
    file.writelines([
                        '\n\t\t\tPercentage'+('\t' * 8)+'CPU usage'+('\t' * 10) + 'Memory usage' + ('\t'*9) +
                        'Disk usage' + ('\t' * 8) + 'Network usage' + ('\t' * 6) + 'DateTime'])
    file.writelines([
                        '\n\tcpu %\tmemory %\tdisc %\t\t\t user\t\t\t sytem\t\t  idle\t\t\t\t   '
                        'used\t\t\tavailable\t\t\tfree\t\t\t  used\t\t\t\tfree\t\t\t\tbyte sent\t\t byte received '])
    while True:
        try:
            #
            # writes all data in every 10 seconds on data.txt file and database
            #
            time.sleep(10)
            file.writelines([' \n\t ' + str(cpu_percent())
                             + '\t  ' + str(memory().percent)
                             + '\t\t ' + str(disc_usage().percent)
                             + '\t\t\t' + str(cpu_usage().user)
                             + '\t\t' + str(cpu_usage().system)
                             + '\t\t' + str(cpu_usage().idle)
                             + '\t\t\t' + str(memory().used)
                             + '\t\t' + str(memory().available)
                             + '\t\t' + str(memory().free)
                             + '\t\t\t' + str(disc_usage().used)
                             + '\t\t' + str(disc_usage().free)
                             + '\t\t\t' + str(network().bytes_sent)
                             + '\t\t\t' + str(network().bytes_recv)
                             + '\t\t' + str(datetime.datetime.now())
                             ])

            #
            # data insertion to the database
            #
            value = (cpu_percent(),
                     cpu_usage().user,
                     cpu_usage().system,
                     cpu_usage().idle,
                     memory().percent,
                     memory().used,
                     memory().available,
                     disc_usage().used,
                     disc_usage().free,
                     disc_usage().percent,
                     network().bytes_sent,
                     network().bytes_recv)
            sql = "INSERT INTO system_usage(" \
                  "cpu_percent, " \
                  "cpu_user, " \
                  "cpu_system, " \
                  "cpu_idle, " \
                  "mem_percent, " \
                  "mem_used, " \
                  "mem_avail, " \
                  "disc_used, " \
                  "disc_free, " \
                  "disc_percent, " \
                  "net_byte_sent, " \
                  "net_byte_recv) " \
                  "VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s) "

            db_insertion(sql, value)

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    #
    # calls the main function
    #
    main()
