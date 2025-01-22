nested_dict = {
    'fruits': ['apple', 'banana', 'cherry'],
    'vegetables': ['carrot', 'broccoli', 'spinach'],
    'grains': ['rice', 'wheat', 'barley']
}

for category, items in nested_dict.items():
    print(f"{category}:")
    for item in items:
        print(f"  - {item}")

# Iterating with a condition inside the nested loop
for category, items in nested_dict.items():
    print(f"{category}:")
    for item in items:
        if 'a' in item:
            print(f"  - {item}")