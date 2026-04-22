# ============================================================
#  WEEK 14 LAB — Q2: HTTP SECURITY HEADER CHECKER
#  COMP2152 — Jamshaid Mirpour
# ============================================================

import urllib.request


# Security headers every website should have
REQUIRED_HEADERS = {
    "Content-Type":              "Defines the content format",
    "X-Frame-Options":           "Vulnerable to clickjacking",
    "X-Content-Type-Options":    "Vulnerable to MIME sniffing",
    "Strict-Transport-Security": "No HTTPS enforcement",
    "Content-Security-Policy":   "No XSS protection policy",
    "X-XSS-Protection":         "No XSS filter",
}


# TODO: Complete check_headers(url)
#   Make a request to url using urllib.request.urlopen
#   Get response headers: dict(response.headers)
#   For each header in REQUIRED_HEADERS:
#     If the header exists in response → append {"header": name, "present": True, "value": value}
#     If missing → append {"header": name, "present": False, "value": "MISSING"}
#   Return the list
#   If the request fails, return an empty list
def check_headers(url):
    try:
        with urllib.request.urlopen(url) as response:
            headers = dict(response.headers)
            results = []
            for header in REQUIRED_HEADERS:
                if header in headers:
                    results.append({
                        "header": header,
                        "present": True,
                        "value": headers[header]
                    })
                else:
                    results.append({
                        "header": header,
                        "present": False,
                        "value": "MISSING"
                    })
            return results
    except Exception as e:
        return []
    
    


# TODO: Complete generate_report(url, results)
#   Print the URL
#   missing_count = 0
#   For each result:
#     If present: print f"  ✓ {header}: {value}"
#     If missing: print f"  ✗ {header}: MISSING — {REQUIRED_HEADERS[header]}"
#       Increment missing_count
#   Print f"  Missing {missing_count} of {len(results)} security headers!"
def generate_report(url, results):
    print(f"URL: {url}")
    missing_count = 0
    for result in results:
        header = result["header"]
        if result["present"]:
            print(f"  ✓ {header}: {result['value']}")
        else:
            print(f"  ✗ {header}: MISSING — {REQUIRED_HEADERS[header]}")
            missing_count += 1
    print(f"  Missing {missing_count} of {len(results)} security headers!")
        


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: HTTP SECURITY HEADER CHECKER")
    print("=" * 60)

    urls = [
        "http://httpbin.org",
        "https://www.google.com",
    ]

    for url in urls:
        print(f"\n--- Checking {url} ---")
        results = check_headers(url)
        if results:
            generate_report(url, results)
        else:
            print("  (could not connect or not implemented)")

    print("\n" + "=" * 60)