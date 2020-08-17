"""字典推导式"""

prices = {
    'ACME': 3.65,
    'ACM3': 3.25,
    'ACM4': 3.55,
    'ACMR': 3.25,
    'ACMY': 4.65,
    'ACMN': 2.65,
}

print({key: value for key, value in prices.items() if value > 3})
