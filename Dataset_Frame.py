import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

movie_context = []
movie_url = ['https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297',
             'https://movie.naver.com/movie/bi/mi/basic.nhn?code=151153',
             'https://movie.naver.com/movie/bi/mi/basic.nhn?code=164101']

def movie_text(tmp):
    for addres in tmp:
        url = urlopen(addres)
        soup = BeautifulSoup(url, "html.parser")
        res = soup.find('p','con_tx').get_text()
        # movie_context.append(res)
    return res


if __name__ == '__main__':
    # url = urlopen("https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297")

    # url = urlopen("https://movie.naver.com/movie/bi/mi/basic.nhn?code=151153")
    # soup = BeautifulSoup(url, "html.parser")
    # soup_specific = soup.find_all('ul','top_thumb_lst')
    # res = soup.find('p','con_tx').get_text()
    # print(res)
    movie_text(movie_url)