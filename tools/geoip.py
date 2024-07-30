import csv
import geoip2.database
import ipaddress


# Function to read network segments from a CSV file and filter based on conditions
def read_network_segments(file_path):
    network_segments = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Check if the value in the second or third column is 1814991
            if len(row) > 2 and (row[1] == '1814991' or row[2] == '1814991'):
                network_segments.append(row[0])  # The network column
    return network_segments


# Function to check if an IP range belongs to China
def is_chinese_ip(ip_range, reader):
    try:
        ip_net = ipaddress.ip_network(ip_range, strict=False)
        for ip in ip_net:
            try:
                response = reader.country(ip)
                if response and response.country.iso_code == 'CN':
                    return True
            except geoip2.errors.AddressNotFoundError:
                continue
    except ValueError:
        pass
    return False


# Main function
def generate_iptables_rules(ipv4_file, ipv6_file, geoip_db_path, output_file):
    with geoip2.database.Reader(geoip_db_path) as reader:
        # Read network segments from files
        ipv4_networks = read_network_segments(ipv4_file)
        ipv6_networks = read_network_segments(ipv6_file)

        with open(output_file, 'w') as output:
            # Check IPv4 networks
            for network in ipv4_networks:
                if is_chinese_ip(network, reader):
                    print(f"New IP Range：{network}")
                    output.write(f"iptables -A INPUT -s {network} -j DROP\n\n")

            # Check IPv6 networks
            for network in ipv6_networks:
                if is_chinese_ip(network, reader):
                    print(f"New IP Range：{network}")
                    output.write(f"ip6tables -A INPUT -s {network} -j DROP\n\n")


# Paths to your files
ipv4_file = 'GeoLite2-Country-Blocks-IPv4.csv'
ipv6_file = 'GeoLite2-Country-Blocks-IPv6.csv'
geoip_db_path = 'GeoLite2-Country.mmdb'
output_file = 'iptables_rules.sh'

# Generate iptables rules
generate_iptables_rules(ipv4_file, ipv6_file, geoip_db_path, output_file)

print(f'iptables rules have been written to {output_file}')
