import os
from tqdm import tqdm


def split_file(file_path, num_splits):
    # 获取大文件的大小
    total_size = os.path.getsize(file_path)
    # 计算每个文件的大致大小（有时候会出现不能整除的问题）
    part_size = total_size // num_splits
    """
    如果大文件的大小不能被num_splits整除，比如大文件的大小是101，要分成10份也就是num_splits=10，那么part_size=101//10=10
    然而如果每一份小文件都是10，那么所有小文件的大小加起来是100，就跟大文件相比差了1，最终就没办法合成完整的大文件
    所以要考虑不能整除的时候，再刚刚那个情况计算得到的remain_size此时就是1
    """
    remain_size = total_size - part_size * num_splits
    """
    一个列表，你分成多少份，列表就有多少个元素，前面num_splits都是part_size，最后一个要考虑remain_size
    举个例子，大文件是101，要分成10份，计算得到part_size=10，remain_size是1，也就是说，
    每一个小文件的大小都是10，除了最后一个文件，最后一个小文件的大小是10+1=11，
    这样所有小文件的大小总和就和大文件的大小一样了。
    """
    each_size_list = [part_size for _ in range(num_splits - 1)] + [part_size + remain_size]
    # 打开大文件，准备读取
    with open(file_path, 'rb') as f:
        # for循环遍历，tqdm的作用是提供一个进度条，提高用户体验
        for i, each_size in enumerate(tqdm(each_size_list)):
            # 每一个小文件的文件名
            part_file = f'{file_path}_{i}'  # 创建小文件名称
            with open(part_file, 'wb') as p:
                p.write(f.read(each_size))


if __name__ == '__main__':
    # 将要被分割的大文件的路径
    file_path = "./projects/test.txt"
    split_file(file_path, 10)
