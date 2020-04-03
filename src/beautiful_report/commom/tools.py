import os


def root_dir():
    root = os.path.dirname(__file__)
    while True:
        md_file = os.path.join(root, 'readme.txt')  # 以项目路径下的readme为依据，直到找找到
        if os.path.exists(md_file):  # 如果存在这个文件，root值已经是项目根目录
            break
        root = os.path.dirname(root)

    return root


def filepath(path):
    r = os.path.join(root_dir(), 'src/beautiful_report')
    file_path = os.path.join(r, path)
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


if __name__ == '__main__':
    print(root_dir())
    logs_path = filepath('logs')
    print(logs_path)
    #logfile_path = os.path.join(logs_path, 'app.log')

    #os.path.join(filepath('logs'),'app.log')
