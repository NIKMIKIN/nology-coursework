# def ran_function():
#     print("Hello World!")
   
def is_palindrome(palindrome):
        palindrome = palindrome.lower().replace(' ', '')
        return palindrome == palindrome[::-1]
# print("demo")
if __name__ == "__main__":
    is_palindrome()
# else:
#     print("Ran as import")

