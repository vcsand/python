key_names = ["id", "nev", "ip", "datum"]
key_widths = [8, 15, 12, 20]

def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()

def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()

def show_ddns(ddns):
    for (n, w) in zip(key_names, key_widths):
        print(str(ddns[n]).ljust(w), end='| ')
    print()

def show(json):
    show_head()
    if type(json) is list:
        for ddns in json:
            show_ddns(ddns)
    elif type(json) is dict:
        if json:
            show_ddns(json)
        else:
            show_empty()
if __name__ == "__main__":
	print("Hiba!")
	exit()

