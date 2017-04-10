import re

#正则表达式demo
class RegexDemo:
    def __init__(self, pattern):
        self.pattern = pattern
    #匹配并打印匹配结果
    def print_reg(self, string):
        reg_obj = re.match(self.pattern, string)
        if reg_obj:
            print(reg_obj.string, '    |    ', self.pattern, '  |  ', string)
        else:
            print(False, '    |    ', self.pattern, '  |  ', string)

rd = RegexDemo(r'\d{3}\-\d{3,8}')
rd.print_reg('010-1234  010-123')