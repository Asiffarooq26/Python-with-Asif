import requests
sql_errors = [
"sql syntax",
"mysql",
"syntax error",
"database error",
"unclosed quotation",
"unknown column",
]
def test_input(url, param, test_value):
    try:
        payload = {param: test_value}
        response = requests.get(url, params=payload, timeout=5)
        text = response.text.lower()
        for error in sql_errors:
            if error in text:
                return True # SQL error found
    except:
        pass
        return False
test_values = [
"'",
"\"",
"''",
"\"\"",
";",
]
def scan(url, param):
    print(f"\nTesting parameter: {param}\n")
    for value in test_values:
        print(f"Trying: {value}")
        if test_input(url, param, value):
            print(f"[!] SQL Error detected with input: {value}")
        else:
            print(f"[OK] No SQL error\n")

url = input("Enter URL: ")
param = input("Parameter to test: ")
scan(url, param)