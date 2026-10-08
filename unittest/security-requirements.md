# Security Requirements for json_search()

SR1:
json_search() must verify the caller's role before returning a value
for a protected key.

SR2:
The apiKey field may only be returned when role="admin".

SR3:
The managementIpAddress field may only be returned when the role is
"admin" or "operator".

SR4:
The issueSummary field may be returned to "admin", "operator", and
"viewer".

SR5:
If a role is not authorized to access the requested key,
json_search() must return an empty list.

SR6:
If role is missing or invalid for a protected field,
json_search() must deny access by default and return an empty list.
