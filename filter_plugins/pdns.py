from copy import deepcopy

def sanitize_domain(z):
  zone = { }
  zone['domain'] = str(z['domain'])
  if 'ttl' in z:
    zone['ttl'] = int(z['ttl'])
  zone['records'] = { }
  records = deepcopy(z['records']) if 'records' in z else { }
  for (record_name, records_name) in records.items():
    zone['records'][str(record_name)] = [ { str(k): str(v) } for record in deepcopy(records_name) for (k, v) in record.items() ]

  return zone

def zone_fixup(zone):
  zone = [ sanitize_domain(domain) for domain in deepcopy(zone) ]
  for domain in zone:
    if not 'services' in domain:
      domain['services'] = [ ]
  return zone

def zone_unite(zone1, zone2):
  a = { domain['domain']: domain for domain in deepcopy(zone1) }
  b = { domain['domain']: domain for domain in zone2 }

  zone1.clear()

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

    dnyamic_records_a = domain_a.get('dynamic_records', [])
    dynamic_records_b = domain_b.get('dynamic_records', [])
    dnyamic_records_a.extend(dynamic_records_b)
    domain_a['dynamic_records'] = dnyamic_records_a

    a[domain_name] = domain_a

  zone1.extend(a.values())
  return zone1

class FilterModule(object):
  def filters(self):
    return {
      'pdns_zone_fixup': zone_fixup,
      'pdns_zone_unite': zone_unite
    }
