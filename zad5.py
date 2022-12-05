import requests

class EmissionsApi:
    """
    Class that create method that create responses from Apis endpoints.
    """
    
    
    def __init__(self, method, url, endpoint, headers, path_param=None, path=None, params=None):
        self.__method = method
        self.__url = url
        self.__endpoint = endpoint
        self.__headers = headers
        self.__path_param = path_param
        self.__path = path
        self.__params = params
        
    def request_no_body(self):
        url = f"{self.__url}{self.__endpoint}"
        headers = self.__headers
        if not isinstance(self.__headers, dict):
            raise Exception("Headers must be dictionary.")
        # response = requests.get(url=url, headers=headers)
        response = self.__method(url=url, headers=headers)
        print(response.status_code)
        return response.json()
    
    def request_with_path_parameters(self):
        url = f"{self.__url}{self.__endpoint}{self.__path_param}{self.__path}"
        headers = self.__headers
        params = self.__params
        if not isinstance(self.__headers, dict):
            raise Exception("Headers must be dictionary.")
        if not isinstance(self.__params, dict):
            raise Exception("Params must be a dictionary.")
        response = self.__method(url=url, headers=headers, params=params)
        print(response.status_code)
        # return response.json()
    
    
    
url1 = "https://api.v2.emissions-api.org"
endpoint1 = "/api/v2/countries.json"
headers1 = {
    'Accept': 'application/json',
}
   
emission1 = EmissionsApi(requests.get, url1, endpoint1, headers1)           
            
# nekoja_varijabla = emission1.request_no_body()
# print(nekoja_varijabla)

endpoint2 = "/api/v2/products.json"
emision2 = EmissionsApi(requests.get, url1, endpoint2, headers1)
# print(emision2.request_no_body())

endpoint3 = "/api/v2/"
path3_param = "methane"
path3 = "/average.json"
params = {
    "country": "MK"
}

emision3 = EmissionsApi(requests.get, url1, endpoint3, headers1, path_param=path3_param, path=path3, params=params)
emision3.request_with_path_parameters()