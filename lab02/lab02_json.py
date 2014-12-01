#!/usr/bin/env python
#!*-* coding:utf-8 *-*
import requests
import getpass
"""

:mod:`lab02_json` -- JSON Navigation
=========================================

LAB02 Learning Objective: Learn to navigate a JSON file and convert to a 
                          python object. Practice file IO using with.
      Optional Objective: Pull live data from Rackspace's APIs using the
                          requests module.

::

 a. Based on a sample Openstack authentication response file, what python 
    syntax would you use to access items in the serviceCatalog? 

    What path would access the publicURL for the DFW CloudServersOpenStack endpoint?

 b. Provide a new dict called compute_api_info and add keys "image_id"
    and "flavor_id". Use None for values. Dump compute_api_info 
    to a file in JSON format (same as function in d.iii below)

 c. Based on analysis of the sample authentication response file, provide 
    the following functions in a new module named compute_api_json.py:
     i. get_token_id() 
     ii. get_tenant_id()
     iii. get_compute_public_URL(region) # solve this programmatically 
                                         # i.e. don't hard code

 d. Also provide these functions using the information given in class:
     i. get_image_id()  # use an ID of your choosing (Ex. 9db746f3-c54f-491b-b139-dea4b73bb9cb)
     ii. get_flavor_id()  # return 2
     iii. update_cached_compute_api_info(compute_api_info) # Dump to compute_api_info
     iv. update_cached_auth_response(auth_response) # Dump to auth_api_info

"""
import json
# a
print("a")
auth_content_js = ""
def update_cached_auth_response():
    password = getpass.getpass()
    payload = '{"auth": {"passwordCredentials": {"username":"python2.class", "password":"'+password+'"}}}'
    url = "https://identity.api.rackspacecloud.com/v2.0/tokens"
    headers = {"content-type": "application/json"}
    r = requests.post(url, data=payload, headers=headers)
    print(r.text)
    #with open("auth_sample.json", "r") as fh:
    auth_content = r.text # fh.read()
    auth_content_js = json.loads(auth_content)
    # purl = auth_content_js["access"]["serviceCatalog"][0]["endpoints"][1]["publicURL"]
    return auth_content_js
auth_content_js = update_cached_auth_response()
# b
print("b")
compute_api_info = {"image_id":None, "flavor_id":None}
print(json.dumps(compute_api_info))

# c
print("c")
def get_token_id(auth):
    return(auth["access"]["token"]["id"])

def get_tenant_id(auth):
    for sc in auth["access"]["serviceCatalog"]:
        if sc["name"] == "cloudServers":
            for endpoint in sc["endpoints"]:
                return endpoint["tenantId"]    


def get_compute_public_URL(auth, region):
    for sc in auth["access"]["serviceCatalog"]:
        if sc["type"] == "compute":
            for endpoint in sc["endpoints"]:
                if "region" in endpoint and endpoint["region"] == region:
                    return endpoint["publicURL"]    

#    all_contents = fh.read()
#    all_contents_js = json.loads(all_contents)
print(auth_content_js)
print(get_token_id(auth_content_js))
print(get_tenant_id(auth_content_js))
print(get_compute_public_URL(auth_content_js, "DFW"))

# d
def update_cached_compute_api_info():
    #with open("compute_api_sample.json", "r") as fh:
    #curl -X GET https://dfw.servers.api.rd.com/v2/830389/flavors -H "X-Auth-Token:67f8fe7f324a421f85eb67b648ba2190"
    headers = {"X-Auth-Token":"67f8fe7f324a421f85eb67b648ba2190"}
    # url = "https://dfw.servers.api.rd.com/v2/{0}".format(get_tenant_id(auth_content_js))
    url = "{0}/flavors".format(get_compute_public_URL(auth_content_js, "DFW"))
    print url
    r = requests.get(url, headers=headers)
    compute_api_content = r.text # fh.read()
    compute_api_content_js = json.loads(compute_api_content)
 
    return compute_api_content_js 
compute_api_info = update_cached_compute_api_info() 
print(compute_api_info)
def get_image_id(compute_info):
   return compute_info["flavor_ID"] 

def get_flavor_id(compute_info):
    return compute_info["image_ID"]

print(get_image_id(compute_api_info))
print(get_flavor_id(compute_api_info))
