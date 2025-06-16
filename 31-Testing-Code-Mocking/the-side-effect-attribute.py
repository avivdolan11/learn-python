from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1,10)

call_me_maybe = Mock(side_effect=generate_number)
#print(call_me_maybe.side_effect)

call_me_maybe.side_effect = generate_number
print(call_me_maybe())


three_item_list = Mock()
three_item_list.pop.side_effect = [3,2,1, IndexError("Pop from empty list")]

print(three_item_list.pop())
print(three_item_list.pop())
print(three_item_list.pop())
# print(three_item_list.pop())

mock = Mock(side_effect= NameError("Some error"))
mock()


### Exercise

from unittest.mock import Mock

airport = Mock()

airport.gates = ["A1", "B2", "C3"]
airport.departures = {
      "Atlanta": "12:00PM",
      "Nashville": "04:30PM"
}

airport.close.return_value = "Closing"
airport.open.side_effect = ["Opening", "Already open"]
