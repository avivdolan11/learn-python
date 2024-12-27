class SmartPhone():
    def __init__(self):
        self._company = "apple"
        self._firmware = 10.0
    
    def get_os_version(self):
        return self._firmware
    
    def update_firmware(self):
        self._firmware += 1

iphone = SmartPhone()
print(iphone._company)
print(iphone._firmware)

print(iphone.update_firmware())
print(iphone._firmware)



class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

    def copyright(self):
        return f"Copyright {self._author}, {self._publisher}"
    
    def rip_in_half(self):
        if self.page_count > 1:
            return self.page_count / 2
        else:
            return self.page_count == 0