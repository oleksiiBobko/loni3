import requests

rics = ["BABA.K", "KAR", "EPAM.N"]

my_file = open("mrsp_events_rics.txt", 'r')
rics = my_file.readlines()
rics = [ric.rstrip() for ric in rics]
print(rics)

for ric in rics:
    # r = requests.get(f"https://a206160-tscc-qs-bdev1-use1-2078426464.us-east-1.elb.amazonaws.com/data/historical-pricing/v1/views/interday-summaries/{ric}?start=2020-12-10T18:00:00.000000000Z&end=2020-12-10T18:50:00.000000000Z&interval=P1D",
    #             headers={"Content-Type":"text",
    #             "x-ts-uuid": "PATSFCP-REALTIME",
    #             "x-ts-applicationid": "localTest",
    #             "x-ts-requestid": "localTest_66fc1c92-8f7f-4265-a7b7-44cb8df77181",
    #             "x-ts-productid": "historical pricing"}, verify=False)

    r = requests.get(f"http://localhost:8080/data/historical-pricing/v1/views/interday-summaries/{ric}?start=2020-12-10T18:00:00.000000000Z&end=2020-12-10T18:50:00.000000000Z&interval=P1D",
                headers={"Content-Type":"text",
                "x-ts-uuid": "PATSFCP-REALTIME",
                "x-ts-applicationid": "localTest",
                "x-ts-requestid": "localTest_66fc1c92-8f7f-4265-a7b7-44cb8df77181",
                "x-ts-productid": "historical pricing"}, verify=False)


    print(r.headers)