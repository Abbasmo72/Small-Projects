from faker import Faker

fake = Faker()  # Create an instance of the Faker class

# Generate and print a fake name
print(fake.name()) 

# Generate and print a fake address
print(fake.address()) 

# Generate and print a fake text (paragraph)
print(fake.text()) 

# Generate and print a fake email address
print(fake.email()) 

# Generate and print a fake country name
print(fake.country()) 

# Generate and print fake latitude and longitude coordinates
print(fake.latitude(), fake.longitude()) 

# Generate and print a fake URL
print(fake.url()) 
