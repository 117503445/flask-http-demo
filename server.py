from flask import Flask, jsonify, request
from werkzeug.exceptions import abort
app = Flask(__name__)

# jsonify 将对象转为 JSON 格式的字符串


@app.route('/')
def hello_world():
    return 'Hello, World!'


tasks = []  # 储存任务清单的列表


@app.route('/task', methods=['GET'])
def read_all_tasks():
    return jsonify(tasks)


@app.route('/task/<int:id>', methods=['GET'])
def read_task(id):
    for task in tasks:
        if task['id'] == id:
            return jsonify(task)

    abort(404)  # 找不到 task 返回 404


@app.route('/task', methods=['POST'])
def create_task():
    js = request.get_json()

    js['id'] = get_new_task_id()
    js['done'] = False  # 新建的任务是 未完成的

    tasks.append(js)

    return 'created'  # 这个返回其实没有必要


@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    is_found = False
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            is_found = True

    if is_found:
        return 'deleted'  # 这个返回其实没有必要
    else:
        abort(404)  # 找不到 task 返回 404


@app.route('/task/<int:id>', methods=['PUT'])
def update_task(id):
    is_found = False
    for task in tasks:
        if task['id'] == id:

            js = request.get_json()
            for key in js:
                if key in task:
                    task[key] = js[key]
                else:
                    print(f'{key} is not allowd')

            is_found = True

    if is_found:
        return 'updated'  # 这个返回其实没有必要
    else:
        abort(404)  # 找不到 task 返回 404


def get_new_task_id():
    '''
    返回新任务的 id : 之前最后一个任务id + 1
    '''
    if len(tasks) == 0:
        # 如果还没有任务
        return 1

    return tasks[-1]['id'] + 1


def main():
    # HTTP 默认运行在 80 端口
    # 其实可以运行在别的端口上 如 8080
    app.run(port='8080')


if __name__ == '__main__':
    main()
