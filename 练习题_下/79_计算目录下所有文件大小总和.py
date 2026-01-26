# 编写一个程序，计算当前目录下所有文件的大小总和，并将结果以千字节(KB)为单位打印

from pathlib import Path

def get_file_size(directory):
    file_size = {}
    for file in Path(directory).rglob('*'):
        if file.is_file():
            file_size[file.name] = file.stat().st_size

    return file_size

print(get_file_size(''))