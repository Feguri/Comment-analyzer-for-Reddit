from analyser import Analyse


def my_analysis():
    wait_time = 15
    my_list = ['is', 'not', 'hi', 'i', 'the']
    url = 'https://www.reddit.com/r/memes/comments/ogvdkn/maybe_in_10_years_time/'
    path = rf'C:\Users\Acer\Desktop\Development\chromedriver.exe'

    data = Analyse(url=url, alist=my_list, wait_time=wait_time, path=path)

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
