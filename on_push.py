import os

def __main__():
    print("This is happening because of a push event!")
    name = os.getenv("USERNAME")
    print(f"Hello {name}, made a push to the repository!")

if __name__ == "__main__":
    __main__()
    