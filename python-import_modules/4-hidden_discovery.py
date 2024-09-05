#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    all = dir(hidden_4)
    for n in all:
        if n[:2] != "__":
            print(n)
