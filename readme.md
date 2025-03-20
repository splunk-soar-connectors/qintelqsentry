# Qintel QSentry

Publisher: Qintel, LLC\
Connector Version: 1.0.1\
Product Vendor: Qintel\
Product Name: Qintel QSentry\
Product Version Supported (regex): ".\*"\
Minimum Product Version: 5.0.0

This app retrieves IP reputation and anonymization data from Qintel's QSentry platform

# Qintel QSentry App for Splunk SOAR

## Description

QSentry queries help measure the likelihood that a user is masking their identity using publicly or
privately available proxy or VPN services. The returns also flag any known fraud associations.
QSentry aggregates data from Qintel's proprietary Deep and DarkWeb research, as well as from
commercially available anonymization services.

For more information, existing customers can visit our [Integrations
Documentation](https://docs.qintel.com/integrations/overview)

## Actions

### ip reputation

Queries QSentry for IP reputation data. Returns the following:

- ASN
- ASN Name
- Last Seen
- Threat Tags
- Descriptions

### test connectivity

Test connectivity to the QSentry API

## Contact Information

*Sales:* contactus@qintel.com\
*Support:* integrations-support@qintel.com

## Legal and License

This Phantom App is licensed under the Apache 2.0 license.

## Port Information

The app uses HTTP/ HTTPS protocol for communicating with the Qintel QSentry server. Below are the
default ports used by the Splunk SOAR Connector.

| SERVICE NAME | TRANSPORT PROTOCOL | PORT |
|--------------|--------------------|------|
| http | tcp | 80 |
| https | tcp | 443 |

### Configuration Variables

The below configuration variables are required for this Connector to operate. These variables are specified when configuring a Qintel QSentry asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**token** | required | password | API Token
**remote** | optional | string | QSentry API URL (Optional)

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration\
[ip reputation](#action-ip-reputation) - Queries for IP intelligence data

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test**\
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'ip reputation'

Queries for IP intelligence data

Type: **investigate**\
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** | required | IP to query | string | `ip`

#### Action Output

DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action_result.parameter.ip | string | `ip`
action_result.data.\*.asn | string |
action_result.data.\*.asn_name | string |
action_result.data.\*.descriptions | string |
action_result.data.\*.last_seen | string |
action_result.data.\*.tags | string |
action_result.status | string |
action_result.message | string |
action_result.summary | string |
summary.total_objects | numeric |
summary.total_objects_successful | numeric |
