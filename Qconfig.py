APItoken='your_api_token'
config = {"url": "https://quantumexperience.ng.bluemix.net/api"}
if APItoken is None:
    raise Exception("Please set your IBM Q access token in Qconfig.py")
