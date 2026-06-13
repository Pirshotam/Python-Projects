print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    if num % 3 == 0 and num % 7 == 0:
        return "FizzBuzz"
    elif num % 7 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif "3" in str(num):
        return "Almost Fizz"
    else:
        return str(num)
    
# Get user input
limit = int(input("Enter a number: "))

# Loop through and print results
for i in range(1, limit + 1):
    print(fizzbuzz(i))
