import os

def __main__():
    print("This is happening because a pull request was made!")
    name = os.getenv("USERNAME")
    print(f"Hello {name}, made a pull request to the repository!")

if __name__ == "__main__":
    __main__()
    