#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for mod in dir(hidden_4):
        if mod[0:2] != "__":
            print(mod)
