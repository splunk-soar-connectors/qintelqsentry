# Qintel QSentry

Publisher: Qintel, LLC \
Connector Version: 1.0.1 \
Product Vendor: Qintel \
Product Name: Qintel QSentry \
Minimum Product Version: 5.0.0

This app retrieves IP reputation and anonymization data from Qintel's QSentry platform

### Configuration variables

This table lists the configuration variables required to operate Qintel QSentry. These variables are specified when configuring a Qintel QSentry asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**token** | required | password | API Token |
**remote** | optional | string | QSentry API URL (Optional) |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration \
[ip reputation](#action-ip-reputation) - Queries for IP intelligence data

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'ip reputation'

Queries for IP intelligence data

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** | required | IP to query | string | `ip` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.ip | string | `ip` | 1.2.3.4 |
action_result.data.\*.asn | string | | 12345 |
action_result.data.\*.asn_name | string | | Some Service Provider |
action_result.data.\*.descriptions | string | | |
action_result.data.\*.last_seen | string | | 2021-11-16T15:05:32.070497 |
action_result.data.\*.tags | string | | vpn,botnet |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
