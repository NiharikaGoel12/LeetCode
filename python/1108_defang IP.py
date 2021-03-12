def defangIPaddr(address):
    revise_address = ""
    for i in address:
        if i == '.':
            revise_address += '[.]'
        else:
            revise_address += i
    return revise_address

def main():
    address = "1.1.1.1"
    print(defangIPaddr(address))

main()


# def main():
#     address = "1.1.1.1"
#     print(address.replace('.', '[.]'))