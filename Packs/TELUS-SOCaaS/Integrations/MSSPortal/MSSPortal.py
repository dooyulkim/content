import demistomock as demisto
from CommonServerPython import *


class Client(BaseClient):
    def __init__(self, server_url, verify, proxy, headers, auth):
        # print(server_url)
        super().__init__(base_url=server_url, verify=verify,
                         proxy=proxy, headers=headers, auth=auth)

    def acknowledge_case_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'put', f'v1/cases/{id_}/acknowledgement', headers=headers)

        return response

    def acknowledge_comment_on_task_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'put', f'v1/tasks/comments/{id_}/acknowledgement', headers=headers)

        return response

    def acknowledge_task_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'put', f'v1/tasks/{id_}/acknowledgement', headers=headers)

        return response

    def activate_playbook_request(self, activateplaybookrequest_caseid, activateplaybookrequest_playbookid, activateplaybookrequest_excludedtaskids):
        data = assign_params(caseId=activateplaybookrequest_caseid, playbookId=activateplaybookrequest_playbookid,
                             excludedTaskIds=activateplaybookrequest_excludedtaskids)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/tasks/from-playbook', json_data=data, headers=headers)

        return response

    def activate_playbook_1_request(self, id_, playbookId, body):
        data = assign_params(body=body)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/cases/{id_}/playbooks/{playbookId}', json_data=data, headers=headers)

        return response

    def add_linked_cases_request(self, id_, body):
        data = assign_params(body=body)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/cases/{id_}/linked-cases', json_data=data, headers=headers)

        return response

    def add_linked_threat_request(self, id_, threatId):
        headers = self._headers

        response = self._http_request(
            'put', f'v1/cases/{id_}/linked-threats/{threatId}', headers=headers)

        return response

    def add_threat_comment_request(self, id_, threatcommentcreation_commenttexthtml):
        data = assign_params(
            commentTextHtml=threatcommentcreation_commenttexthtml)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/threats/{id_}/comments', json_data=data, headers=headers)

        return response

    def confirm_case_incident_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'put', f'v1/cases/{id_}/incid_ent', headers=headers)

        return response

    def create_alert_request(self, alertcreation_sourceid, alertcreation_sourcecreatedat, alertcreation_sourcemodifiedat, alertcreation_sourcealertid, alertcreation_sourceraw, alertcreation_severity, alertcreation_customerid, alertcreation_investigationcaseid, alertcreation_name, alertcreation_casedescription, alertcreation_casetitle, alertcreation_detailhtml, alertcreation_providerid, alertcreation_providercreatedat, alertcreation_providermodifiedat, alertcreation_provideralertid, alertcreation_providerraw):
        data = assign_params(sourceId=alertcreation_sourceid, sourceCreatedAt=alertcreation_sourcecreatedat, sourceModifiedAt=alertcreation_sourcemodifiedat, sourceAlertId=alertcreation_sourcealertid, sourceRaw=alertcreation_sourceraw, severity=alertcreation_severity, customerId=alertcreation_customerid, investigationCaseId=alertcreation_investigationcaseid,
                             name=alertcreation_name, caseDescription=alertcreation_casedescription, caseTitle=alertcreation_casetitle, detailHtml=alertcreation_detailhtml, providerId=alertcreation_providerid, providerCreatedAt=alertcreation_providercreatedat, providerModifiedAt=alertcreation_providermodifiedat, providerAlertId=alertcreation_provideralertid, providerRaw=alertcreation_providerraw)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/alerts', json_data=data, headers=headers)

        return response

    def create_case_request(self, casecreation_status, casecreation_telusprime, casecreation_description, casecreation_casetitle, casecreation_priority, casecreation_resolutionnotes, casecreation_customerid, casecreation_casesource, casecreation_alertname, casecreation_servicecomponent):
        data = assign_params(status=casecreation_status, telusPrime=casecreation_telusprime, description=casecreation_description, caseTitle=casecreation_casetitle, priority=casecreation_priority,
                             resolutionNotes=casecreation_resolutionnotes, customerId=casecreation_customerid, caseSource=casecreation_casesource, alertName=casecreation_alertname, serviceComponent=casecreation_servicecomponent)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/cases', json_data=data, headers=headers)

        return response

    def create_comment_on_case_request(self, id_, casecommentcreation_commenttexthtml):
        data = assign_params(
            commentTextHtml=casecommentcreation_commenttexthtml)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/cases/{id_}/comments', json_data=data, headers=headers)

        return response

    def create_comment_on_task_request(self, taskcommentcreation_taskid, taskcommentcreation_commenttexthtml, taskcommentcreation_authorship):
        data = assign_params(taskId=taskcommentcreation_taskid,
                             commentTextHtml=taskcommentcreation_commenttexthtml, authorship=taskcommentcreation_authorship)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/tasks/{id_}/comments', json_data=data, headers=headers)

        return response

    def create_customer_request(self, customercreation_id, customercreation_caseretentionperiodmonths):
        data = assign_params(
            id=customercreation_id, caseRetentionPeriodMonths=customercreation_caseretentionperiodmonths)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/customers', json_data=data, headers=headers)

        return response

    def create_identity_request(self, identitycreation_id, identitycreation_key, identitycreation_grantedbehalfuserpattern, identitycreation_ratelimitconfiguration, identitycreation_permissions):
        data = assign_params(id=identitycreation_id, key=identitycreation_key, grantedBehalfUserPattern=identitycreation_grantedbehalfuserpattern,
                             rateLimitConfiguration=identitycreation_ratelimitconfiguration, permissions=identitycreation_permissions)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/identities', json_data=data, headers=headers)

        return response

    def create_playbook_request(self, playbookcreation_name, playbookcreation_description):
        data = assign_params(name=playbookcreation_name,
                             description=playbookcreation_description)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/playbooks', json_data=data, headers=headers)

        return response

    def create_playbook_task_request(self, playbookId, playbooktaskcreation_name, playbooktaskcreation_description, playbooktaskcreation_accountable, playbooktaskcreation_priority, playbooktaskcreation_phase, playbooktaskcreation_duedateperiod):
        data = assign_params(name=playbooktaskcreation_name, description=playbooktaskcreation_description, accountable=playbooktaskcreation_accountable,
                             priority=playbooktaskcreation_priority, phase=playbooktaskcreation_phase, dueDatePeriod=playbooktaskcreation_duedateperiod)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/playbooks/{playbookId}/tasks', json_data=data, headers=headers)

        return response

    def create_task_request(self, taskcreation_name, taskcreation_description, taskcreation_caseid, taskcreation_accountable, taskcreation_telusprime, taskcreation_priority, taskcreation_phase, taskcreation_status, taskcreation_duedate, taskcreation_abouttoexpirethresholdindays, taskcreation_modifiedbytelus):
        data = assign_params(name=taskcreation_name, description=taskcreation_description, caseId=taskcreation_caseid, accountable=taskcreation_accountable, telusPrime=taskcreation_telusprime, priority=taskcreation_priority,
                             phase=taskcreation_phase, status=taskcreation_status, dueDate=taskcreation_duedate, aboutToExpireThresholdInDays=taskcreation_abouttoexpirethresholdindays, modifiedByTelus=taskcreation_modifiedbytelus)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/tasks', json_data=data, headers=headers)

        return response

    def create_threat_request(self, threatcreation_description, threatcreation_actor, threatcreation_detailhtml):
        data = assign_params(description=threatcreation_description,
                             actor=threatcreation_actor, detailHtml=threatcreation_detailhtml)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/threats', json_data=data, headers=headers)

        return response

    def create_webhook_request(self, webhookcreation_url, webhookcreation_authenticationheadername, webhookcreation_authenticationheadervalue, webhookcreation_eventtypes):
        data = assign_params(url=webhookcreation_url, authenticationHeaderName=webhookcreation_authenticationheadername,
                             authenticationHeaderValue=webhookcreation_authenticationheadervalue, eventTypes=webhookcreation_eventtypes)
        headers = self._headers

        response = self._http_request(
            'post', 'v1/webhooks', json_data=data, headers=headers)

        return response

    def delete_customer_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/customers/{id_}', headers=headers)

        return response

    def delete_identity_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/id_entities/{id_}', headers=headers)

        return response

    def delete_playbook_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/playbooks/{id_}', headers=headers)

        return response

    def delete_playbook_task_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/playbooks/tasks/{id_}', headers=headers)

        return response

    def delete_task_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/tasks/{id_}', headers=headers)

        return response

    def delete_threat_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/threats/{id_}', headers=headers)

        return response

    def delete_webhook_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/webhooks/{id_}', headers=headers)

        return response

    def download_case_attachment_request(self, id_, name, forceDownload):
        params = assign_params(forceDownload=forceDownload)
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/{id_}/attachments/{name}', params=params, headers=headers)

        return response

    def download_task_attachment_request(self, id_, name, forceDownload):
        params = assign_params(forceDownload=forceDownload)
        headers = self._headers

        response = self._http_request(
            'get', f'v1/tasks/{id_}/attachments/{name}', params=params, headers=headers)

        return response

    def download_threat_attachment_request(self, id_, name, forceDownload):
        params = assign_params(forceDownload=forceDownload)
        headers = self._headers

        response = self._http_request(
            'get', f'v1/threats/{id_}/attachments/{name}', params=params, headers=headers)

        return response

    def find_alert_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/alerts/{id_}', headers=headers)

        return response

    def find_alerts_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/{id_}/alerts', headers=headers)

        return response

    def find_alerts_1_request(self, id_, severity, customerId, sourceCreatedAt_from, sourceCreatedAt_to, sourceModifiedAt_from, sourceModifiedAt_to, investigationCaseId, sort, offset, limit):
        params = assign_params(id=id_, severity=severity, customerId=customerId, sourceCreatedAt_from=sourceCreatedAt_from, sourceCreatedAt_to=sourceCreatedAt_to,
                               sourceModifiedAt_from=sourceModifiedAt_from, sourceModifiedAt_to=sourceModifiedAt_to, investigationCaseId=investigationCaseId, sort=sort, offset=offset, limit=limit)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/alerts', params=params, headers=headers)

        return response

    def find_case_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/{id_}', headers=headers)

        return response

    def find_case_attachment_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/attachments/{id_}', headers=headers)

        return response

    def find_case_attachments_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/{id_}/attachments', headers=headers)

        return response

    def find_case_sources_by_customer_id_request(self, customerId):
        params = assign_params(customerId=customerId)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/cases/sources', params=params, headers=headers)

        return response

    def find_cases_request(self, id_, serviceComponent, priority, status, telusPrime, incident, createdAt_from, createdAt_to, customerId, alertId, caseSource, searchText, resolvedAt_from, resolvedAt_to, resolvedBy, threatId, sort, offset, limit):
        params = assign_params(id=id_, serviceComponent=serviceComponent, priority=priority, status=status, telusPrime=telusPrime, incident=incident, createdAt_from=createdAt_from, createdAt_to=createdAt_to, customerId=customerId,
                               alertId=alertId, caseSource=caseSource, searchText=searchText, resolvedAt_from=resolvedAt_from, resolvedAt_to=resolvedAt_to, resolvedBy=resolvedBy, threatId=threatId, sort=sort, offset=offset, limit=limit)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/cases', params=params, headers=headers)

        return response

    def find_comments_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/{id_}/comments', headers=headers)

        return response

    def find_count_of_unread_comments_by_case_id_and_accountable_request(self, caseId, accountable):
        params = assign_params(caseId=caseId, accountable=accountable)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/tasks/comments/countUnread', params=params, headers=headers)

        return response

    def find_customers_request(self):
        headers = self._headers

        response = self._http_request('get', 'v1/customers', headers=headers)

        return response

    def find_linked_cases_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/{id_}/linked-cases', headers=headers)

        return response

    def find_linked_threats_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/cases/{id_}/linked-threats', headers=headers)

        return response

    def find_playbook_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/playbooks/{id_}', headers=headers)

        return response

    def find_playbook_task_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/playbooks/tasks/{id_}', headers=headers)

        return response

    def find_playbook_tasks_request(self, playbookId, playbooktaskcriteria_sort, playbooktaskcriteria_id, playbooktaskcriteria_createdat, playbooktaskcriteria_updatedat, playbooktaskcriteria_playbookid, playbooktaskcriteria_searchtext, offset, limit):
        params = assign_params(sort=playbooktaskcriteria_sort, id=playbooktaskcriteria_id, createdAt=playbooktaskcriteria_createdat,
                               updatedAt=playbooktaskcriteria_updatedat, playbookId=playbooktaskcriteria_playbookid, searchText=playbooktaskcriteria_searchtext, offset=offset, limit=limit)
        headers = self._headers

        response = self._http_request(
            'get', f'v1/playbooks/{playbookId}/tasks', params=params, headers=headers)

        return response

    def find_playbooks_request(self, id_, createdAt_from, createdAt_to, updatedAt_from, updatedAt_to, searchText, sort, offset, limit):
        params = assign_params(id=id_, createdAt_from=createdAt_from, createdAt_to=createdAt_to, updatedAt_from=updatedAt_from,
                               updatedAt_to=updatedAt_to, searchText=searchText, sort=sort, offset=offset, limit=limit)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/playbooks', params=params, headers=headers)

        return response

    def find_task_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/tasks/{id_}', headers=headers)

        return response

    def find_task_attachment_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/tasks/attachments/{id_}', headers=headers)

        return response

    def find_task_attachments_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/tasks/{id_}/attachments', headers=headers)

        return response

    def find_task_comment_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/tasks/comments/{id_}', headers=headers)

        return response

    def find_task_count_request(self, id_, name, description, caseId, accountable, phase, priority, status, telusPrime, createdAt_from, createdAt_to, dueDate, customerId, caseTitle, searchText, resolvedAt_from, resolvedAt_to, resolvedBy, sort):
        params = assign_params(id=id_, name=name, description=description, caseId=caseId, accountable=accountable, phase=phase, priority=priority, status=status, telusPrime=telusPrime, createdAt_from=createdAt_from,
                               createdAt_to=createdAt_to, dueDate=dueDate, customerId=customerId, caseTitle=caseTitle, searchText=searchText, resolvedAt_from=resolvedAt_from, resolvedAt_to=resolvedAt_to, resolvedBy=resolvedBy, sort=sort)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/tasks/count', params=params, headers=headers)

        return response

    def find_tasks_request(self, id_, name, description, caseId, accountable, phase, priority, status, telusPrime, createdAt_from, createdAt_to, dueDate, customerId, caseTitle, searchText, resolvedAt_from, resolvedAt_to, resolvedBy, sort, offset, limit):
        params = assign_params(id=id_, name=name, description=description, caseId=caseId, accountable=accountable, phase=phase, priority=priority, status=status, telusPrime=telusPrime, createdAt_from=createdAt_from, createdAt_to=createdAt_to,
                               dueDate=dueDate, customerId=customerId, caseTitle=caseTitle, searchText=searchText, resolvedAt_from=resolvedAt_from, resolvedAt_to=resolvedAt_to, resolvedBy=resolvedBy, sort=sort, offset=offset, limit=limit)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/tasks', params=params, headers=headers)

        return response

    def find_threat_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/threats/{id_}', headers=headers)

        return response

    def find_threat_attachment_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/threats/attachments/{id_}', headers=headers)

        return response

    def find_threat_attachments_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/threats/{id_}/attachments', headers=headers)

        return response

    def find_threats_request(self, id_, customerId, caseId, createdAt_from, createdAt_to, searchText, sort, offset, limit):
        params = assign_params(id=id_, customerId=customerId, caseId=caseId, createdAt_from=createdAt_from,
                               createdAt_to=createdAt_to, searchText=searchText, sort=sort, offset=offset, limit=limit)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/threats', params=params, headers=headers)

        return response

    def get_current_request(self):
        headers = self._headers

        response = self._http_request(
            'get', 'v1/identities/current', headers=headers)

        return response

    def get_customer_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'get', f'v1/customers/{id_}', headers=headers)

        return response

    def get_identities_request(self):
        headers = self._headers
        
        response = self._http_request('get', 'v1/identities', headers=headers)

        return response

    def get_service_metrics_request(self, casecriteria_sort, casecriteria_id, casecriteria_servicecomponent, casecriteria_priority, casecriteria_status, casecriteria_telusprime, casecriteria_incident, casecriteria_createdat, casecriteria_customerid, casecriteria_alertid, casecriteria_casesource, casecriteria_searchtext, casecriteria_resolvedat, casecriteria_resolvedby, casecriteria_threatid, casecriteria_servicecomponents, casecriteria_casesources, casecriteria_statuses, casecriteria_priorities):
        params = assign_params(sort=casecriteria_sort, id=casecriteria_id, serviceComponent=casecriteria_servicecomponent, priority=casecriteria_priority, status=casecriteria_status, telusPrime=casecriteria_telusprime, incident=casecriteria_incident, createdAt=casecriteria_createdat, customerId=casecriteria_customerid, alertId=casecriteria_alertid,
                               caseSource=casecriteria_casesource, searchText=casecriteria_searchtext, resolvedAt=casecriteria_resolvedat, resolvedBy=casecriteria_resolvedby, threatId=casecriteria_threatid, serviceComponents=casecriteria_servicecomponents, caseSources=casecriteria_casesources, statuses=casecriteria_statuses, priorities=casecriteria_priorities)
        headers = self._headers

        response = self._http_request(
            'get', 'v1/cases/service-metrics', params=params, headers=headers)

        return response

    def get_webhooks_request(self):
        headers = self._headers

        response = self._http_request('get', 'v1/webhooks', headers=headers)

        return response

    def put_current_key_request(self, body):
        data = assign_params(body=body)
        headers = self._headers

        response = self._http_request(
            'put', 'v1/identities/current/key', json_data=data, headers=headers)

        return response

    def put_customer_request(self, id_, customerupdate_caseretentionperiodmonths):
        data = assign_params(
            caseRetentionPeriodMonths=customerupdate_caseretentionperiodmonths)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/customers/{id_}', json_data=data, headers=headers)

        return response

    def put_identity_request(self, id_, identityupdate_grantedbehalfuserpattern, identityupdate_ratelimitconfiguration, identityupdate_permissions):
        data = assign_params(grantedBehalfUserPattern=identityupdate_grantedbehalfuserpattern,
                             rateLimitConfiguration=identityupdate_ratelimitconfiguration, permissions=identityupdate_permissions)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/id_entities/{id_}', json_data=data, headers=headers)

        return response

    def put_webhook_request(self, id_, webhookupdate_url, webhookupdate_authenticationheadername, webhookupdate_authenticationheadervalue, webhookupdate_eventtypes):
        data = assign_params(url=webhookupdate_url, authenticationHeaderName=webhookupdate_authenticationheadername,
                             authenticationHeaderValue=webhookupdate_authenticationheadervalue, eventTypes=webhookupdate_eventtypes)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/webhooks/{id_}', json_data=data, headers=headers)

        return response

    def remove_case_attachment_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/cases/attachments/{id_}', headers=headers)

        return response

    def remove_linked_case_request(self, id_, linkedCaseId):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/cases/{id_}/linked-cases/{linkedCaseId}', headers=headers)

        return response

    def remove_linked_threat_request(self, id_, threatId):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/cases/{id_}/linked-threats/{threatId}', headers=headers)

        return response

    def remove_task_attachment_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/tasks/attachments/{id_}', headers=headers)

        return response

    def remove_threat_attachment_request(self, id_):
        headers = self._headers

        response = self._http_request(
            'delete', f'v1/threats/attachments/{id_}', headers=headers)

        return response

    def resolve_case_request(self, id_, caseresolution_resolutionnotes):
        data = assign_params(resolutionNotes=caseresolution_resolutionnotes)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/cases/{id_}/resolution', json_data=data, headers=headers)

        return response

    def update_case_request(self, id_, caseupdate_status, caseupdate_telusprime, caseupdate_description, caseupdate_casetitle, caseupdate_priority, caseupdate_resolutionnotes):
        data = assign_params(status=caseupdate_status, telusPrime=caseupdate_telusprime, description=caseupdate_description,
                             caseTitle=caseupdate_casetitle, priority=caseupdate_priority, resolutionNotes=caseupdate_resolutionnotes)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/cases/{id_}', json_data=data, headers=headers)

        return response

    def update_comment_on_task_request(self, id_, taskcommentinfo_id, taskcommentinfo_createdat, taskcommentinfo_createdby, taskcommentinfo_updatedat, taskcommentinfo_updatedby, taskcommentinfo_commenttexthtml, taskcommentinfo_authorship, taskcommentinfo_acknowledged, taskcommentinfo_acknowledgedat, taskcommentinfo_acknowledgedby, taskcommentinfo_readat):
        data = assign_params(id=taskcommentinfo_id, createdAt=taskcommentinfo_createdat, createdBy=taskcommentinfo_createdby, updatedAt=taskcommentinfo_updatedat, updatedBy=taskcommentinfo_updatedby, commentTextHtml=taskcommentinfo_commenttexthtml,
                             authorship=taskcommentinfo_authorship, acknowledged=taskcommentinfo_acknowledged, acknowledgedAt=taskcommentinfo_acknowledgedat, acknowledgedBy=taskcommentinfo_acknowledgedby, readAt=taskcommentinfo_readat)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/tasks/comments/{id_}', json_data=data, headers=headers)

        return response

    def update_comment_on_task_1_request(self, id_, casecommentinfo_id, casecommentinfo_createdat, casecommentinfo_createdby, casecommentinfo_updatedat, casecommentinfo_updatedby, casecommentinfo_commenttexthtml):
        data = assign_params(id=casecommentinfo_id, createdAt=casecommentinfo_createdat, createdBy=casecommentinfo_createdby,
                             updatedAt=casecommentinfo_updatedat, updatedBy=casecommentinfo_updatedby, commentTextHtml=casecommentinfo_commenttexthtml)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/cases/comments/{id_}', json_data=data, headers=headers)

        return response

    def update_playbook_request(self, id_, playbookupdate_name, playbookupdate_description):
        data = assign_params(name=playbookupdate_name,
                             description=playbookupdate_description)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/playbooks/{id_}', json_data=data, headers=headers)

        return response

    def update_playbook_task_request(self, id_, playbooktaskupdate_name, playbooktaskupdate_description, playbooktaskupdate_accountable, playbooktaskupdate_priority, playbooktaskupdate_phase, playbooktaskupdate_duedateperiod):
        data = assign_params(name=playbooktaskupdate_name, description=playbooktaskupdate_description, accountable=playbooktaskupdate_accountable,
                             priority=playbooktaskupdate_priority, phase=playbooktaskupdate_phase, dueDatePeriod=playbooktaskupdate_duedateperiod)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/playbooks/tasks/{id_}', json_data=data, headers=headers)

        return response

    def update_read_flag_for_comment_on_task_request(self, id_, body):
        data = assign_params(body=body)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/tasks/comments/{id_}/read-flag', json_data=data, headers=headers)

        return response

    def update_task_request(self, id_, taskupdate_status, taskupdate_telusprime, taskupdate_name, taskupdate_description, taskupdate_priority, taskupdate_modifiedbytelus, taskupdate_duedate):
        data = assign_params(status=taskupdate_status, telusPrime=taskupdate_telusprime, name=taskupdate_name, description=taskupdate_description,
                             priority=taskupdate_priority, modifiedByTelus=taskupdate_modifiedbytelus, dueDate=taskupdate_duedate)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/tasks/{id_}', json_data=data, headers=headers)

        return response

    def update_threat_request(self, id_, threatupdate_description, threatupdate_actor, threatupdate_detailhtml):
        data = assign_params(description=threatupdate_description,
                             actor=threatupdate_actor, detailHtml=threatupdate_detailhtml)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/threats/{id_}', json_data=data, headers=headers)

        return response

    def update_threat_comment_request(self, id_, threatcommentupdate_commenttexthtml):
        data = assign_params(
            commentTextHtml=threatcommentupdate_commenttexthtml)
        headers = self._headers

        response = self._http_request(
            'put', f'v1/threats/comments/{id_}', json_data=data, headers=headers)

        return response

    def upload_case_attachment_request(self, id_, body):
        data = assign_params(body=body)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/cases/{id_}/attachments', json_data=data, headers=headers)

        return response

    def upload_task_attachment_request(self, id_, body):
        data = assign_params(body=body)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/tasks/{id_}/attachments', json_data=data, headers=headers)

        return response

    def upload_threat_attachment_request(self, id_, body):
        data = assign_params(body=body)
        headers = self._headers

        response = self._http_request(
            'post', f'v1/threats/{id_}/attachments', json_data=data, headers=headers)

        return response


