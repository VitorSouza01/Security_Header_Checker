
# Security Header Checker

# Importando a biblioteca
import requests

url = str(input("[+] URL: "))

# Lista de Headers
def check_security_headers(url):
    headers_to_check = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-XSS-Protection",
        "X-Content-Type_Options",
        "Referrer-Policy",
        "Feature-Policy"
    ]

    # Validação dos Headers
    response = requests.head(url)
    missing_headers = []

    for header in headers_to_check:

        if header not in response.headers:
            missing_headers.append(header)

    # Exibição dos Headers que estão Faltando
    if len(missing_headers) == 0:
        print(f"[+] {url} site OK")

    else:
        print(f"[-] {url} falta os headers:")

        for header in missing_headers:
            print(header)


check_security_headers(url)
