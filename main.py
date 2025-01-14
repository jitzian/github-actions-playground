import os

def __main__():
    print("Hello, World as a test!")
    name = os.getenv("USERNAME")
    print(f"Hello {name}, from github!")

if __name__ == "__main__":
    __main__()
    