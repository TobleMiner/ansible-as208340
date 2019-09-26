def zone_fixup(zone):
  zone = zone.copy()
  for domain in zone:
    if not 'services' in domain:
      domain['services'] = [ ]
  return zone

def zone_unite(a, b):
  a = { domain['domain']: domain for domain in a }
  b = { domain['domain']: domain for domain in b }

  for domain_name in b.keys():
    if not domain_name in a:
      a[domain_name] = b[domain_name]
      continue

    domain_a = a[domain_name]
    domain_b = b[domain_name]
    if 'tll' in domain_b:
      domain_a['ttl'] = domain_b['ttl']

    records_a = domain_a['records']
    records_b = domain_b['records']
    for record_name in records_b.keys():
      if not record_name in records_a:
        records_a[record_name] = records_b[record_name]
        continue

      for record in records_b[record_name]:
        records_a[record_name].append(record)

    domain_a['records'] = records_a
    a[domain_name] = domain_a

  return list(a.values())

class FilterModule(object):
  def filters(self):
    return {
      'pdns_zone_fixup': zone_fixup,
      'pdns_zone_unite': zone_unite
    }