def acknowledge_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.acknowledge_case_request(id_)
    command_results = CommandResults(
        readable_output=f'MSSPortal Case {id_} acknowledged',
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def acknowledge_comment_on_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.acknowledge_comment_on_task_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def acknowledge_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.acknowledge_task_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def activate_playbook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    activateplaybookrequest_caseid = args.get(
        'activateplaybookrequest_caseid', None)
    activateplaybookrequest_playbookid = args.get(
        'activateplaybookrequest_playbookid', None)
    activateplaybookrequest_excludedtaskids = argToList(
        args.get('activateplaybookrequest_excludedtaskids', []))

    response = client.activate_playbook_request(
        activateplaybookrequest_caseid, activateplaybookrequest_playbookid, activateplaybookrequest_excludedtaskids)
    command_results = CommandResults(
        readable_output=f'MSSPortal playbook {activateplaybookrequest_playbookid} was activated in the case {activateplaybookrequest_caseid}',
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def activate_playbook_1_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    playbookId = args.get('playbookId', None)
    body = argToList(args.get('body', []))

    response = client.activate_playbook_1_request(id_, playbookId, body)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def add_linked_cases_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    body = argToList(args.get('body', []))

    response = client.add_linked_cases_request(id_, body)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def add_linked_threat_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    threatId = args.get('threatId', None)

    response = client.add_linked_threat_request(id_, threatId)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def add_threat_comment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    threatcommentcreation_commenttexthtml = str(
        args.get('threatcommentcreation_commenttexthtml', ''))

    response = client.add_threat_comment_request(
        id_, threatcommentcreation_commenttexthtml)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def confirm_case_incident_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.confirm_case_incident_request(id_)
    command_results = CommandResults(
        readable_output=f'MSSPortal Case {id_} confirmed as a true incident',
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_alert_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    alertcreation_sourceid = str(args.get('alertcreation_sourceid', ''))
    alertcreation_sourcecreatedat = str(
        args.get('alertcreation_sourcecreatedat', ''))
    alertcreation_sourcemodifiedat = str(
        args.get('alertcreation_sourcemodifiedat', ''))
    alertcreation_sourcealertid = str(
        args.get('alertcreation_sourcealertid', ''))
    alertcreation_sourceraw = str(args.get('alertcreation_sourceraw', ''))
    alertcreation_severity = str(args.get('alertcreation_severity', ''))
    alertcreation_customerid = args.get('alertcreation_customerid', None)
    alertcreation_investigationcaseid = args.get(
        'alertcreation_investigationcaseid', None)
    alertcreation_name = str(args.get('alertcreation_name', ''))
    alertcreation_casedescription = str(
        args.get('alertcreation_casedescription', ''))
    alertcreation_casetitle = str(args.get('alertcreation_casetitle', ''))
    alertcreation_detailhtml = str(args.get('alertcreation_detailhtml', ''))
    alertcreation_providerid = str(args.get('alertcreation_providerid', ''))
    alertcreation_providercreatedat = str(
        args.get('alertcreation_providercreatedat', ''))
    alertcreation_providermodifiedat = str(
        args.get('alertcreation_providermodifiedat', ''))
    alertcreation_provideralertid = str(
        args.get('alertcreation_provideralertid', ''))
    alertcreation_providerraw = str(args.get('alertcreation_providerraw', ''))

    response = client.create_alert_request(alertcreation_sourceid, alertcreation_sourcecreatedat, alertcreation_sourcemodifiedat, alertcreation_sourcealertid, alertcreation_sourceraw, alertcreation_severity, alertcreation_customerid, alertcreation_investigationcaseid,
                                           alertcreation_name, alertcreation_casedescription, alertcreation_casetitle, alertcreation_detailhtml, alertcreation_providerid, alertcreation_providercreatedat, alertcreation_providermodifiedat, alertcreation_provideralertid, alertcreation_providerraw)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.AlertInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    casecreation_status = str(args.get('casecreation_status', ''))
    casecreation_telusprime = str(args.get('casecreation_telusprime', ''))
    casecreation_description = str(args.get('casecreation_description', ''))
    casecreation_casetitle = str(args.get('casecreation_casetitle', ''))
    casecreation_priority = str(args.get('casecreation_priority', ''))
    casecreation_resolutionnotes = str(
        args.get('casecreation_resolutionnotes', ''))
    casecreation_customerid = args.get('casecreation_customerid', None)
    casecreation_casesource = str(args.get('casecreation_casesource', ''))
    casecreation_alertname = str(args.get('casecreation_alertname', ''))
    casecreation_servicecomponent = str(
        args.get('casecreation_servicecomponent', ''))

    response = client.create_case_request(casecreation_status, casecreation_telusprime, casecreation_description, casecreation_casetitle, casecreation_priority,
                                          casecreation_resolutionnotes, casecreation_customerid, casecreation_casesource, casecreation_alertname, casecreation_servicecomponent)
    command_results = CommandResults(
        readable_output=tableToMarkdown(f'MSSPortal Case {response["id"]}', response),
        outputs_prefix='MSSPortal.CaseInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_comment_on_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    casecommentcreation_commenttexthtml = str(
        args.get('casecommentcreation_commenttexthtml', ''))

    response = client.create_comment_on_case_request(
        id_, casecommentcreation_commenttexthtml)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_comment_on_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    taskcommentcreation_taskid = args.get('taskcommentcreation_taskid', None)
    taskcommentcreation_commenttexthtml = str(
        args.get('taskcommentcreation_commenttexthtml', ''))
    taskcommentcreation_authorship = str(
        args.get('taskcommentcreation_authorship', ''))

    response = client.create_comment_on_task_request(
        taskcommentcreation_taskid, taskcommentcreation_commenttexthtml, taskcommentcreation_authorship)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_customer_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    customercreation_id = args.get('customercreation_id', None)
    customercreation_caseretentionperiodmonths = args.get(
        'customercreation_caseretentionperiodmonths', None)

    response = client.create_customer_request(
        customercreation_id, customercreation_caseretentionperiodmonths)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.CustomerInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_identity_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    identitycreation_id = str(args.get('identitycreation_id', ''))
    identitycreation_key = str(args.get('identitycreation_key', ''))
    identitycreation_grantedbehalfuserpattern = str(
        args.get('identitycreation_grantedbehalfuserpattern', ''))
    identitycreation_ratelimitconfiguration = str(
        args.get('identitycreation_ratelimitconfiguration', ''))
    identitycreation_permissions = argToList(
        args.get('identitycreation_permissions', []))

    response = client.create_identity_request(identitycreation_id, identitycreation_key,
                                              identitycreation_grantedbehalfuserpattern, identitycreation_ratelimitconfiguration, identitycreation_permissions)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.IdentityInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_playbook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    playbookcreation_name = str(args.get('playbookcreation_name', ''))
    playbookcreation_description = str(
        args.get('playbookcreation_description', ''))

    response = client.create_playbook_request(
        playbookcreation_name, playbookcreation_description)
    command_results = CommandResults(
        readable_output=tableToMarkdown('MSSPortal Playbook', response),
        outputs_prefix='MSSPortal.PlaybookInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_playbook_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    playbookId = args.get('playbookId', None)
    playbooktaskcreation_name = str(args.get('playbooktaskcreation_name', ''))
    playbooktaskcreation_description = str(
        args.get('playbooktaskcreation_description', ''))
    playbooktaskcreation_accountable = str(
        args.get('playbooktaskcreation_accountable', ''))
    playbooktaskcreation_priority = str(
        args.get('playbooktaskcreation_priority', ''))
    playbooktaskcreation_phase = str(
        args.get('playbooktaskcreation_phase', ''))
    playbooktaskcreation_duedateperiod = args.get(
        'playbooktaskcreation_duedateperiod', None)

    response = client.create_playbook_task_request(playbookId, playbooktaskcreation_name, playbooktaskcreation_description,
                                                   playbooktaskcreation_accountable, playbooktaskcreation_priority, playbooktaskcreation_phase, playbooktaskcreation_duedateperiod)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.PlaybookTaskInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    taskcreation_name = str(args.get('taskcreation_name', ''))
    taskcreation_description = str(args.get('taskcreation_description', ''))
    taskcreation_caseid = args.get('taskcreation_caseid', None)
    taskcreation_accountable = str(args.get('taskcreation_accountable', ''))
    taskcreation_telusprime = str(args.get('taskcreation_telusprime', ''))
    taskcreation_priority = str(args.get('taskcreation_priority', ''))
    taskcreation_phase = str(args.get('taskcreation_phase', ''))
    taskcreation_status = str(args.get('taskcreation_status', ''))
    taskcreation_duedate = str(args.get('taskcreation_duedate', ''))
    taskcreation_abouttoexpirethresholdindays = args.get(
        'taskcreation_abouttoexpirethresholdindays', None)
    taskcreation_modifiedbytelus = argToBoolean(
        args.get('taskcreation_modifiedbytelus', False))

    response = client.create_task_request(taskcreation_name, taskcreation_description, taskcreation_caseid, taskcreation_accountable, taskcreation_telusprime,
                                          taskcreation_priority, taskcreation_phase, taskcreation_status, taskcreation_duedate, taskcreation_abouttoexpirethresholdindays, taskcreation_modifiedbytelus)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.TaskInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_threat_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    threatcreation_description = str(
        args.get('threatcreation_description', ''))
    threatcreation_actor = str(args.get('threatcreation_actor', ''))
    threatcreation_detailhtml = str(args.get('threatcreation_detailhtml', ''))

    response = client.create_threat_request(
        threatcreation_description, threatcreation_actor, threatcreation_detailhtml)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.ThreatInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def create_webhook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    webhookcreation_url = str(args.get('webhookcreation_url', ''))
    webhookcreation_authenticationheadername = str(
        args.get('webhookcreation_authenticationheadername', ''))
    webhookcreation_authenticationheadervalue = str(
        args.get('webhookcreation_authenticationheadervalue', ''))
    webhookcreation_eventtypes = argToList(
        args.get('webhookcreation_eventtypes', []))

    response = client.create_webhook_request(webhookcreation_url, webhookcreation_authenticationheadername,
                                             webhookcreation_authenticationheadervalue, webhookcreation_eventtypes)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.WebhookInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def delete_customer_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.delete_customer_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def delete_identity_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = str(args.get('id_', ''))

    response = client.delete_identity_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def delete_playbook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.delete_playbook_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def delete_playbook_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.delete_playbook_task_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def delete_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.delete_task_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def delete_threat_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.delete_threat_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def delete_webhook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.delete_webhook_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def download_case_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    name = str(args.get('name', ''))
    forceDownload = argToBoolean(args.get('forceDownload', False))

    response = client.download_case_attachment_request(
        id_, name, forceDownload)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def download_task_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    name = str(args.get('name', ''))
    forceDownload = argToBoolean(args.get('forceDownload', False))

    response = client.download_task_attachment_request(
        id_, name, forceDownload)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def download_threat_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    name = str(args.get('name', ''))
    forceDownload = argToBoolean(args.get('forceDownload', False))

    response = client.download_threat_attachment_request(
        id_, name, forceDownload)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_alert_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_alert_request(id_)

    command_results = CommandResults(
        readable_output=tableToMarkdown(f'MSSPortal Alert {id_}', response),
        outputs_prefix='MSSPortal.AlertInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_alerts_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_alerts_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.AlertInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_alerts_1_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    severity = str(args.get('severity', ''))
    customerId = args.get('customerId', None)
    sourceCreatedAt_from = str(args.get('sourceCreatedAt_from', ''))
    sourceCreatedAt_to = str(args.get('sourceCreatedAt_to', ''))
    sourceModifiedAt_from = str(args.get('sourceModifiedAt_from', ''))
    sourceModifiedAt_to = str(args.get('sourceModifiedAt_to', ''))
    investigationCaseId = args.get('investigationCaseId', None)
    sort = str(args.get('sort', ''))
    offset = args.get('offset', None)
    limit = args.get('limit', None)

    response = client.find_alerts_1_request(id_, severity, customerId, sourceCreatedAt_from, sourceCreatedAt_to,
                                            sourceModifiedAt_from, sourceModifiedAt_to, investigationCaseId, sort, offset, limit)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.PageAlertInfo',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_case_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.CaseInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_case_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_case_attachment_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.BaseAttachmentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_case_attachments_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_case_attachments_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.BaseAttachmentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_case_sources_by_customer_id_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    customerId = args.get('customerId', None)

    response = client.find_case_sources_by_customer_id_request(customerId)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_cases_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    serviceComponent = str(args.get('serviceComponent', ''))
    priority = str(args.get('priority', ''))
    status = str(args.get('status', ''))
    telusPrime = str(args.get('telusPrime', ''))
    incident = argToBoolean(args.get('incident', False))
    createdAt_from = str(args.get('createdAt_from', ''))
    createdAt_to = str(args.get('createdAt_to', ''))
    customerId = args.get('customerId', None)
    alertId = args.get('alertId', None)
    caseSource = argToList(args.get('caseSource', []))
    searchText = str(args.get('searchText', ''))
    resolvedAt_from = str(args.get('resolvedAt_from', ''))
    resolvedAt_to = str(args.get('resolvedAt_to', ''))
    resolvedBy = str(args.get('resolvedBy', ''))
    threatId = args.get('threatId', None)
    sort = str(args.get('sort', ''))
    offset = args.get('offset', None)
    limit = args.get('limit', None)

    response = client.find_cases_request(id_, serviceComponent, priority, status, telusPrime, incident, createdAt_from, createdAt_to,
                                         customerId, alertId, caseSource, searchText, resolvedAt_from, resolvedAt_to, resolvedBy, threatId, sort, offset, limit)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.PageCaseInfo',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_comments_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_comments_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.CaseCommentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_count_of_unread_comments_by_case_id_and_accountable_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    caseId = args.get('caseId', None)
    accountable = str(args.get('accountable', ''))

    response = client.find_count_of_unread_comments_by_case_id_and_accountable_request(
        caseId, accountable)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_customers_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.find_customers_request()
    command_results = CommandResults(
        outputs_prefix='MSSPortal.CustomerInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_linked_cases_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_linked_cases_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.LinkedCase',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_linked_threats_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_linked_threats_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.ThreatInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_playbook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_playbook_request(id_)
    command_results = CommandResults(
        readable_output=tableToMarkdown('MSSPortal Playbooks found', response),
        outputs_prefix='MSSPortal.PlaybookInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_playbook_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_playbook_task_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.PlaybookTaskInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_playbook_tasks_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    playbookId = args.get('playbookId', None)
    playbooktaskcriteria_sort = str(args.get('playbooktaskcriteria_sort', ''))
    playbooktaskcriteria_id = str(args.get('playbooktaskcriteria_id', ''))
    playbooktaskcriteria_createdat_from = str(
        args.get('playbooktaskcriteria_createdat_from', ''))
    playbooktaskcriteria_createdat_to = str(
        args.get('playbooktaskcriteria_createdat_to', ''))
    playbooktaskcriteria_createdat = assign_params(playbooktaskcriteria_createdat_from, playbooktaskcriteria_createdat_to)
    playbooktaskcriteria_updatedat_from = str(
        args.get('playbooktaskcriteria_updatedat_from', ''))
    playbooktaskcriteria_updatedat_to = str(
        args.get('playbooktaskcriteria_updatedat_to', ''))
    playbooktaskcriteria_updatedat = assign_params(playbooktaskcriteria_updatedat_from, playbooktaskcriteria_updatedat_to)
    playbooktaskcriteria_playbookid = str(
        args.get('playbooktaskcriteria_playbookid', ''))
    playbooktaskcriteria_searchtext = str(
        args.get('playbooktaskcriteria_searchtext', ''))
    offset = args.get('offset', None)
    limit = args.get('limit', None)

    response = client.find_playbook_tasks_request(playbookId, playbooktaskcriteria_sort, playbooktaskcriteria_id, playbooktaskcriteria_createdat,
                                                  playbooktaskcriteria_updatedat, playbooktaskcriteria_playbookid, playbooktaskcriteria_searchtext, offset, limit)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.PagePlaybookTaskInfo',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_playbooks_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    createdAt_from = str(args.get('createdAt_from', ''))
    createdAt_to = str(args.get('createdAt_to', ''))
    updatedAt_from = str(args.get('updatedAt_from', ''))
    updatedAt_to = str(args.get('updatedAt_to', ''))
    searchText = str(args.get('searchText', ''))
    sort = str(args.get('sort', ''))
    offset = args.get('offset', None)
    limit = args.get('limit', None)

    response = client.find_playbooks_request(
        id_, createdAt_from, createdAt_to, updatedAt_from, updatedAt_to, searchText, sort, offset, limit)
    command_results = CommandResults(
        readable_output=tableToMarkdown('MSSPortal Playbooks found', response),
        outputs_prefix='MSSPortal.PagePlaybookInfo',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_task_request(id_)
    command_results = CommandResults(
        readable_output=tableToMarkdown(f'MSSPortal Task {id_}', response),
        outputs_prefix='MSSPortal.TaskInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_task_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_task_attachment_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.BaseAttachmentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_task_attachments_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_task_attachments_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.BaseAttachmentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_task_comment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_task_comment_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.TaskCommentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_task_count_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    name = str(args.get('name', ''))
    description = str(args.get('description', ''))
    caseId = args.get('caseId', None)
    accountable = str(args.get('accountable', ''))
    phase = str(args.get('phase', ''))
    priority = str(args.get('priority', ''))
    status = str(args.get('status', ''))
    telusPrime = str(args.get('telusPrime', ''))
    createdAt_from = str(args.get('createdAt_from', ''))
    createdAt_to = str(args.get('createdAt_to', ''))
    dueDate = str(args.get('dueDate', ''))
    customerId = args.get('customerId', None)
    caseTitle = str(args.get('caseTitle', ''))
    searchText = str(args.get('searchText', ''))
    resolvedAt_from = str(args.get('resolvedAt_from', ''))
    resolvedAt_to = str(args.get('resolvedAt_to', ''))
    resolvedBy = str(args.get('resolvedBy', ''))
    sort = str(args.get('sort', ''))

    response = client.find_task_count_request(id_, name, description, caseId, accountable, phase, priority, status, telusPrime,
                                              createdAt_from, createdAt_to, dueDate, customerId, caseTitle, searchText, resolvedAt_from, resolvedAt_to, resolvedBy, sort)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_tasks_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    name = str(args.get('name', ''))
    description = str(args.get('description', ''))
    caseId = args.get('caseId', None)
    accountable = str(args.get('accountable', ''))
    phase = str(args.get('phase', ''))
    priority = str(args.get('priority', ''))
    status = str(args.get('status', ''))
    telusPrime = str(args.get('telusPrime', ''))
    createdAt_from = str(args.get('createdAt_from', ''))
    createdAt_to = str(args.get('createdAt_to', ''))
    dueDate = str(args.get('dueDate', ''))
    customerId = args.get('customerId', None)
    caseTitle = str(args.get('caseTitle', ''))
    searchText = str(args.get('searchText', ''))
    resolvedAt_from = str(args.get('resolvedAt_from', ''))
    resolvedAt_to = str(args.get('resolvedAt_to', ''))
    resolvedBy = str(args.get('resolvedBy', ''))
    sort = str(args.get('sort', ''))
    offset = args.get('offset', None)
    limit = args.get('limit', None)

    response = client.find_tasks_request(id_, name, description, caseId, accountable, phase, priority, status, telusPrime, createdAt_from,
                                         createdAt_to, dueDate, customerId, caseTitle, searchText, resolvedAt_from, resolvedAt_to, resolvedBy, sort, offset, limit)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.PageTaskInfo',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_threat_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_threat_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.ThreatInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_threat_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_threat_attachment_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.BaseAttachmentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_threat_attachments_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.find_threat_attachments_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.BaseAttachmentInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def find_threats_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    customerId = args.get('customerId', None)
    caseId = args.get('caseId', None)
    createdAt_from = str(args.get('createdAt_from', ''))
    createdAt_to = str(args.get('createdAt_to', ''))
    searchText = str(args.get('searchText', ''))
    sort = str(args.get('sort', ''))
    offset = args.get('offset', None)
    limit = args.get('limit', None)

    response = client.find_threats_request(
        id_, customerId, caseId, createdAt_from, createdAt_to, searchText, sort, offset, limit)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.PageThreatInfo',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def get_current_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.get_current_request()
    command_results = CommandResults(
        outputs_prefix='MSSPortal.IdentityInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def get_customer_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.get_customer_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.CustomerInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def get_identities_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.get_identities_request()
    command_results = CommandResults(
        outputs_prefix='MSSPortal.IdentityInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def get_service_metrics_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    casecriteria_sort = str(args.get('casecriteria_sort', ''))
    casecriteria_id = args.get('casecriteria_id', None)
    casecriteria_servicecomponent = argToList(
        args.get('casecriteria_servicecomponent', []))
    casecriteria_priority = argToList(args.get('casecriteria_priority', []))
    casecriteria_status = argToList(args.get('casecriteria_status', []))
    casecriteria_telusprime = str(args.get('casecriteria_telusprime', ''))
    casecriteria_incident = argToBoolean(
        args.get('casecriteria_incident', False))
    casecriteria_createdat_from = str(
        args.get('casecriteria_createdat_from', ''))
    casecriteria_createdat_to = str(args.get('casecriteria_createdat_to', ''))
    casecriteria_createdat = assign_params(casecriteria_createdat_from, to=casecriteria_createdat_to)
    casecriteria_customerid = args.get('casecriteria_customerid', None)
    casecriteria_alertid = args.get('casecriteria_alertid', None)
    casecriteria_casesource = argToList(
        args.get('casecriteria_casesource', []))
    casecriteria_searchtext = str(args.get('casecriteria_searchtext', ''))
    casecriteria_resolvedat_from = str(
        args.get('casecriteria_resolvedat_from', ''))
    casecriteria_resolvedat_to = str(
        args.get('casecriteria_resolvedat_to', ''))
    casecriteria_resolvedat = assign_params(casecriteria_resolvedat_from, to=casecriteria_resolvedat_to)
    casecriteria_resolvedby = str(args.get('casecriteria_resolvedby', ''))
    casecriteria_threatid = args.get('casecriteria_threatid', None)
    casecriteria_servicecomponents = argToList(
        args.get('casecriteria_servicecomponents', []))
    casecriteria_casesources = argToList(
        args.get('casecriteria_casesources', []))
    casecriteria_statuses = argToList(args.get('casecriteria_statuses', []))
    casecriteria_priorities = argToList(
        args.get('casecriteria_priorities', []))

    response = client.get_service_metrics_request(casecriteria_sort, casecriteria_id, casecriteria_servicecomponent, casecriteria_priority, casecriteria_status, casecriteria_telusprime, casecriteria_incident, casecriteria_createdat, casecriteria_customerid,
                                                  casecriteria_alertid, casecriteria_casesource, casecriteria_searchtext, casecriteria_resolvedat, casecriteria_resolvedby, casecriteria_threatid, casecriteria_servicecomponents, casecriteria_casesources, casecriteria_statuses, casecriteria_priorities)
    command_results = CommandResults(
        outputs_prefix='MSSPortal.CaseServiceMetrics',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def get_webhooks_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.get_webhooks_request()
    command_results = CommandResults(
        outputs_prefix='MSSPortal.WebhookInfo',
        outputs_key_field='id',
        outputs=response,
        raw_response=response
    )

    return command_results


def put_current_key_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    body = str(args.get('body', ''))

    response = client.put_current_key_request(body)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def put_customer_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    customerupdate_caseretentionperiodmonths = args.get(
        'customerupdate_caseretentionperiodmonths', None)

    response = client.put_customer_request(
        id_, customerupdate_caseretentionperiodmonths)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def put_identity_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = str(args.get('id_', ''))
    identityupdate_grantedbehalfuserpattern = str(
        args.get('identityupdate_grantedbehalfuserpattern', ''))
    identityupdate_ratelimitconfiguration = str(
        args.get('identityupdate_ratelimitconfiguration', ''))
    identityupdate_permissions = argToList(
        args.get('identityupdate_permissions', []))

    response = client.put_identity_request(
        id_, identityupdate_grantedbehalfuserpattern, identityupdate_ratelimitconfiguration, identityupdate_permissions)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def put_webhook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    webhookupdate_url = str(args.get('webhookupdate_url', ''))
    webhookupdate_authenticationheadername = str(
        args.get('webhookupdate_authenticationheadername', ''))
    webhookupdate_authenticationheadervalue = str(
        args.get('webhookupdate_authenticationheadervalue', ''))
    webhookupdate_eventtypes = argToList(
        args.get('webhookupdate_eventtypes', []))

    response = client.put_webhook_request(id_, webhookupdate_url, webhookupdate_authenticationheadername,
                                          webhookupdate_authenticationheadervalue, webhookupdate_eventtypes)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def remove_case_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.remove_case_attachment_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def remove_linked_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    linkedCaseId = args.get('linkedCaseId', None)

    response = client.remove_linked_case_request(id_, linkedCaseId)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def remove_linked_threat_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    threatId = args.get('threatId', None)

    response = client.remove_linked_threat_request(id_, threatId)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def remove_task_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.remove_task_attachment_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def remove_threat_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)

    response = client.remove_threat_attachment_request(id_)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def resolve_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    caseresolution_resolutionnotes = str(
        args.get('caseresolution_resolutionnotes', ''))

    response = client.resolve_case_request(id_, caseresolution_resolutionnotes)
    
    command_results = CommandResults(
        readable_output=f'MSSPortal Case {id_} resolved - {caseresolution_resolutionnotes}',
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_case_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    caseupdate_status = str(args.get('caseupdate_status', ''))
    caseupdate_telusprime = str(args.get('caseupdate_telusprime', ''))
    caseupdate_description = str(args.get('caseupdate_description', ''))
    caseupdate_casetitle = str(args.get('caseupdate_casetitle', ''))
    caseupdate_priority = str(args.get('caseupdate_priority', ''))
    caseupdate_resolutionnotes = str(
        args.get('caseupdate_resolutionnotes', ''))

    response = client.update_case_request(id_, caseupdate_status, caseupdate_telusprime,
                                          caseupdate_description, caseupdate_casetitle, caseupdate_priority,
                                          caseupdate_resolutionnotes)
    command_results = CommandResults(
        readable_output=f'MSSPortal Case {id_} updated',
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_comment_on_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    taskcommentinfo_id = args.get('taskcommentinfo_id', None)
    taskcommentinfo_createdat = str(args.get('taskcommentinfo_createdat', ''))
    taskcommentinfo_createdby = str(args.get('taskcommentinfo_createdby', ''))
    taskcommentinfo_updatedat = str(args.get('taskcommentinfo_updatedat', ''))
    taskcommentinfo_updatedby = str(args.get('taskcommentinfo_updatedby', ''))
    taskcommentinfo_commenttexthtml = str(
        args.get('taskcommentinfo_commenttexthtml', ''))
    taskcommentinfo_authorship = str(
        args.get('taskcommentinfo_authorship', ''))
    taskcommentinfo_acknowledged = argToBoolean(
        args.get('taskcommentinfo_acknowledged', False))
    taskcommentinfo_acknowledgedat = str(
        args.get('taskcommentinfo_acknowledgedat', ''))
    taskcommentinfo_acknowledgedby = str(
        args.get('taskcommentinfo_acknowledgedby', ''))
    taskcommentinfo_readat = str(args.get('taskcommentinfo_readat', ''))

    response = client.update_comment_on_task_request(id_, taskcommentinfo_id, taskcommentinfo_createdat, taskcommentinfo_createdby, taskcommentinfo_updatedat, taskcommentinfo_updatedby,
                                                     taskcommentinfo_commenttexthtml, taskcommentinfo_authorship, taskcommentinfo_acknowledged, taskcommentinfo_acknowledgedat, taskcommentinfo_acknowledgedby, taskcommentinfo_readat)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_comment_on_task_1_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    casecommentinfo_id = args.get('casecommentinfo_id', None)
    casecommentinfo_createdat = str(args.get('casecommentinfo_createdat', ''))
    casecommentinfo_createdby = str(args.get('casecommentinfo_createdby', ''))
    casecommentinfo_updatedat = str(args.get('casecommentinfo_updatedat', ''))
    casecommentinfo_updatedby = str(args.get('casecommentinfo_updatedby', ''))
    casecommentinfo_commenttexthtml = str(
        args.get('casecommentinfo_commenttexthtml', ''))

    response = client.update_comment_on_task_1_request(id_, casecommentinfo_id, casecommentinfo_createdat,
                                                       casecommentinfo_createdby, casecommentinfo_updatedat, casecommentinfo_updatedby, casecommentinfo_commenttexthtml)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_playbook_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    playbookupdate_name = str(args.get('playbookupdate_name', ''))
    playbookupdate_description = str(
        args.get('playbookupdate_description', ''))

    response = client.update_playbook_request(
        id_, playbookupdate_name, playbookupdate_description)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_playbook_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    playbooktaskupdate_name = str(args.get('playbooktaskupdate_name', ''))
    playbooktaskupdate_description = str(
        args.get('playbooktaskupdate_description', ''))
    playbooktaskupdate_accountable = str(
        args.get('playbooktaskupdate_accountable', ''))
    playbooktaskupdate_priority = str(
        args.get('playbooktaskupdate_priority', ''))
    playbooktaskupdate_phase = str(args.get('playbooktaskupdate_phase', ''))
    playbooktaskupdate_duedateperiod = args.get(
        'playbooktaskupdate_duedateperiod', None)

    response = client.update_playbook_task_request(id_, playbooktaskupdate_name, playbooktaskupdate_description,
                                                   playbooktaskupdate_accountable, playbooktaskupdate_priority, playbooktaskupdate_phase, playbooktaskupdate_duedateperiod)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_read_flag_for_comment_on_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    body = argToBoolean(args.get('body', False))

    response = client.update_read_flag_for_comment_on_task_request(id_, body)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_task_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    taskupdate_status = str(args.get('taskupdate_status', ''))
    taskupdate_telusprime = str(args.get('taskupdate_telusprime', ''))
    taskupdate_name = str(args.get('taskupdate_name', ''))
    taskupdate_description = str(args.get('taskupdate_description', ''))
    taskupdate_priority = str(args.get('taskupdate_priority', ''))
    taskupdate_modifiedbytelus = argToBoolean(
        args.get('taskupdate_modifiedbytelus', False))
    taskupdate_duedate = str(args.get('taskupdate_duedate', ''))

    response = client.update_task_request(id_, taskupdate_status, taskupdate_telusprime, taskupdate_name,
                                          taskupdate_description, taskupdate_priority, taskupdate_modifiedbytelus, taskupdate_duedate)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_threat_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    threatupdate_description = str(args.get('threatupdate_description', ''))
    threatupdate_actor = str(args.get('threatupdate_actor', ''))
    threatupdate_detailhtml = str(args.get('threatupdate_detailhtml', ''))

    response = client.update_threat_request(
        id_, threatupdate_description, threatupdate_actor, threatupdate_detailhtml)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def update_threat_comment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    threatcommentupdate_commenttexthtml = str(
        args.get('threatcommentupdate_commenttexthtml', ''))

    response = client.update_threat_comment_request(
        id_, threatcommentupdate_commenttexthtml)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def upload_case_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    body = str(args.get('body', ''))

    response = client.upload_case_attachment_request(id_, body)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def upload_task_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    body = str(args.get('body', ''))

    response = client.upload_task_attachment_request(id_, body)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def upload_threat_attachment_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    id_ = args.get('id_', None)
    body = str(args.get('body', ''))

    response = client.upload_threat_attachment_request(id_, body)
    command_results = CommandResults(
        outputs_prefix='MSSPortal',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


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
        client.get_current_request()
    except DemistoException as e:
        if 'Forbidden' in str(e):
            return 'Authorization Error: make sure API Key is correctly set'
        else:
            raise e
    return 'ok'


def main() -> None:

    params: Dict[str, Any] = demisto.params()
    args: Dict[str, Any] = demisto.args()
    url = params.get('url')
    api_key = params.get('api_key')
    verify_certificate: bool = not params.get('insecure', False)
    proxy = params.get('proxy', False)
    headers = {
        'X-Lestrade-Key-ID': 'xsoar',
        'X-Lestrade-Key': api_key
    }

    command = demisto.command()
    demisto.debug(f'Command being called is {command}')

    try:
        requests.packages.urllib3.disable_warnings()
        client: Client = Client(
            urljoin(url, ''), verify_certificate, proxy, headers=headers, auth=None)

        commands = {
            'mssportal-acknowledge-case': acknowledge_case_command,
            'mssportal-acknowledge-comment-on-task': acknowledge_comment_on_task_command,
            'mssportal-acknowledge-task': acknowledge_task_command,
            'mssportal-activate-playbook': activate_playbook_command,
            'mssportal-activate-playbook-1': activate_playbook_1_command,
            'mssportal-add-linked-cases': add_linked_cases_command,
            'mssportal-add-linked-threat': add_linked_threat_command,
            'mssportal-add-threat-comment': add_threat_comment_command,
            'mssportal-confirm-case-incident': confirm_case_incident_command,
            'mssportal-create-alert': create_alert_command,
            'mssportal-create-case': create_case_command,
            'mssportal-create-comment-on-case': create_comment_on_case_command,
            'mssportal-create-comment-on-task': create_comment_on_task_command,
            'mssportal-create-customer': create_customer_command,
            'mssportal-create-identity': create_identity_command,
            'mssportal-create-playbook': create_playbook_command,
            'mssportal-create-playbook-task': create_playbook_task_command,
            'mssportal-create-task': create_task_command,
            'mssportal-create-threat': create_threat_command,
            'mssportal-create-webhook': create_webhook_command,
            'mssportal-delete-customer': delete_customer_command,
            'mssportal-delete-identity': delete_identity_command,
            'mssportal-delete-playbook': delete_playbook_command,
            'mssportal-delete-playbook-task': delete_playbook_task_command,
            'mssportal-delete-task': delete_task_command,
            'mssportal-delete-threat': delete_threat_command,
            'mssportal-delete-webhook': delete_webhook_command,
            'mssportal-download-case-attachment': download_case_attachment_command,
            'mssportal-download-task-attachment': download_task_attachment_command,
            'mssportal-download-threat-attachment': download_threat_attachment_command,
            'mssportal-find-alert': find_alert_command,
            'mssportal-find-alerts': find_alerts_command,
            'mssportal-find-alerts-1': find_alerts_1_command,
            'mssportal-find-case': find_case_command,
            'mssportal-find-case-attachment': find_case_attachment_command,
            'mssportal-find-case-attachments': find_case_attachments_command,
            'mssportal-find-case-sources-by-customer-id': find_case_sources_by_customer_id_command,
            'mssportal-find-cases': find_cases_command,
            'mssportal-find-comments': find_comments_command,
            'mssportal-find-count-of-unread-comments-by-case-id-and-accountable': find_count_of_unread_comments_by_case_id_and_accountable_command,
            'mssportal-find-customers': find_customers_command,
            'mssportal-find-linked-cases': find_linked_cases_command,
            'mssportal-find-linked-threats': find_linked_threats_command,
            'mssportal-find-playbook': find_playbook_command,
            'mssportal-find-playbook-task': find_playbook_task_command,
            'mssportal-find-playbook-tasks': find_playbook_tasks_command,
            'mssportal-find-playbooks': find_playbooks_command,
            'mssportal-find-task': find_task_command,
            'mssportal-find-task-attachment': find_task_attachment_command,
            'mssportal-find-task-attachments': find_task_attachments_command,
            'mssportal-find-task-comment': find_task_comment_command,
            'mssportal-find-task-count': find_task_count_command,
            'mssportal-find-tasks': find_tasks_command,
            'mssportal-find-threat': find_threat_command,
            'mssportal-find-threat-attachment': find_threat_attachment_command,
            'mssportal-find-threat-attachments': find_threat_attachments_command,
            'mssportal-find-threats': find_threats_command,
            'mssportal-get-current': get_current_command,
            'mssportal-get-customer': get_customer_command,
            'mssportal-get-identities': get_identities_command,
            'mssportal-get-service-metrics': get_service_metrics_command,
            'mssportal-get-webhooks': get_webhooks_command,
            'mssportal-put-current-key': put_current_key_command,
            'mssportal-put-customer': put_customer_command,
            'mssportal-put-identity': put_identity_command,
            'mssportal-put-webhook': put_webhook_command,
            'mssportal-remove-case-attachment': remove_case_attachment_command,
            'mssportal-remove-linked-case': remove_linked_case_command,
            'mssportal-remove-linked-threat': remove_linked_threat_command,
            'mssportal-remove-task-attachment': remove_task_attachment_command,
            'mssportal-remove-threat-attachment': remove_threat_attachment_command,
            'mssportal-resolve-case': resolve_case_command,
            'mssportal-update-case': update_case_command,
            'mssportal-update-comment-on-task': update_comment_on_task_command,
            'mssportal-update-comment-on-task-1': update_comment_on_task_1_command,
            'mssportal-update-playbook': update_playbook_command,
            'mssportal-update-playbook-task': update_playbook_task_command,
            'mssportal-update-read-flag-for-comment-on-task': update_read_flag_for_comment_on_task_command,
            'mssportal-update-task': update_task_command,
            'mssportal-update-threat': update_threat_command,
            'mssportal-update-threat-comment': update_threat_comment_command,
            'mssportal-upload-case-attachment': upload_case_attachment_command,
            'mssportal-upload-task-attachment': upload_task_attachment_command,
            'mssportal-upload-threat-attachment': upload_threat_attachment_command,
        }

        if command == 'test-module':
            test_module(client)
        elif command in commands:
            return_results(commands[command](client, args))
        else:
            raise NotImplementedError(f'{command} command is not implemented.')

    except Exception as e:
        return_error(str(e))


if __name__ in ['__main__', 'builtin', 'builtins']:
    main()
