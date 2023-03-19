def SiftDown(data, swaps, i):
    # 
    n = len(data)
    indekss = i
    child = 2 * i + 1
    mc = child < n and data[child] < data[indekss]
    indekss += mc * (child - indekss)
    child += mc
    mc = child < n and data[child] < data[indekss]
    indekss += mc * (child - indekss)
    child += mc
    if indekss != i:
        swaps.append((i, indekss))
        data[i], data[indekss] = data[indekss], data[i]
        SiftDown(data, swaps, indekss)


def build_heap(data):
    swaps = [] 

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)
    i = n // 2 - 1
    while i >= 0:
        SiftDown(data, swaps, i)
        i -= 1
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    
    text = input("Ievadiet 'I' vai 'F': ")
    
    # input from keyboard
    
    if "I" in text:
        n = int(input("Input the size: "))
        data = list(map(int, input("Input the heap: ").split()))
    elif "F" in input_type:
        while True:
            try:
                file_name = "/tests" + input()
                with open(file_name, 'r', encoding="utf-8") as f:
                    n = int(f.readline().strip())
                    data = list(map(int, f.readline().strip().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
