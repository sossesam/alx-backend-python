#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(666.666)

print(ans == math.floor(666.666))
print(floor.__annotations__)
print("floor(666.666) returns {}, which is a {}".format(ans, type(ans)))