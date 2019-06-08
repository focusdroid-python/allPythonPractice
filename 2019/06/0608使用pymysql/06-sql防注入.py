from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)


    def show_all_items(self):
        '''显示所有的商品'''
        sql = 'select * from goods'
        self.execute_sql(sql)

    def show_cate_id(self):
        '''显示所有的商品分类'''
        sql = 'select * from goods_cates'
        self.execute_sql(sql)

    def show_brand_id(self):
        '''所有的商品品牌分类'''
        sql = 'select * from goods_brands'
        self.execute_sql(sql)

    def add_brands(self):
        '''添加商品分类'''
        item_name = input('输入新商品分类的名称： ')
        sql = '''insert into goods_brands (name) values("%s")'''% item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        '''注入防护'''
        find_name = input('请输入要查询的商品名称: ')
        # sql = '''select * from goods where name="%s";'''% find_name
        # print('------->%s<-----'% sql)
        # self.execute_sql(sql)
        sql = "select * from goods where name=%s"
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall())

    @staticmethod
    def print_menu():
        print('--------------京东----------------')
        print('1.所有的商品')
        print('2.所有的商品分类')
        print('3.所有的商品品牌分类')
        print('4.添加商品分类')
        return input('请输入功能对应的序号： ')


    def run(self):
        while True:
            num = self.print_menu()
            if num == '1':
                # 查询所有分类
                self.show_all_items()
            elif num == '2':
                # 所有的商品分类
                self.show_cate_id()
            elif num == '3':
                # 所有的商品品牌分类
                self.show_brand_id()
            elif num == '4':
                self.add_brands()
            elif num == '5':
                # "or 1=1 or"1 [数据全出来了]
                self.get_info_by_name()
            else:
                print('输入有误！')
                return


def main():
    # 0. 创建一个京东对象
    jd = JD()

    # 调用这个对jd象的run方法
    jd.run()



if __name__ == '__main__':
    main()