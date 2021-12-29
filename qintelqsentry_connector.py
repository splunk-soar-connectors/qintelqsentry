# File: qintelqsentry_connector.py
#
# Copyright (c) 2009-2021 Qintel, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

import json
import os
from copy import deepcopy

# Phantom App imports
import phantom.app as phantom
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector

from qintelqsentry_helper import search_qsentry
from qintelqsentry_consts import *


class QSentryConnector(BaseConnector):

    def __init__(self):

        # Call the BaseConnectors init first
        super(QSentryConnector, self).__init__()

        self._state = None

    def _handle_test_connectivity(self):

        try:
            res = search_qsentry('1.1.1.1', **self.client_args)
            self.debug_print('qsentry test connectivity return: ', res)
        except Exception as e:
            self.debug_print('qsentry test connectivity error: ', e)
            self.set_status(phantom.APP_ERROR,
                            'QSentry Connectivity Test Failed ', e)
            return self.get_status()

        self.save_progress('Test Connectivity Successful')
        return self.set_status(phantom.APP_SUCCESS, 'Test Connectivity Successful')

    def _init_handler(self, param, field):

        self.save_progress("In action handler for: {0}"
                           .format(self.get_action_identifier()))

        action_result = self.add_action_result(ActionResult(dict(param)))

        return param.get(field), action_result

    def _qsentry_query(self, ip, search_args=None):

        kwargs = deepcopy(self.client_args)
        if search_args:
            kwargs.update(search_args)

        try:
            return search_qsentry(ip, **kwargs)
        except Exception as e:
            self.debug_print('qsentry lookup failed: ', e)
            raise Exception(str(e))

    def _process_qsentry_data(self, response, summary):

        rv = {}

        for k, v in response.items():
            rv[k] = v

        if 'criminal' in rv['tags']:
            summary['criminal'] = True

        if 'vpn' in rv['tags'] or 'proxy' in rv['tags']:
            summary['anonymization'] = True

        return rv

    def _handle_ip_reputation(self, param):

        ip, action_result = self._init_handler(param, 'ip')

        if not ip:
            self.debug_print(f'missing ip parameter for '
                             f'{self.get_action_identifier()}')
            self.set_status(phantom.APP_ERROR, 'Missing ip address for lookup')
            return self.get_status()

        summary = {'criminal': False, 'anonymization': False}

        try:
            response = self._qsentry_query(ip)
        except Exception as e:
            return action_result.set_status(phantom.APP_ERROR, str(e))

        if isinstance(response, dict):
            rv = self._process_qsentry_data(response, summary)
            action_result.add_data(rv)

        action_result.update_summary(summary)

        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):

        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()
        self.debug_print("action_id", self.get_action_identifier())

        if action_id == 'test_connectivity':
            ret_val = self._handle_test_connectivity()

        elif action_id == 'ip_reputation':
            ret_val = self._handle_ip_reputation(param)

        return ret_val

    def initialize(self):

        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()

        if not isinstance(self._state, dict):
            self.debug_print("Resetting the state file with the default format")
            self._state = {
                "app_version": self.get_app_json().get('app_version')
            }
            return self.set_status(phantom.APP_ERROR, QINTELQSENTRY_STATE_FILE_CORRUPT_ERR)

        config = self.get_config()
        self._proxies = {}
        env_vars = config.get('_reserved_environment_variables', {})
        if 'HTTP_PROXY' in env_vars:
            self._proxies['http'] = env_vars['HTTP_PROXY']['value']
        elif 'HTTP_PROXY' in os.environ:
            self._proxies['http'] = os.environ.get('HTTP_PROXY')

        if 'HTTPS_PROXY' in env_vars:
            self._proxies['https'] = env_vars['HTTPS_PROXY']['value']
        elif 'HTTPS_PROXY' in os.environ:
            self._proxies['https'] = os.environ.get('HTTPS_PROXY')

        self.plaintext_passwords = config.get('qwatch_fetch_password')

        self.client_args = {
            'remote': config.get('remote'),
            'token': config['token'],
            'user_agent': USER_AGENT,
            'logger': self.debug_print,
            'proxies': self._proxies
        }

        return phantom.APP_SUCCESS

    def finalize(self):

        # Save the state, this data is saved across actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS


if __name__ == '__main__':

    import sys

    if (len(sys.argv) < 2):
        print("No test json specified as input")
        sys.exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = QSentryConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    sys.exit(0)
