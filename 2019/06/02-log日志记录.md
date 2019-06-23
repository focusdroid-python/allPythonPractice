
    ****编码与解码****
    ```
        import urllib
        
        urllib.parse.quote('中国') // %E4%B8%AD%E5%9B%BD
        urllib.parse.unquote('%E4%B8%AD%E5%9B%BD') // 中国
    ```
### log日志级别
    > 0. DEBUG      详细信息，通常问题只出现在诊断问题上
    > 1. INFO       确认一切按照预期运行
    > 2. WARNING    一个迹象表明，一些意想不到的事情发生了，
    > 3. ERROR      更严重的问题，软件没能执行一些功能
    > 4. CRITICAL   严重错误，软件程序无法运行
    
   ```
        log.py
        import logging
        
        logging.basicConfig(
                            level=logging.WARNING,
                            filename='./log.txt',
                            filemode='w',
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:')
        
        logging.info('这是 logging info message')
        logging.debug('这是 logging debug message')
        logging.warning('这是 logging warning message')
        logging.error('这是 logging error message')
        logging.critical('这是 logging critical message')
   ```
   
### log日志像输出终端一样
    ```
        import logging
        
        # 第一步
        logger = logging.getLogger()
        logger.setLevel(logging.INFO) # log等级总开关
        
        # 第二步
        logfile = './log.txt'
        fh = logging.FileHandler(logfile, mode='a') # open的打开模式这里可以进行参考
        fh.setLevel(logging.DEBUG) # 输出到file的log总开关
        
        # 第三步: 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING) # 输出到console的log等级开关
        
        #第四步：定义hangler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        # 第五步
        logger.addHandler(fh)
        logger.addHandler(ch)
        
        logging.info('这是 logging info message')
        logging.debug('这是 logging debug message')
        logging.warning('这是 logging warning message')
        logging.error('这是 logging error message')
        logging.critical('这是 logging critical message')
        
    ```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       