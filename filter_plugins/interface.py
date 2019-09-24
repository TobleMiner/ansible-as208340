def normalize_addresses(addrs):
  if not isinstance(addrs, list):
    addrs = [ addrs ]

  normalized = [ ]
  for address in addrs:
    if not isinstance(address, dict):
      address = { 'address': address }
    if not 'flags' in address:
      address['flags'] = [ ]
    if not isinstance(address['flags'], list):
      address['flags'] = [ address['flags'] ]
    if not 'options' in address:
      address['options'] = { }
    normalized.append(address)

  primary = normalized[0]
  others = normalized[1:]

  return (primary, others)

def set_home_flag(addr):
  if not 'home' in addr['flags']:
    addr['flags'].append('home')
  return addr

def mtu_fixup(interface, ifname, interfaces):
  for iface in interfaces:
    if not 'managed' in iface or not iface['managed']:
      continue
    if iface['type'] != 'bridge':
      continue
    if not mtu in iface:
      continue
    if not 'slaves' in iface:
      continue
    slaves = iface['slaves'] if isinstance(iface['slaves'], list) else [ iface['slaves'] ]
    if not ifname in slaves:
      continue
    interface['mtu'] = iface['mtu']
    break

  return interface

class FilterModule(object):
  def filters(self):
    return {
      'interface_normalize_addresses': normalize_addresses,
      'interface_set_home_flag': set_home_flag,
      'interface_mtu_fixup': mtu_fixup,
    }
