from analyser import Analyse


def my_analysis():
    wait_time = 10
    my_list = ['i', 'a', 'of', 'the', 'roman', 'empire']
    url = 'https://en.wikipedia.org/wiki/Roman_Empire'

    data = Analyse(url=url, alist=my_list, wait_time=wait_time)

    result = data.get_result()
    data.calculate_percentage()
    percentage_of_result = data.get_percentage()
    comments_analysed = data.get_number_of_comments_analysed()

    return result, percentage_of_result, comments_analysed


if __name__ == '__main__':
    comment_data = my_analysis()
    print(f'Comments analysis:\n{comment_data[0]}'
          f'\n\n'
          f'Percentage analysis:\n{comment_data[1]}'
          f'\n\n'
          f'Comments analyzed:\n{comment_data[2]}')