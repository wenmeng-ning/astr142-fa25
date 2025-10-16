"""
Here are some demos on debugging code.
"""

# ==============================
# 1. print()

# def divide(a, b):
#     print(f"Dividing {a} by {b}")  # Debug statement
#     return a / b

# result = divide(10, 0)


# ==============================
# 2. pdb

# import pdb

# def divide(a, b):
#     pdb.set_trace()  # Breakpoint
#     return a / b

# result = divide(10, 0)


# ==============================
# 3. breakpoint() 

# def divide(a, b):
#     breakpoint()  # Automatically invokes pdb
#     return a / b

# result = divide(10, 0)


# ==============================
# 4. logging module

import logging

logging.basicConfig(
    filename='demo2.log',
    filemode='w',  # 'a' to append
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero", exc_info=True)
        return None

divide(10, 2)
divide(10, 0)
