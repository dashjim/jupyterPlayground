#!/bin/env bash
PYTHONIOENCODING=UTF-8
while [ true ]; do
 sleep 3
 # do what you need to here
 python python_sankey_01.py
 svg-sankey --size 800,600 --margins 10,150 ivr_rec_sankey.json > ivr_rec_sankey.svg
 python remove_header.py
done

