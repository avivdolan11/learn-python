from unittest.mock import Mock

mock = Mock(return_value=25)

# print(mock.return_value())
# mock.return_value = 25
print(mock())

stuntman = Mock()
stuntman.jump_off_building.return_value = "My leg"
stuntman.light_on_fire.return_value = "It burns"

print(stuntman.jump_off_building())
print(stuntman.light_on_fire())