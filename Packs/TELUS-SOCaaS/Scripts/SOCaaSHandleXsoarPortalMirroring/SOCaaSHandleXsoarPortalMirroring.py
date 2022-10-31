import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401


def main():
    try:
        id = demisto.context()["MSSPortal"]["CaseInfo"]["id"]
        findCaseResult = demisto.executeCommand("mssportal-find-case", {'id_': id})
        if is_error(findCaseResult):
            return_error(findCaseResult)
        else:
            case = findCaseResult[0]['Contents']
            if((not case['nbTelusPendingTasks'] or case['nbTelusPendingTasks'] == 0) and case['nbCustomerClosedTasks'] == case['nbCustomerTasks']):
                demisto.executeCommand("mssportal-resolve-case", {'id_': id, 'caseresolution_resolutionnotes': 'Closure via mirroring'})
                print(f'Case({case["id"]}) resolved')
            else:
                raise DemistoException('The incident cannot be resolved until all the tasks are closed on mssportal.')

    except Exception as ex:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute HandleXsoarPortalMirroring. Error: {str(ex)}')


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
