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

def get_master(ifname, interfaces):
  for master_name in interfaces.keys():
    iface = interfaces[master_name]
    if not 'managed' in iface or not iface['managed']:
      continue
    if not 'slaves' in iface:
      continue
    slaves = iface['slaves'] if isinstance(iface['slaves'], list) else [ iface['slaves'] ]
    if not ifname in slaves:
      continue
    return master_name

  return None

def has_master(ifname, interfaces):
  return get_master(ifname, interfaces) != None

def mtu_fixup(interface, ifname, interfaces):
  if not has_master(ifname, interfaces):
    return interface

  master_name = get_master(ifname, interfaces)
  master = interfaces[master_name]

  if master['type'] != 'bridge':
    return interface
  if not mtu in master:
    return interface

  interface['mtu'] = master['mtu']
  return interface

class FilterModule(object):
  def filters(self):
    return {
      'interface_normalize_addresses': normalize_addresses,
      'interface_set_home_flag': set_home_flag,
      'interface_mtu_fixup': mtu_fixup,
      'interface_has_master': has_master
    }
