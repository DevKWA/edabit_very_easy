def burrp_p(number_of_r):
    return number_of_r.count("r") or number_of_r.count("R")


print(burrp_p("Burrp"))
print(burrp_p("BURRRRRRRP"))