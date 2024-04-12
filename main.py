def reader(path):
    with open(path, 'r') as file:
        contents_file = file.read()
        count_cells, numbers = contents_file.split('\n')
        list_numbers = []

        for i in numbers:
            try:
                list_numbers.append(int(i))
            except:
                pass

    list_numbers.pop()

    return count_cells, list_numbers


def writer(count):
    answer_path = './e.out'

    with open(answer_path, 'w+') as answer:
        answer.write(str(count))


def scaner(cells):
    a = []

    for i in cells:
        a.append(i)
        if comparator(a, cells):
            return len(a)


def comparator(a, b):
    i = 0
    count_true = 0
    iter_count = round(len(b)/len(a))

    while i < iter_count:
        if a == b[i * len(a):len(a)*(i+1):1]:
            count_true += 1
        else:
            break
        i += 1

    if count_true == iter_count:
        return True


def main():
    _, b = reader('./e.in')
    writer(scaner(b))


if __name__ == '__main__':
    main()
