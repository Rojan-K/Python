def show_info(**pack):
    for key, value in pack.items():
        print(f"{key}: {value}")

show_info(name="Rojan",age=12)
show_info(name="Bibek",age=21,city="Kharibot")