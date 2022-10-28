import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401


"""Base Script for Cortex XSOAR (aka Demisto)
This is an empty script with some basic structure according
to the code conventions.
MAKE SURE YOU REVIEW/REPLACE ALL THE COMMENTS MARKED AS "TODO"
Developer Documentation: https://xsoar.pan.dev/docs/welcome
Code Conventions: https://xsoar.pan.dev/docs/integrations/code-conventions
Linting: https://xsoar.pan.dev/docs/integrations/linting
"""

import traceback


''' STANDALONE FUNCTION '''


def main():
    try:
        sys_conf = demisto.executeCommand("demisto-api-get", {"uri": "/system/config"})[0]["Contents"]["response"]["sysConf"]
        tsp_customer_id = sys_conf.get("tsp_customer_id")
        if not tsp_customer_id:
            raise Exception("Sorry, tsp_customer_id is not found. Please add it to server configuration under About -> troubleshoot")
        result = CommandResults(
            readable_output=f'Portal Customer ID : {tsp_customer_id}',
            outputs_prefix='MSSPortal.CustomerInfo',
            outputs_key_field='id',
            outputs={'id': tsp_customer_id}
        )
        return_results(result)
    except Exception as ex:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(
            f'Failed to execute demisto-api-get. Please make sure that Demisto REST API integration is installed and configured. Error: {str(ex)}')


''' ENTRY POINT '''


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
