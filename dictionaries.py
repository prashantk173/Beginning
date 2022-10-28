monthconv = {
    "jan":"January",
    "feb":"February",
    "mar":"March",
    "apr":"April",
    "may":"May",
    "jun":"June",
    "jul":"July",
    "Aug":"August",
    "sept":"September",
    "oct":"October",
    "nov":"November",
    "dec":"December"
} #we can also use numbers as keys.

print(monthconv["mar"]) #using [] to call the keys.
print(monthconv.get("oct"))
print(monthconv.get("octo", "Invalid Key")) # using get fn we can assign default values.

numbers = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}

print(numbers[1])
print(numbers.get(7,"Not valid"))
print(numbers.get(3,"not valid"))