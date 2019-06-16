def set_fun1(func):
    def callfunc():
        return '<a>' +func() +'</a>'
    return callfunc

def set_fun2(func):
    def cann_func():
        return '<td>'+func()+'</td>'
    return cann_func


@set_fun1
@set_fun2
def get_str():
    return '这是一个标题'


print(get_str())