import socket
import argparse

# installed packages
import dns # pip3 install dnspython
import dns.resolver

"""
    command line arguments
"""
parser = argparse.ArgumentParser(
    prog='Simple DNS explorer'
    )
# domain 
parser.add_argument(
    "-d",
    "--domain",
    required=False,
    help="Provide the domain to explore"
    )
# ip
parser.add_argument(
    "-ip",
    "--ip_address",
    required=False,
    help="Provide the ip address for the reverse DNS exploration")

# subdomain filepath
parser.add_argument(
    "-f",
    "--filepath",
    required=False,
    help="Provide the filepath for the subdomains textfile")


def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]]+result[1]
    except socket.herror:
        print(f"Error with reverse DNS using ip {ip}")
        return None

def DNSRequest(domain):
    ips = []
    try:
        result = dns.resolver.resolve(domain)
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names: %s" % ReverseDNS(answer.to_text()))
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout, dns.resolver.NoAnswer):
        print(f"Error for domain {domain}")
        return []
    return ips

def SubdomainSearch(domain, filepath, nums):
    successes = []

    dictionary = []

    with open(filepath,"r") as f:
        dictionary = f.read().splitlines()

    for word in dictionary:
        subdomain = word+"."+domain
        DNSRequest(subdomain)
        if nums:
            for i in range(0,10):
                s = word+str(i)+"."+domain
                DNSRequest(s)

args = parser.parse_args()
domain = args.domain
ip = args.ip_address
filepath = args.filepath

SubdomainSearch(domain, filepath, True)

#print(ReverseDNS(ip))