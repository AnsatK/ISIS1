import re 

test_string = "dabssdjiwejw;abbfbj;cneodkwedjffnjawfhawe;i3 doepwdkw eekdwkd"

reg = "ab{2,3}"
m = re.search(reg, test_string)
print(m)