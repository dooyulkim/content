"""MSS Portal - MDR Integration for Cortex XSOAR - Unit Tests file

This file contains the Unit Tests for the "MSS Portal - MDR Integration based
on pytest. Cortex XSOAR contribution requirements mandate that every
integration, as well as a portal sync integration, should have a proper set of unit
tests to automatically verify that the integration is behaving as expected
during CI/CD pipeline.

Test Execution
--------------

Unit tests can be checked in 3 ways:
- Using the command `lint` of demisto-sdk. The command will build a dedicated
  docker instance for your mss portal integration locally and use the docker instance to
  execute your tests in a dedicated docker instance.
- From the command line using `pytest -v` or `pytest -vv`
- From PyCharm

Example with demisto-sdk (from the content root directory):
demisto-sdk lint -i Packs/TELUS-SOCaaS/Integrations/MSSPortalMDR

Coverage
--------

There should be at least one unit test per command function. In each unit
test, the target command function is executed with specific parameters and the
output of the command function is checked against an expected output.

Unit tests should be self contained and should not interact with external
resources like (API, devices, ...). To isolate the code from external resources
you need to mock the API of the external resource using pytest-mock:
https://github.com/pytest-dev/pytest-mock/

In the following code we configure requests-mock (a mock of Python requests)
before each test to simulate the API calls to the MSSPortalMDR API (which is
OpenPhish). This way we can have full control of the API behavior and focus only
on testing the logic inside the integration code.

We recommend to use outputs from the API calls and use them to compare the
results when possible. See the ``test_data`` directory that contains the data
we use for comparison, in order to reduce the complexity of the unit tests and
avoding to manually mock all the fields.

NOTE: we do not have to import or build a requests-mock instance explicitly.
requests-mock library uses a pytest specific mechanism to provide a
requests_mock instance to any function with an argument named requests_mock.

More Details
------------

More information about Unit Tests in Cortex XSOAR:
https://xsoar.pan.dev/docs/integrations/unit-testing

"""

import io
import json

from CommonServerPython import tableToMarkdown
from MSSPortalMDR import Client, get_alert_command
# from MSSPortalMDR import Client, create_alert_command, get_alert_command

URL = "https://portalservice.url"


def util_load_json(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


def test_get_alert_command(mocker):
    """
    Given:
        - Output of the portal API as list
    When:
        - Getting a alert from the Portal API
    Then:
        - Return results as war-room entry

    """
    client = Client(base_url=URL)
    result_alert = util_load_json('./test_data/get_alert_result.json')
    mocker.patch.object(Client, 'get_alert', return_value=result_alert)
    results = get_alert_command(client, args={'alert_id': '1'})
    human_readable = tableToMarkdown('MSSPortal Alert 1', result_alert)
    assert results.readable_output == human_readable
