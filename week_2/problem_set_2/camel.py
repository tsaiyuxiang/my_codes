# camel.py

import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

if __name__ == "__main__":
    camel_str = input("camelString: ")
    snake_str = camel_to_snake(camel_str)
    print(f"CamelCase: {camel_str}")
    print(f"Snake_case: {snake_str}")

