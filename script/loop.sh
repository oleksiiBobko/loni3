#!/bin/bash

for i in KAR BABA.K EPAM.N
do
    curl --location --request GET 'https://a206160-tscc-qs-bdev1-use1-2078426464.us-east-1.elb.amazonaws.com/data/historical-pricing/v1/views/interday-summaries/$i?start=2020-12-10T18:00:00.000000000Z&end=2020-12-10T18:50:00.000000000Z&interval=P1D' \
    --header 'x-ts-uuid: PATSFCP-REALTIME' \
    --header 'x-ts-applicationid: localTest' \
    --header 'x-ts-requestid: localTest_66fc1c92-8f7f-4265-a7b7-44cb8df77181' \
    --header 'x-ts-productid: historical pricing'

done
