import json
import os

with open('apiclient.json', 'r+') as f:
    data = json.load(f)
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

new_file_name = 'new-apiclient.json'

with open(new_file_name, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2))


os.system('demisto-sdk openapi-codegen -i new-apiclient.json -n MSSPortal -o MSSPortal'
          + ' -u "id" -pr mssportal -r "MSSPortal" -afv')
