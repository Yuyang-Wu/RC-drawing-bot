# serialN.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author        Date            Version         Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yuyang Wu     Dec 9, 2022     1.0.0           burn/read serial number from on-board flash
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json


# def burnSN():
#     config = {
#       'SN': '8964',
#       'ref': '3c4e'
#     }
#     with open('SN.json', 'w') as file:
#       json.dump(config, file)


def readSN():
    with open('SN.json', 'r') as file:
        config = json.load(file)
        return config
