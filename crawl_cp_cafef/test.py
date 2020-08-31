ind = 0

class Test():
    
    def __init__(self):
        self.script = self.get_msg()

    def get_msg(self):
        global ind 
        ind += 1
        msg = "sdfsfasfafas{}".format(ind)
        return msg 
    
    def print_msg(self):
        print(self.script)


if __name__ =="__main__":
    test = Test()
    test.print_msg()