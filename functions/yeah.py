from csv import writer


def save(title, line):
    with open(title , 'a', newline='') as data:
        writer_object = writer(data, delimiter=',')
        writer_object.writerow(line)
        data.close()