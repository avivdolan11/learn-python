def be_nice(fn):
    def inner():
        print("Nice to meet you")
        fn()
        print("It was my pleasure")
    
    return inner

@be_nice
def complex_business_logic():
    print("Something complex")


complex_business_logic()

# result = be_nice(complex_business_logic)
# result()
# be_nice(complex_business_logic)()