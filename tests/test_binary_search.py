from ch01.binary_search import binary_search, binary_search_number_of_steps
def test_binary_search_sucessfull():
    for item in range(10):
        input_list = list(range(1, 101))
        index_item = binary_search(input_list, item)
        if index_item:
            assert input_list[index_item] == item

def test_binary_search_return_None():
    input_list = list(range(1, 101))
    assert binary_search(input_list, 200) is None

def test_max_steps_for_100_items():
    input_list = list(range(1, 101))
    _, number_of_steps =  binary_search_number_of_steps(input_list, 100)
    assert number_of_steps == 7


def test_max_steps_for_128_items():
    input_list = list(range(1, 129))
    _, number_of_steps =  binary_search_number_of_steps(input_list, 128)
    assert number_of_steps == 8

def test_max_steps_for_256_items():
    input_list = list(range(1, 257))
    _, number_of_steps =  binary_search_number_of_steps(input_list, 256)
    assert number_of_steps == 9