import sys

def compress(string : str) -> dict:
    if type(string) != str:
        raise TypeError("Input must be a string")

    compression_dict  = {}
    for index, symbol in enumerate(string):
        if symbol in compression_dict:
            compression_dict[symbol].append(index)
        else:
            compression_dict[symbol] = [index]

    return compression_dict

def decompress(compressed_dict : dict) -> str:
    if type(compressed_dict) != dict:
       raise TypeError("Input must be a dict")

    length = sum(len(item) for item in compressed_dict.values())
    chars = [0] * length
    for key, value in compressed_dict.items():
        for index in value:
            chars[index] = key
    return "".join(chars)



if __name__ == "__main__":
    string = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris lectus nulla, sagittis at pharetra ut, finibus vel dui. 
    Ut a lorem nec risus efficitur consectetur nec quis mi. 
    Aenean vehicula, sem vel porta sagittis, lorem ipsum rhoncus quam, pharetra finibus ex ex id magna. 
    Nulla consectetur non neque vel finibus. Sed lacinia, magna ultricies vehicula ornare, arcu magna maximus massa, eu sagittis quam massa id ex. 
    Vestibulum ac diam hendrerit, imperdiet augue suscipit, lacinia elit. 
    Vivamus maximus interdum velit ac vulputate. Donec ac mauris vitae arcu rhoncus ornare ut non odio. 
    Ut volutpat ornare sapien, vitae accumsan nisl mollis vel. Phasellus et feugiat augue, non tincidunt lectus. 
    Ut faucibus iaculis neque, vel faucibus lectus semper id. 
    Maecenas lacinia, enim in porttitor porta, diam nisl efficitur nunc, ac interdum ipsum nibh ac sapien.
    """
    compressed_dict = compress(string)
    print(compressed_dict)
    print(f"""Size of string is {sys.getsizeof(string)}\n
    Size of compressed string is {sys.getsizeof(compressed_dict)}""")

    uncompressed_string = decompress(compressed_dict)
    print(f"Uncompressed string is {uncompressed_string}")
