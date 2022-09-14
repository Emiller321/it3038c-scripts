#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')


echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative COVID cases, $DEATH deaths and $HOSPITALIZED hospitalized"
