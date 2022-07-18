#!/usr/bin/python3
"""
DOC
"""
import argparse
import subprocess
from os.path import expanduser
import os
import sys

parser = argparse.ArgumentParser(description='Nmap Scanner.')
parser.add_argument('--ip', dest='ip_addr', type=str, help='IP Address of Target host' )
parser.add_argument('--min_rate', dest='min_rate', type=str, help='nmap min rate', default='1000')
parser.add_argument('--skip_workdir', dest='skip_workdir',
        type=bool,help='Toggle to skip creating workdir creation', default=False)
parser.add_argument('--skip_portscan', dest='skip_portscan',
        type=bool, help='Toggle to skip port scanning', default=False)
parser.add_argument('--ports', dest='ports', type=str, help='comma seperated ports', default=None)
parser.add_argument('--nmap_opt', dest='nmap_options',
        type=str,
        help="Nmap arguments",
        default="-sC -sV")

args = parser.parse_args()

if args.skip_portscan and not args.ports:
    print("When skipping portscan, ports must be provided e.g: '80,22'")
    sys.exit(1)


#Prep filesystem

if not args.skip_workdir:
    home = expanduser("~")
    path = home + "/offsec/" + args.ip_addr

    # Check whether the specified path exists or not
    DIREXISTS = os.path.exists(path)

    if not DIREXISTS:
        # Create a new directory because it does not exist
        os.makedirs(path + "/enum")
        print("Directory for " + path + "/enum created!")

def port_scan():
    """
    Function: port_scan()

    """
    if not args.skip_portscan:
        with subprocess.Popen(["/usr/bin/nmap -p- --min-rate=" + args.min_rate + \
          " -T4 " + args.ip_addr + " | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//"],
                              stdin =subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              universal_newlines=True,
                              shell=True,
                              bufsize=0) as nmap_found_ports:
            open_ports = nmap_found_ports.communicate()[0]
    else:
        open_ports = args.ports

    return open_ports


ports_to_scan = port_scan()
print("Ports to scan", ports_to_scan)

def svc_scan():
    """
    Function svc_scan:
    """
    with subprocess.Popen(["/usr/bin/nmap " + args.nmap_options + " -p" + \
        ports_to_scan + " " +  args.ip_addr + " -oN " + path + "/enum/nmap_results.log"],
                            stdin =subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            shell=True,
                            bufsize=0) as nmap_service:

        for line in nmap_service.communicate():
            print(line.strip())


port_scan()
svc_scan()
