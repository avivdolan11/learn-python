def outer():
    bubble_tea_flav = 'Black'

    def inner():
        nonlocal bubble_tea_flav
        bubble_tea_flav = "Taro"

    inner()

    return bubble_tea_flav

print(outer())