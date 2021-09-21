#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:56:30 2021

Uses Blockchain.com API to retrieve important data from all of the major bitcoin exchanges.

@author: Ben
"""

import requests
import pandas as pd
from datetime import datetime

headers =  {"X-API-Token" : "Bearer{5bae91f0-8215-4baa-87d2-b4b5b09b3963}"}
#Headers for our API Key

response = requests.get("https://api.blockchain.com/v3/exchange/tickers/BTC-USD")
#Basic unfiltered API response

date = "2020-03-01"

print(datetime.date(date))