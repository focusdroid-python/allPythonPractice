from pymysql import *

def main():
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jing_dong', charset='utf8')

    conn

    print('*'*50)
    print(conn)
    print('*' * 50)
if __name__ == '__main__':
    main()