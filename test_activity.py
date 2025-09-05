import json
import math
import csv
import pandas as pd
from pandas import json_normalize
from espn_api.football import League

league = League(
    league_id=394987,
    year=2025 ,
    espn_s2=r'AEC3Lgz00RKOu%2FDNUibH83MpBE%2FlYtyJi65kZuxiq2dT6QGUsIkLg0sl4n1RGgmHdU2GcQC8FDmVRdn49L2IpS7xAwv0YlOXFh8%2FnmwLZndLjwBYATXTKawV6U%2BXAHnlmfuR9QBNky3RyWIhm3Xw5JcG5AKl5RvPYyDCGcpXx6ogieKoH5jRRmWL%2BxpXhi%2BT6tLACcYespcRy10nIrVv%2Fybif6omZBpUamaPNX3oka1yJZoU%2FuSImvEhXysP3xOfB8rjFgipXHLRv4eoL5ITLT1u',
    swid=r'{B9A9106B-C26A-11D4-820E-00A0C9E58E2D}',
    debug=False
    )

activity = league.transactions()
dfs = []
df = pd.DataFrame(activity)
for x in activity:
    print(x)
print(df)