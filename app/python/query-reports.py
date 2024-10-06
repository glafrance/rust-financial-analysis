from sec_api import QueryApi
from sec_api import RenderApi
import json

def download_filing(url):
  try:
    filing = renderApi.get_filing(url)
    # file_name example: 000156459019027952-msft-10k_20190630.htm
    file_name = url.split("/")[-2] + "-" + url.split("/")[-1]
    download_to = "./filings/" + file_name
    with open(download_to, "w") as f:
      f.write(filing)
  except Exception as e:
    print("Problem with {url}".format(url=url))
    print(e)

file = open("../../../private-do-not-commit-to-git/sec-api.io-api-key.txt", "r")
api_key = file.read()
# print(api_key)
file.close()

queryApi = QueryApi(api_key=api_key)
renderApi = RenderApi(api_key=api_key)

query = {
  "query": { "query_string": {
      "query": "formType:\"10-K\" AND ticker:TSLA", # only 10-Ks
  }},
  "from": "0", # start returning matches from position null, i.e. the first matching filing
  "size": "1"  # return just one filing
}

response = queryApi.get_filings(query)
# print(json.dumps(response["filings"][0]["linkToFilingDetails"], indent=2))

download_filing(response["filings"][0]["linkToFilingDetails"])
