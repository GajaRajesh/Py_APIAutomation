import requests
import json
from requests.auth import HTTPBasicAuth

class ApiRequests:
    #GET REQUEST
    def get_request(self,url,auth,headers,in_json):
        response=requests.get(url=url,auth=auth,headers=headers)
        if in_json is True:
            return response.json()
        return response

    #post Request
    def post_request(self,url,auth,headers,payload,in_json):
        response=requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
        if in_json is True:
            return response.json()
        return response

    #Patch Request
    def patch_request(self,url,auth,headers,payload,in_json):
        response=requests.patch(url=url,auth=auth,headers=headers,data=json.dumps(payload))
        if in_json is response:
            return response.json()
        return response

    #Put Request

    def put_request(self,url,auth,headers,payload,in_json):
        response= requests.put(url=url,auth=auth,headers=headers,data=json.dumps(payload))
        if in_json is True:
            return response.json()
        return response

    #Delete Request
    def delete_request(self,url,auth,headers,in_json):
        response=requests.delete(url=url,auth=auth,headers=headers)
        if in_json is True:
            return response.json()
        return response.json()


