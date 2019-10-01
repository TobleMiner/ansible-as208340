import ipaddress

def rdns_hosts(net, fmt, start=0, end=None):
  hosts = list(ipaddress.ip_network(net).hosts())[start:end]
  return {
    addr.reverse_pointer: [ { 'ptr': fmt.format(addr.compressed) } ] for addr in hosts
  }

class FilterModule(object):
  def filters(self):
    return {
      'rdns_hosts': rdns_hosts
    }
