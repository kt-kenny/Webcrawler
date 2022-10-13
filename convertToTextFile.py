import ast
import time

def create_new():
    # file = "/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/final55393.txt"
    #
    # with open(file, 'r') as inputFile:
    #     temp = ast.literal_eval(inputFile.read())

    file = '/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/test2.txt'
    file3 = '/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/indexOfindex2.txt'
    student_score = {'Ritika': 5,
                     'Sam': 7,
                     'John': 10,
                     'Aadi': 8}
    counter = 1
    seek_position = 0
    with open(file, 'w') as newFile:
        for key, value in student_score.items():
            print(counter)
            out_text = key + " : " + str(value) + "\n"
            newFile.write(out_text)
            counter = counter + 1
            with open(file3, 'a') as index_file:
                index_file.write(key + " : " + str(seek_position) + '\n')
            seek_position = seek_position + len(out_text)


def create_new2():
    file = "/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/final55393.txt"

    input_file = open(file, 'r')
    print("before ast")
    temp = ast.literal_eval(input_file.read())
    print("after ast")
    input_file.close()

    file2 = '/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/test.txt'

    counter = 1
    seek_position = 0
    with open(file2, 'w') as newFile:
        for key, value in temp.items():
            print(counter)
            out_text = key + " : " + str(value) + "\n"
            newFile.write(out_text)
            counter = counter + 1
            with open(file3, 'a') as index_file:
                index_file.write(key + " : " + str(seek_position) + "\n")

            seek_position = seek_position + len(out_text)

def create_new3():
    file = "1500Split/index_subset_Sorted1500.txt"

    input_file = open(file, 'r')
    print("before ast")
    temp = ast.literal_eval(input_file.read()[11:-1])
    print("after ast")
    input_file.close()

    file2 = '/Users/kenny/Documents/cs121/Assignment3/testlbl.txt'
    counter = 1
    new_file = open(file2, 'w')
    for key, value in temp.items():
        if counter%1000 == 0:
            print(counter)
        out_text = "{" + "'" + key + "'" + " : " + str(value) + "}\n"
        new_file.write(out_text)
        counter = counter + 1

    new_file.close()

def create_new4():
    file = "/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/finalIndex.txt"
    file2 = '/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/indexOfindex.txt'

    input_file = open(file, 'r')
    index_file = open(file2, 'w')
    seek_position = 0
    print("start")
    for line in input_file:
        temp_dict = ast.literal_eval(line)
        for key, value in temp_dict.items():
            # print(key)
            # print(seek_position)
            index_file.write(key + " : " + str(seek_position) + "\n")
            seek_position = seek_position + len(line)

    input_file.close()
    index_file.close()

def seek_test(seek_position):
    file = "/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/finalIndex.txt"
    file2 = "/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/url1500.txt"
    input_file = open(file, 'r')

    urls = open(file2, 'r')

    input_file.seek(seek_position)
    temp = input_file.readline()
    list_of_urls = []
    temp_dict = ast.literal_eval(temp)
    for key, value in temp_dict.items():
        for item in value:
            list_of_urls.append(item[0])

    counter = 0
    for line in urls:
        first_word = int(line.split()[0])
        # print(first_word)
        if first_word in list_of_urls:
            counter = counter + 1
            # print(line.split()[1])
            if counter == 5:
                break
    print(counter)


def query_test():
    file1 = '/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/indexOfindex.txt'
    file2 = "/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/finalIndex.txt"

    indexOfindex = open(file1, 'r')

    print("cristina")
    query_term = "0"

    for line in indexOfindex:
        first_word = line.split()[0]
        if first_word == query_term:
            print(first_word)
            seek_position = int(line.split()[2])
            break
    return seek_position

if __name__ == "__main__":
    create_new3()


