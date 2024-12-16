def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you")
        fn(*args, **kwargs)
        print("It was my pleasure")
    
    return inner

@be_nice
def complex_business_logic(stakeholder):
    print(f"Something complex for {stakeholder}")

complex_business_logic("Boris")