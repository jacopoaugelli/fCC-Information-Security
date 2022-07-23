import socket
import re

def get_ports(target, port_range):
  try:
    open_ports = []
  
    for i in range(port_range[0],port_range[1]+1):
        
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.settimeout(1)
      result = client.connect_ex((target,i))
        
      if result == 0:
    
        open_ports.append(i)

    return open_ports
  except socket.gaierror:
    if re.search("[a-zA-Z]" , target):
      return "Error: Invalid hostname"
    else:
      return "Error: Invalid IP address"
  

def get_ports_verbose(target, port_range):
  ip = ""
  open_ports = get_ports(target, port_range)
  try:
    ip = socket.gethostbyname(target)
  except socket.gaierror:
    return "Invalid address"
  except socket.error:
    return "Invalid address"

  host = None
  try:
    host = socket.gethostbyaddr(ip)[0]
  except socket.herror:
    host = None

  l1 = "Open ports for"
  if host != None:
    l1 = l1 + " {url} ({ip})".format(url=host , ip=ip)
  else:
    l1 = l1 + " {ip}".format(ip=ip)
  l1 = l1 + "\n"
  l2 = "PORT     SERVICE\n"
  l3 = ""
  for i in open_ports:
    l3 = l3 + "{port}".format(port=i) + " "*(9-len(str(i))) + "{service}".format(service = socket.getservbyport(i))
    if open_ports[len(open_ports)-1] != i:
      l3 = l3 + "\n"
  return l1 + l2 + l3
  
def get_open_ports(target, port_range, verbose=False):
    
  if verbose:
      return get_ports_verbose(target, port_range)
    
  else:
      return get_ports(target , port_range)