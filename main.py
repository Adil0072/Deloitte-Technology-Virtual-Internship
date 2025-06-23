import json, unittest, datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    json_dict = json.loads(json.dumps(jsonData1))
    json_object = json.dumps(jsonData1)
    #Updating dictonary for the required format
    json_dict.update({
        "location": {
            "country": json_dict["location"].split("/")[0],
            "city": json_dict["location"].split("/")[1],
            "area": json_dict["location"].split("/")[2],
            "factory": json_dict["location"].split("/")[3],
            "section": json_dict["location"].split("/")[4]
        }
    })

    json_dict.update({
        "data": {
            "status": json_dict["operationStatus"],
            "temperature": json_dict["temp"]
        }
    })

    del json_dict["operationStatus"]
    del json_dict["temp"]

    return json_dict


def convertFromFormat2(jsonObject):

    # IMPLEMENT: Conversion From Type 1

    json_dict = json.loads(json.dumps(jsonData2))
    json_object = json.dumps(jsonData2)

    json_dict.update({
        "deviceID":
        json_dict["device"]["id"],
        "deviceType":
        json_dict["device"]["type"],
        "timestamp":
        int(
            datetime.datetime.strptime(json_dict["timestamp"],
                                       "%Y-%m-%dT%H:%M:%S.%fZ").timestamp() *
            1000),
        "location": {
            "country": json_dict["country"],
            "city": json_dict["city"],
            "area": json_dict["area"],
            "factory": json_dict["factory"],
            "section": json_dict["section"]
        }
    })

    del json_dict["device"]
    del json_dict["country"]
    del json_dict["city"]
    del json_dict["area"]
    del json_dict["factory"]
    del json_dict["section"]

    return json_dict


def main(jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):

        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 1 failed')

    def test_dataType2(self):

        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 2 failed')


if __name__ == '__main__':
    unittest.main()
