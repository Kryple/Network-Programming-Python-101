# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

# Gather and display information about local and remote machines using the socket module
import socket

# Print local machine infor
def print_current_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("Host name: %s" %host_name)
    print ("IP address: %s" %ip_address)

# Print remote machine infor  
def get_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print ("IP address of %s: %s" %(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print ("%s: %s" %(remote_host, err_msg))


if __name__ == '__main__':
    print_current_machine_info()
    get_remote_machine_info()
