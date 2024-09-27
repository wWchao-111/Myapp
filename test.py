# import sys
# import getopt
# import fractions
#
# # def main(argv):
# #     try:
# #         opts, args = getopt.getopt(argv, "n:", "r:")
# #     # if(getopt.GetoptError):
# #     except getopt.GetoptError:
# #         print('Error:test.py -n <整数> -r <数值范围>')
# #         sys.exit(2)
# #     # print(getopt.GetoptError.args)
# #         # sys.exit(2)
# #     for opt, arg in opts:
# #         if opt == '-n':
# #             n = int(arg)
# #     print(n+1)
import pytest
from 11 import generate_expressions, evaluate, is_valid, random_fraction, random_expression

def test_random_fraction():
    # 测试生成的随机分数在范围内
    frac = random_fraction(10)
    assert 0 <= frac.numerator < 10
    assert frac.denominator > 0 and frac.denominator <= 10

def test_random_expression():
    # 测试随机生成的表达式
    expr = random_expression(10, 3)
    assert is_valid(expr)  # 应该是有效的表达式

def test_is_valid():
    # 测试合法性检查
    valid_expr = "1/2 + 1/3"
    invalid_expr = "1/2 - 3/4"
    assert is_valid(valid_expr)
    assert not is_valid(invalid_expr)

def test_evaluate():
    # 测试表达式的计算
    expr = "1/2 + 1/4"
    result = evaluate(expr)
    assert result == '3/4'  # 期望结果为 3/4

if __name__ == "__main__":
    pytest.main()




