def convert_gallons_to_cups(gallons):
    def gallon_to_quartz(gallons):
        print(f"Converting {gallons} gallons to quartz")
        return gallons * 4
    def quartz_to_pints(quartz):
        print(f"Converting {quartz} quartz to pints")
        return quartz * 2 
    def pints_to_cups(pints):
        return pints * 2
    
    quartz = gallon_to_quartz(gallons)
    pints = quartz_to_pints(quartz)
    cups = pints_to_cups(pints)
    return cups

print(convert_gallons_to_cups(3))