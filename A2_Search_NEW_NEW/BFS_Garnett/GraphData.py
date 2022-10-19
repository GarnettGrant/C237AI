'''
@author: Devangini Patel

Reference: https://www.python.org/doc/essays/graphs/
'''

# create a dictionary with all the mappings
relationships = {}
relationships["Adam"] = {"Ema", "Garnett", "Bob"}
relationships["Ema"] = {"Bob", "Adam", "Dolly"}
relationships["Garnett"] = {"Adam", "George", "Frank"}
relationships["Bob"] = {"Adam", "Ema", "Dolly"}
relationships["George"] = {"Garnett"}
relationships["Frank"] = {"Garnett"}
relationships["Dolly"] = {"Bob", "Ema"}
