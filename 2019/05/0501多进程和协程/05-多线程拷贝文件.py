import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    '''完成文件的复制'''
    print('--------模拟copy文件： 从%s----> 到%s文件名是：%s' % (file_name, old_folder_name, new_folder_name))
    old_f = open(old_folder_name + '/' + file_name, 'rb')
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + '/' + file_name, 'rb')
    new_f.write(content)
    new_f.close()



def main():
    # 1. 获取文件夹的名称
    old_folder_name = input('请输入要拷贝的文件名： ')
    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(old_folder_name + "[复件]")
    except:
        pass

    # 3. 获取文件夹所有的待拷贝的文件名字
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 4。 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 向进程池中添加copy文件的人物
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))

    po.close()
    po.join()

    # 复制原来的文件，到新文件夹中的文件去

if __name__ == '__main__':
    main()