#!/usr/bin/env python3

import requests, time

t_end = time.time() + 60 * 5

while time.time() < t_end:
    url_time = requests.get("https://gitlab.com").elapsed.total_seconds()
print(url_time)
