from unittest.mock import Mock, MagicMock

plain_mock = Mock()
magic_mock = MagicMock()

# print(len(plain_mock))
print(len(magic_mock))

# print(plain_mock[3])
print(magic_mock[3])

magic_mock.__len__.return_value = 50
print(len(magic_mock))
