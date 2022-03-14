from ch01.binary_search import binary_search
def test_binary_search_sucessfull():
    for item in range(10):
        input_list = list(range(1, 101))
        index_item = binary_search(input_list, item)
        if index_item:
            assert input_list[index_item] == item

def test_binary_search_return_None():
    input_list = list(range(1, 101))
    assert binary_search(input_list, 200) is None
