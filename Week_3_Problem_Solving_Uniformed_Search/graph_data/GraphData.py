"""
@author: Devangini Patel

Reference: https://www.python.org/doc/essays/graphs/
"""

# create a dictionary with all the mappings
connections = {"Dev": {"Ali", "Seth", "Tom"}, "Ali": {"Dev", "Seth", "Ram"}, "Seth": {"Ali", "Tom", "Harry"},
               "Tom": {"Dev", "Seth", "Kai", 'Jill'}, "Ram": {"Ali", "Jill"}, "Kai": {"Tom"}, "Mary": {"Jill"},
               "Harry": {"Seth"}, "Jill": {"Ram", "Tom", "Mary"}}

print(connections["Harry"])

print(type(connections["Harry"]))
