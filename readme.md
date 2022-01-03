[comment]: # " File: readme.md"
[comment]: # ""
[comment]: # "  Copyright (c) 2022 Qintel, LLC"
[comment]: # ""
[comment]: # "  Licensed under the Apache License, Version 2.0 (the \"License\");"
[comment]: # "  you may not use this file except in compliance with the License."
[comment]: # "  You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "      http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "  Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "  the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "  either express or implied. See the License for the specific language governing permissions"
[comment]: # "  and limitations under the License."
[comment]: # ""
# Qintel QSentry App for Splunk SOAR

## Description

QSentry queries help measure the likelihood that a user is masking their identity using publicly or privately available
proxy or VPN services. The returns also flag any known fraud associations. QSentry aggregates data from Qintel’s
proprietary Deep and DarkWeb research, as well as from commercially available anonymization services.

For more information, existing customers can visit our
[Integrations Documentation](https://docs.qintel.com/integrations/overview).

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

_Sales:_ contactus@qintel.com

_Support:_ integrations-support@qintel.com

## Legal and License

This Phantom App is licensed under the Apache 2.0 license.

**Port Information**
*  The app uses HTTP/ HTTPS protocol for communicating with the Qintel QWatch server. Below are the default ports used by the Splunk SOAR Connector.

    SERVICE NAME | TRANSPORT PROTOCOL | PORT
    ------------ | ------------------ | ----
    http | tcp | 80
    https | tcp | 443