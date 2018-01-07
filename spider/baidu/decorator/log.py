def log(f):
    def decorator(*args, **kwargs):
        print('--------类:{},方法:{}开始执行---------'.format(f.__module__, f.__name__))
        r = f(*args, **kwargs)
        print('--------类:{},方法:{}执行完成---------'.format(f.__module__, f.__name__))
        return r

    return decorator
