import codecs


def read_file(input):
    """ Gets a file path and returns the formatted text in the file """
    data = codecs.open(input, 'r')
    return data.read()
    # with open(input, 'r') as template:
    #     data = template.read().replace('\n', ' ')
    # return data
