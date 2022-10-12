import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
# import json
import urllib3
# import dateparser
import traceback
# from typing import Any, Dict, Tuple, List, Optional, Union, cast
from typing import Any, Dict

# Disable insecure warnings
urllib3.disable_warnings()


''' CONSTANTS '''


DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

''' CLIENT CLASS '''


class Client(BaseClient):
    """Client class to interact with the service API

    This Client implements API calls, and does not contain any Demisto logic.
    Should only do requests and return data.
    It inherits from BaseClient defined in CommonServer Python.
    Most calls use _http_request() that handles proxy, SSL verification, etc.
    For this MSSPortal implementation, no special attributes defined
    """

    def getCurrentUserIdentity(self) -> Dict[str, Any]:
        """Gets cirremt user's identity
        This methods will be used mainly to test API connectivity
        """

        return self._http_request('get', '/identities/current')

    def get_alert(self, alert_id: str) -> Dict[str, Any]:
        """Gets a specific MSSPortal alert by id

        :type alert_id: ``str``
        :param alert_id: id of the alert to return

        :return: dict containing the alert as returned from the API
        :rtype: ``Dict[str, Any]``
        """

        return self._http_request('get', f'/alerts/{alert_id}')

    def update_case(self, case_id: str, data: Dict[str, Any]) -> str:
        """Updates a specific MSSPortal case by id

        :type case_id: ``str``
        :param case_id: id of the case to update

        :return: string from the API call
        :rtype: ``str``
        """

        return self._http_request('put', f'/cases/{case_id}', json_data=data, resp_type='text')

    def acknowledge_case(self, case_id: str) -> str:
        """Acknowledge a specific MSSPortal case by id

        :type case_id: ``str``
        :param case_id: id of the case to acknowledge

        :return: string from the API call
        :rtype: ``str``
        """

        return self._http_request('put', f'/cases/{case_id}/acknowledgement', resp_type='text')

    def create_alert(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Gets a specific MSSPortal alert by id

        :type: dict containing the alert
        :param ``Dict[str, Any]``

        :return: dict containing the alert as returned from the API
        :rtype: ``Dict[str, Any]``
        """

        return self._http_request('post', '/alerts', json_data=data)


''' HELPER FUNCTIONS '''


''' COMMAND FUNCTIONS '''


def test_module(client: Client) -> str:
    """Tests API connectivity

    Returning 'ok' indicates that the integration works like it is supposed to.
    Connection to the service is successful.
    Raises exceptions if something goes wrong.

    :type client: ``Client``
    :param Client: MSSPortal client to use

    :type name: ``str``
    :param name: name to append to the 'Hello' string

    :return: 'ok' if test passed, anything else will fail the test.
    :rtype: ``str``
    """

    # INTEGRATION DEVELOPER TIP
    # Client class should raise the exceptions, but if the test fails
    # the exception text is printed to the Cortex XSOAR UI.
    # If you have some specific errors you want to capture (i.e. auth failure)
    # you should catch the exception here and return a string with a more
    # readable output (for example return 'Authentication Error, API Key
    # invalid').
    # Cortex XSOAR will print everything you return different than 'ok' as
    # an error
    try:
        client.getCurrentUserIdentity()
    except DemistoException as e:
        if 'Forbidden' in str(e):
            return 'Authorization Error: make sure API Key is correctly set'
        else:
            raise e
    return 'ok'


def get_alert_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    """mssportal-get-alert command: Returns a MSSPortal alert

    :type client: ``Client``
    :param Client: MSSPortal client to use

    :type args: ``Dict[str, Any]``
    :param args:
        all command arguments, usually passed from ``demisto.args()``.
        ``args['alert_id']`` alert ID to return

    :return:
        A ``CommandResults`` object that is then passed to ``return_results``,
        that contains an alert

    :rtype: ``CommandResults``
    """

    alert_id = args.get('alert_id', None)
    if not alert_id:
        raise ValueError('alert_id not specified')

    alert = client.get_alert(alert_id)

    # tableToMarkdown() is defined is CommonServerPython.py and is used very
    # often to convert lists and dicts into a human readable format in markdown
    readable_output = tableToMarkdown(f'MSSPortal Alert {alert_id}', alert)

    return CommandResults(
        readable_output=readable_output,
        outputs_prefix='MSSPortal.Alert',
        outputs_key_field='id',
        outputs=alert
    )


def update_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    """mssportal-update-case command: Returns a MSSPortal case

    :type client: ``Client``
    :param Client: MSSPortal client to use

    :type args: ``Dict[str, Any]``
    :param args:
        all command arguments, usually passed from ``demisto.args()``.
        ``args['case_id']`` alert ID to return

    :return:
        A ``CommandResults`` object that is then passed to ``return_results``,
        that contains the result of case update

    :rtype: ``CommandResults``
    """

    case_id = args.get('case_id', None)
    if not case_id:
        raise ValueError('case_id not specified')

    json_data: Dict[str, Any] = {}

    status = args.get('status')
    if not status:
        json_data['status'] = status
    telusPrime = args.get('telusPrime')
    if not status:
        json_data['telusPrime'] = telusPrime
    description = args.get('description')
    if not status:
        json_data['description'] = description
    caseTitle = args.get('caseTitle')
    if not status:
        json_data['caseTitle'] = caseTitle
    priority = args.get('priority')
    if not priority:
        json_data['priority'] = priority
    resolutionNotes = args.get('resolutionNotes')
    if not resolutionNotes:
        json_data['resolutionNotes'] = resolutionNotes

    client.update_case(case_id, json_data)

    return CommandResults(
        readable_output=f'MSSPortal Case {case_id} updated'
    )


def acknowledge_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    """mssportal-acknowledge-alert command: Returns a MSSPortal case

    :type client: ``Client``
    :param Client: MSSPortal client to use

    :type args: ``Dict[str, Any]``
    :param args:
        all command arguments, usually passed from ``demisto.args()``.
        ``args['case_id']`` case ID to return

    :return:
        A ``CommandResults`` object that is then passed to ``return_results``,
        that contains an alert

    :rtype: ``CommandResults``
    """

    case_id = args.get('case_id', None)
    if not case_id:
        raise ValueError('case_id not specified')

    client.acknowledge_case(case_id)

    return CommandResults(
        readable_output=f'MSSPortal Case {case_id} acknowledged'
    )


def create_alert_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    """mssportal-get-alert command: Returns a MSSPortal alert

    :type client: ``Client``
    :param Client: MSSPortal client to use

    :type args: ``Dict[str, Any]``
    :param args:
        all command arguments, usually passed from ``demisto.args()``.
        ``args['alert_id']`` alert ID to return

    :return:
        A ``CommandResults`` object that is then passed to ``return_results``,
        that contains an alert

    :rtype: ``CommandResults``
    """

    provider_id = args.get('provider_id')
    if not provider_id:
        raise ValueError('provider_id not specified')
    alert_id = args.get('alert_id')
    if not alert_id:
        raise ValueError('alert_id not specified')
    created_at = args.get('created_at')
    if not created_at:
        raise ValueError('created_at not specified')
    modified_at = args.get('modified_at')
    if not modified_at:
        raise ValueError('modified_at not specified')
    raw_data = args.get('raw_data', '{}')
    if not raw_data:
        raise ValueError('raw_data not specified')
    severity = args.get('severity')
    if not severity:
        raise ValueError('severity not specified')
    customer_id = args.get('customer_id',)
    if not customer_id:
        raise ValueError('customer_id not specified')
    investigation_case_id = args.get('investigation_case_id')
    name = args.get('name')
    if not name:
        raise ValueError('name not specified')
    related_case_description = args.get('related_case_description')
    related_case_title = args.get('related_case_title')

    json_data = {
        "providerId": provider_id,
        "providerCreatedAt": created_at,
        "providerModifiedAt": modified_at,
        "providerAlertId": alert_id,
        "providerRaw": raw_data,
        "severity": severity,
        "customerId": customer_id,
        "investigationCaseId": investigation_case_id,
        "name": name,
        "Related case description": related_case_description,
        "Related case title": related_case_title
    }

    alert = client.create_alert(json_data)

    # INTEGRATION DEVELOPER TIP
    # We want to convert the "created" time from timestamp(s) to ISO8601 as
    # Cortex XSOAR customers and integrations use this format by default

    # tableToMarkdown() is defined is CommonServerPython.py and is used very
    # often to convert lists and dicts into a human readable format in markdown

    readable_output = tableToMarkdown(f'MSSPortal Alert {alert_id}', alert)

    return CommandResults(
        readable_output=readable_output,
        outputs_prefix='MSSPortal.Alert',
        outputs_key_field='alert_id',
        outputs=alert
    )


''' MAIN FUNCTION '''


def main() -> None:
    """main function, parses params and runs command functions

    :return:
    :rtype:
    """

    api_key = demisto.params().get('api_key')

    # get the service API url
    base_url = urljoin(demisto.params()['url'], '/api/v1')

    # if your Client class inherits from BaseClient, SSL verification is
    # handled out of the box by it, just pass ``verify_certificate`` to
    # the Client constructor
    verify_certificate = not demisto.params().get('insecure', True)

    # if your Client class inherits from BaseClient, system proxy is handled
    # out of the box by it, just pass ``proxy`` to the Client constructor
    proxy = demisto.params().get('proxy', False)

    # INTEGRATION DEVELOPER TIP
    # You can use functions such as ``demisto.debug()``, ``demisto.info()``,
    # etc. to print information in the XSOAR server log. You can set the log
    # level on the server configuration
    # See: https://xsoar.pan.dev/docs/integrations/code-conventions#logging

    demisto.debug(f'Command being called is {demisto.command()}')
    try:
        headers = {
            'X-Lestrade-Key-ID': 'xsoar',
            'X-Lestrade-Key': api_key
        }
        client = Client(
            base_url=base_url,
            verify=verify_certificate,
            headers=headers,
            proxy=proxy)

        if demisto.command() == 'test-module':
            # This is the call made when pressing the integration Test button.
            result = test_module(client)
            return_results(result)

        elif demisto.command() == 'mssportal-get-alert':
            return_results(get_alert_command(client, demisto.args()))
        elif demisto.command() == 'mssportal-update-case':
            return_results(update_case_command(client, demisto.args()))
        elif demisto.command() == 'mssportal-acknowledge-case':
            return_results(acknowledge_case_command(client, demisto.args()))
        elif demisto.command() == 'mssportal-create-alert':
            return_results(create_alert_command(client, demisto.args()))

    # Log exceptions and return errors
    except Exception as e:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute {demisto.command()} command.\nError:\n{str(e)}')


''' ENTRY POINT '''

if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
