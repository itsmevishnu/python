def convert_number(num_string):
    short_terms = {
    "k":1000, "K":1000,
    "l":100000, "L":100000,
    "cr":10000000, "Cr":10000000, "CR":10000000 }

    regrex = "([0-9]+(?:\.[0-9]+)?)"
    
    error, amount, unit = re.split(regex, num_string)
    
    return float(amount) * short_terms[unit] if unit in short_terms.keys() else "Undefined"
  
  print(convert_number(input("Enter the number")))
