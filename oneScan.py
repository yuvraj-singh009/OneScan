import subprocess
import re

def netdiscover():
 comm= ["sudo","netdiscover","-i","eth0"]
 process = subprocess.Popen(comm, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
 output, error = process.communicate()

 devices = []

    # REGEX pattern to extract IP, MAC, vendor from netdiscover output
 pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([A-Fa-f0-9:]{17})\s+(.+?)\s+\w"

 for line in output.splitlines():
        match = re.search(pattern, line)
        if match:
            ip, mac, vendor = match.groups()
            devices.append({"ip": ip, "mac": mac, "vendor": vendor.strip()})

 return devices


def nmap(ip):
    print("running command for nmap")
    cmd=["nmap","-sV", ip]
    process=subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return output



if __name__ == "__main__":

# ip = int(input("enter your ip:"))
 devices = netdiscover()

 for device in devices:
    print("--------------------------------------------")
    print(f"Device: {device['ip']}")
    print(f"MAC:    {device['mac']}")
    print(f"Vendor: {device['vendor']}")
    print("--------------------------------------------")
    nmap_output= nmap(device['ip'])
    print(nmap_output)
    print("--------------------------------------------\n")






