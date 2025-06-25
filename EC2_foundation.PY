import random
import string

# Step 1: Ask user how many EC2 names they want
num_names = int(input("How many EC2 instance names do you want to generate? "))

# Step 2: Ask for department name
department = input("Enter your department name: ")

# Step 3: Generate and print EC2 names
for _ in range(num_names):
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    ec2_name = f"{department}-{random_str}"
    print(ec2_name)
    

