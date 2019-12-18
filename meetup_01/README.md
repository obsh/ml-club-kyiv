```bash
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d '{
  "payload": {
    "row": {
      "values": [
        "Троєщина",
        "2.0",
        "52",
        "5",
        "серія КТ",
        "1984",
        "панель",
        "False",
        "Деснянський"
      ],
      "columnSpecIds": [
        "1005780460531351552",
        "5617466478958739456",
        "3311623469745045504",
        "7923309488172433408",
        "2158701965138198528",
        "6770387983565586432",
        "4464544974351892480",
        "9076230992779280384",
        "8499770240475856896"
      ]
    }
  }
}' \
 https://eu-automl.googleapis.com/v1beta1/projects/ml-club-kyiv/locations/eu/models/TBL4996251205358321664:predict
```