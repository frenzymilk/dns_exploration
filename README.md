# DNS Explorer

A Python script for exploring DNS information, including resolving domain names and reverse DNS exploration.

## Purpose

The purpose of this project is to provide a basic DNS exploration tool. Given a list of common subdomains in a text file, it performs DNS queries to identify valid domain names. It can also explore reverse DNS information for a given IP address. 

## Dependencies

This project relies on the following Python packages:
- `dnspython`

These dependencies can be installed using:

```bash
pip3 install dnspython
```

## Usage

To use the DNS explorer, run the script with the desired command-line arguments:

```bash
python dns_explorer.py -d <domain> -f <subdomain filepath>
```
or 
```bash
python dns_explorer.py -ip <ip_address>
```

Example:
```bash
python dns_explorer.py -d example.com -f subdomains.txt
```
or 
```bash
python dns_explorer.py -ip 8.8.8.8
```

## Command Line Arguments

The script accepts the following command-line arguments:

- `-d` or `--domain`: Specify the target domain for DNS exploration.
- `-f` or `--filepath`: Provide the filepath for a text file containing the subdomains.
- `-ip` or `--ip_address`: Provide the IP address for reverse DNS exploration.
