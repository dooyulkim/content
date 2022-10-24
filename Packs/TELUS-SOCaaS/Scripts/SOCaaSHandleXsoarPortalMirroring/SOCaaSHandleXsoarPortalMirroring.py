import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401


def main():
    try:
        args = demisto.args()
        xdr_status = args.get('new')
        print(xdr_status)
        id = demisto.context()["MSSPortal"]["Case"]["id"]
        case = demisto.executeCommand("mssportal-get-case", {'id': id})
        if(case.nbTelusPendingTasks == 0 and case.nbCustomerClosedTasks == case.nbCustomerTasks):
            demisto.executeCommand("mssportal-resolve-case", {'id': id})
        else:
            raise DemistoException('The incident cannot be resolved until all the tasks are closed on mssportal.')
    except Exception as ex:
        demisto.error(traceback.format_exc())  # print the traceback
       # return_error(f'Failed to execute HandleXsoarPortalMirroring. Error: {res}')


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
