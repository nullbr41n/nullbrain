#!/usr/bin/python3
import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='Nmap Scanner.')
parser.add_argument('--ip', dest='ip_addr', type=str, help='IP Address of Target host' )
parser.add_argument('--nmap_opt', dest='nmap_options',
        type=str,
        help="Nmap arguments",
        default="-sC -sV")

args = parser.parse_args()

#os.environ['TARGET_MACHINE'] = args.ip_addr

nmap_found_ports = subprocess.Popen(["/usr/bin/nmap -p- --min-rate=1000 -T4 " + args.ip_addr + " | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//"],
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        shell=True,
                        bufsize=0)

PORTS = nmap_found_ports.communicate()[0]
print(PORTS)

nmap_service = subprocess.Popen(["/usr/bin/nmap " + args.nmap_options + " -p" + PORTS + " " +  args.ip_addr],
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        shell=True,
                        bufsize=0)

for line in nmap_service.communicate():
    print(line.strip())
