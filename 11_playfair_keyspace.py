import math

key = input("Enter the Playfair key: ")

print("Entered key:", key)
print("Raw Playfair keyspace: 25!")
print("log2(25!) =", round(math.log2(math.factorial(25)), 2))
print("Approximate raw keyspace: 2^%.2f" % math.log2(math.factorial(25)))
print("Effective unique key count depends on which equivalent matrices your textbook treats as identical.")