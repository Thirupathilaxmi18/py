fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits ]

print(newlist)
numbers=[1,2,3,4,5]
doubled_numbers=[num*2 for num in numbers]
print("doubled numbers:",doubled_numbers)

even_numbers=[x  for x in range(1,10) if x%2==0]
print("even numbers:",even_numbers)

primes = [x for x in range(2, 20) if all(x % y != 0 for y in range(2, int(x**0.5) + 1)) ]
print(primes)
print(len(primes))
prime=[x for x in range(0,100) if all(x%y!=0 for y in range(2,int(x/2+1)))]
print(prime)
print(len(prime))



numbers = [1, 2, 3, 4, 5, 6]
even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(even_odd_list)

word = "Python"
vowels = "aeiou"
result = [char for char in word if char in vowels]
print(result)

lis = [num for num in range(100)

	if num % 5 == 0 if num % 10 == 0]
print(lis)

