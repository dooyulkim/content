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

from typing import Dict, Any
import traceback


''' STANDALONE FUNCTION '''


def main():
    try:
        sys_conf = demisto.executeCommand("demisto-api-get", {"uri": "/system/config"})[0]["Contents"]["response"]["sysConf"]
        tsp_customer_id = sys_conf.get("tsp_customer_id")
        result = CommandResults(
            readable_output=f'Portal Customer ID : {tsp_customer_id}',
            outputs_prefix='MSSPortal',
            outputs_key_field='tsp_customer_id',
            outputs={'tsp_customer_id': tsp_customer_id}
        )
        return_results(result)
    except Exception as ex:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute BaseScript. Error: {str(ex)}')


''' ENTRY POINT '''


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
