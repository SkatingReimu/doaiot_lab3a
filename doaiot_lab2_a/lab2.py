import statistics

def main():
    print("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temp(num_list)
    calc_minmax_temp(num_list)
    sort_temp(num_list)
    median_temp(num_list)

def display_main_menu():
    print("Enter different area temperatures separated by commas (e.g. 5, 67, 32):")

def get_user_input():
    x=input()
    y = x.split(", ")
    b=[float(a) for a in y]
    return b

def calc_average_temp(b):
    t = sum(b)
    avg = t/len(b)
    print("Average temp: ", avg)
    return avg

def calc_minmax_temp(b):
    mint = min(b)
    maxt = max(b)
    print("Min temp: ", mint)
    print("Max temp: ", maxt)
    min_max = [mint, maxt]
    return min_max

def sort_temp(b):
    print("Temps in ascending order: ", sorted(b))
    return sorted(b)

def median_temp(b):
    d=statistics.median(b)
    print("Median temp: ", d)
    return d

if __name__ == "__main__":
    main()

