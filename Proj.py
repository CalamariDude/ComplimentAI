
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'abc7b1ab904041b69126b58a290af454',
}

params = urllib.parse.urlencode({
    # Request parameters

})


def jsonReader(input):
    parsed_json = json.loads(input)
    list = parsed_json['description']
    fh = open("hello.txt", "w")
    fh.write(str(list))

class Proj:
    def mainer(self, stra):
        try:
            conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/vision/v1.0/describe?%s" % params, '{"url": "%s" }' % stra, headers)
            response = conn.getresponse()
            data = response.read()
            jsonReader(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))




