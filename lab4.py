

def get_list():
    numbers = input("Enter numbers separated by spaces: ")
    parts = numbers.split()
    lst = []
    for p in parts:
        lst.append(float(p))
    return lst

def get_min(lst):
    return min(lst)

def get_max(lst):
    return max(lst)

def get_mean(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

def get_median(lst):
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

def get_stddev(lst):
    mean = get_mean(lst)
    total = 0
    for num in lst:
    return math.sqrt(total / len(lst))

def print_menu():
    print("\n1. Minimum")
    print("2. Maximum")
    print("3. Mean")
    print("4. Median")
    print("5. Standard Deviation")
    print("6. Exit")

def main():
    lst = get_list()
    choice = ""

    while choice != "6":
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Minimum:", get_min(lst))
        elif choice == "2":
            print("Maximum:", get_max(lst))
        elif choice == "3":
            print("Mean:", get_mean(lst))
        elif choice == "4":
            print("Median:", get_median(lst))
        elif choice == "5":
            print("Standard Deviation:", get_stddev(lst))

main()
