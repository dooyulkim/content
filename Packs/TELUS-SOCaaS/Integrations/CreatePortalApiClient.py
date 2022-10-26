import json
import os

title = input("Enter the title of the integration. EX)SOC as a service from TELUS:")
with open('apiClient.json', 'r+') as f:
    data = json.load(f)
    if title:
        data["info"]["title"] = title
    for path in data.get('paths').items():
        for methodDef in path[1].items():
            parameters = []
            requestBody = False
            for methodDefElm in methodDef[1].items():
                if(methodDefElm[0] == "requestBody"):
                    requestBody = True
                    if methodDef[1].get("parameters"):
                        parameters = methodDef[1]["parameters"]
                        parameters.append(
                            {
                                "in": "body",
                                "name": "body",
                                "required": True,
                                "schema": methodDefElm[1]["content"]["application/json"]["schema"]
                            }
                        )
                    else:
                        parameters = [(
                            {
                                "in": "body",
                                "name": "body",
                                "required": True,
                                "schema": methodDefElm[1]["content"]["application/json"]["schema"]
                            }
                        )]
                if(methodDefElm[0] == "responses"):
                    methodDefElm[1]["200"].pop("headers", None)

            if requestBody:
                methodDef[1]["parameters"] = parameters
                methodDef[1].pop("requestBody", None)

new_file_name = 'newApiClient.json'
with open(new_file_name, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2))

name = input("Enter the name of integration: ")
isdir = os.path.isdir(f"./{name}")
if(isdir):
    raise Exception("Sorry, An integration with the same name exists.")
else:
    command_prefix = input("Enter the command prefix. Ex) mssportal: ")
    command = f'demisto-sdk openapi-codegen -i {new_file_name} -n {name} -o {name} -u "id" -pr {command_prefix} -r "{name}" -afv'
    os.system(command)
