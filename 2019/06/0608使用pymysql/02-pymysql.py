from pymysql import connect


class JD(object):
    def __init__(self):
        conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jing_dong', charset='utf8')


    def show_all_items(self):
        '''显示所有的商品'''
        sql = 'select * from goods'
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)

    def run(self):
        while True:
            print('--------------京东----------------')
            print('1.所有的商品')
            print('2.所有的商品分类')
            print('3.所有的商品品牌分类')
            num = input('请输入功能对应的序号： ')
            if num == '1':
                # 查询所有分类
                self.show_all_items()
            elif num == '2':
                # 所有的商品分类
                pass
            elif num == '3':
                # 所有的商品品牌分类
                pass
            else:
                print('输入有误！')


def main():
    # 0. 创建一个京东对象
    jd = JD()

    # 调用这个对jd象的run方法
    jd.run()



if __name__ == '__main__':
    main()