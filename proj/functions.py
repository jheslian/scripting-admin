"""
Module cpu_usage, cpu_percent, memory, disc, network

used to retrieves all data needed for supervising a machine
"""
import psutil
import mysql.connector


def cpu_usage():
    """
    returns the CPU has spent in the given mode
    """
    return psutil.cpu_times()


def cpu_percent():
    """
    returns the current system-wide CPU utilization as a percentage
    """
    return psutil.cpu_percent()


def memory():
    """
    return statistics about system memory usage
    """
    return psutil.virtual_memory()


def disc_usage():
    """
    returns information for every physical disk installed on the system
    """
    return psutil.disk_usage('/')


def network():
    """
    returns information for every network interface installed on the system as
    """
    return psutil.net_io_counters()


def db_insertion(sql, value):
    """
    write data to the database

    args:
        sql : sql statement to be excuted
        value : values to be insert to the database
    """
    try:
        conn = mysql.connector.connect(host="localhost",
                                       port="8889",
                                       database="system-admin",
                                       user="system",
                                       password="system")
    except mysql.connector.Error as e:
        print(f"Error connection to mySQL Database: {e}")
        return
    #
    # Create's cursor
    #
    cur = conn.cursor()
    #
    # Execute SQL statement and SQL value
    #
    cur.execute(sql, value)
    #
    # Commit DB
    #
    conn.commit()
    #
    # Close connection
    #
    conn.close()
