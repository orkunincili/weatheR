
import http.client,json

class Weat:
    connection="api.collectapi.com"
    api_key = "7pWscfZvQUT4Mg1xdChzXu:2OMTXkdUKTKBYwbqzQhvXG"
    path="/weather/getWeather?data.lang=en&data.city="
    headers = {
        'content-type': "application/json",
        'authorization': "apikey {}".format(api_key)
    }
    default_city="ankara"
    def create_connection(self):

        return http.client.HTTPSConnection(self.connection)


    def req_and_res(self,conn,city):
        conn.request("GET", self.path + city, headers=self.headers)
        res = conn.getresponse()
        data = res.read()
        result = json.loads(data)

        return result