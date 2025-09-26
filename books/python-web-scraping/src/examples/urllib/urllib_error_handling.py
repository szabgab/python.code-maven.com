import urllib.request
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} URL")

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as fh:
        html = fh.read()
except urllib.error.HTTPError as err:
    if err.code == 404:
        print("not found")
    elif err.code == 500:
        print("internal error")
    else:
        print(f"Unhandled error: {err.code}")

    print(f"HTTPError: {err}")
except urllib.error.URLError as err:
    print(f"URLError: {err}")
    print(err.reason)
else:
    print(f"Success: Downloaded {len(html)} characters.")
