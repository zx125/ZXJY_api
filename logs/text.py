class file_zx:
    def __init__(self,file_name,do):
        self.file_name = file_name
        self.do = do
        print('init')

    def __enter__(self):
        self.fw = open(self.file_name,self.do)
        print('entry')
        return self.fw

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.fw.close()

with file_zx('zx.log','w') as fw:
    fw.write('zxzxzx')
    print('over')