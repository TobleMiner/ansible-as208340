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

class FilterModule(object):
  def filters(self):
    return {
      'interface_normalize_addresses': normalize_addresses
    }
