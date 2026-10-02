# Threat Model for json_search()

## 1. Actors / Roles

The system supports three roles:

- admin:
  Can access apiKey, managementIpAddress, and issueSummary.

- operator:
  Can access managementIpAddress and issueSummary.
  Cannot access apiKey.

- viewer:
  Can access issueSummary only.
  Cannot access apiKey or managementIpAddress.

## 2. Assets

Sensitive assets that may be returned from the JSON data include:

- apiKey:
  SNMP authentication/community string.
  This is highly sensitive authentication information.

- managementIpAddress:
  Management IP address of a network device.
  This is internal infrastructure information.

- issueSummary:
  Network monitoring information.
  This is less sensitive and is allowed for all defined roles.

## 3. Trust Boundary

The trust boundary exists between the caller of json_search()
and the JSON data returned by the function.

If json_search() accepts a requested key and returns its value
without checking the caller's role, an unauthorized user may cross
this trust boundary and access protected information.

## 4. Threats

### T1 - Information Disclosure

A viewer or operator may search for the key "apiKey".
If json_search() does not verify role permissions, the function may
return the SNMP community string to an unauthorized user.

STRIDE category: Information Disclosure.

### T2 - Information Disclosure

A viewer may request "managementIpAddress".
Without role-based access control, the viewer may obtain internal
network management information.

STRIDE category: Information Disclosure.

### T3 - Elevation of Privilege

A low-privileged role may attempt to access a field reserved for a
higher-privileged role. If the function does not enforce the policy,
the caller effectively obtains privileges beyond its assigned role.

STRIDE category: Elevation of Privilege.
