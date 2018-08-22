#!/bin/env bash
PYTHONIOENCODING=UTF-8
while [ true ]; do
 sleep 1
 # do what you need to here

 python read_from_mysql.py
 python python_sankey_01.py
 svg-sankey --size 1920,1080 --margins 10,150 ivr_rec_sankey.json > ivr_rec_sankey.svg
 python remove_header.py
 cp ivr_rec_sankey.svg ivr_rec_sankey_1.svg
 sleep 2
 cp ivr_rec_sankey_1.svg ivr_rec_sankey_2.svg
done

