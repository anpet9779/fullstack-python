chai_type ="ginger"
customer_name = "John Doe"

print(f"Order for {customer_name} : {chai_type} chai.")

# Indexing and slicing:

chai_description = "Aromatic and Bold"

print(f"first word: {chai_description[0:8]}") # Output: first word: Aromatic

print(f"first word: {chai_description[:8]}") # Output: first word: Aromatic

print(f"first word: {chai_description[12:]}") # Output: first word: Bold

print(f"first word: {chai_description[0:8:2]}") # Output: first word: Aoai -- Every 2nd character from 0-8

print(f"first word: {chai_description[::-1]}") # Output: first word: dloB dna citamorA -- reverse the string
