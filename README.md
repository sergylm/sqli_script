# sqli_script
This script automates SQL Injection (SQLi) on a specified target URL by extracting data from a given database, table, and column. 

## Features
- Constructs SQL payloads dynamically based on user input.
- Supports optional WHERE clauses for filtering.
- Iteratively extracts data by modifying offsets until default match is found.

## Prerequisites
- Python 3.6 or higher.
- requests library for HTTP requests.
- Basic knowledge of SQL Injection principles.

## Usage
`python script.py -url <target_url> --database <database_name> --table <table_name> --column <column_name> --match <regex_pattern> [--where <condition>]`

### Arguments
|Argument|Description|
|--------|-----------|
|--url| Target URL vulnerable to SQL Injection.|
|--database/-db| Name of the target database.|
|--table/-t| Name of the table to query.|
|--column/-c| Column to extract data from.|
|--match/-m| Regex pattern to match and extract data from responses.|
| --where/-w (optional)| SQL WHERE clause for filtering rows.|

## Example
`python script.py -url "http://example.com/item?id=1" -db "test_db" -t "users" -c "username" -m "<div class=response>\s*(*?)\s*<\/div>" -w "role='admin'"`
