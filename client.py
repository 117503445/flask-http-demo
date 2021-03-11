from flask import json
from flask.globals import request
import requests
from requests.sessions import session
from requests_toolbelt.utils import dump


def dump_response(response):
    '''
    查看整个 HTTP 包,也可以用来观察其他请求的详情
    '''
    print(dump.dump_all(response).decode('utf-8'))


def basic_get():
    print('basic_get')

    response = requests.get('http://localhost:8080/')

    print(response.text)  # 查看返回的文本
    print()
    dump_response(response)
    print()


def rest():
    print('rest')
    sess = requests.session()  # 使用 session 效率更高

    # 创建 3 个 任务
    sess.post('http://localhost:8080/task', json={'title': 'sleep'})
    sess.post('http://localhost:8080/task', json={'title': 'run'})
    sess.post('http://localhost:8080/task', json={'title': 'study'})

    # 查询所有任务
    print(sess.get('http://localhost:8080/task').text)

    # 查询第 2 个 任务
    print(sess.get('http://localhost:8080/task/2').text)

    # 删除第 1 个 任务
    sess.delete('http://localhost:8080/task/1')

    # 修改第 2 个 任务
    sess.put('http://localhost:8080/task/2', json={'done': True})

    # 查询所有任务
    print(sess.get('http://localhost:8080/task').text)


def main():
    basic_get()
    rest()


if __name__ == '__main__':
    main()
