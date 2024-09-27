import argparse
import random
import fractions
import cProfile


# 生成随机数
def random_fraction(max_denominator):
    return fractions.Fraction(random.randint(0, max_denominator-1), random.randint(1, max_denominator))


# 生成表达式
def random_expression(max_denominator, max_operators):
    operators = ['+', '-', '*']
    expression = str(random_fraction(max_denominator))
    for _ in range(random.randint(1, max_operators)):
        # 用空格分开，方便后续计算对表达式分割
        expression += ' ' + random.choice(operators) + ' ' + str(random_fraction(max_denominator))
    return expression


# 检查表达式合法性
def is_valid(expression):
    parts = expression.split()
    for i in range(2, len(parts), 2):
        if parts[i] == '-' and fractions.Fraction(parts[i-1]) < fractions.Fraction(parts[i+1]):
            return False
        if parts[i] == '/' and fractions.Fraction(parts[i+1]) == 0:
            return False
    return True


# 生成总表达式
def generate_expressions(n, max_denominator):
    expressions = set()
    while len(expressions) < n:
        expression = random_expression(max_denominator, 3)
        if is_valid(expression):
            expressions.add(expression)
    return expressions


# 计算
def evaluate(expression):
    parts = expression.split()  # 将表达式分隔
    result = fractions.Fraction(parts[0])  # 初始化第一个为分数

    for i in range(1, len(parts), 2):  # 每次取运算符
        operator = parts[i]
        # 读取exercise文件时会比自己生成的表达式多一个=符号
        if operator != '=':
            next_fraction = fractions.Fraction(parts[i + 1])  # 需要运算的数

        if operator == '+':
            result += next_fraction
        elif operator == '-':
            result -= next_fraction
        elif operator == '*':
            result *= next_fraction
        elif operator == '/':
            result /= next_fraction

    return result


# 比对答案
def grade(exercises, answers):
    correct = []
    wrong = []
    for i, (exercise, answer) in enumerate(zip(exercises, answers), 1):
        # print(f"{exercise}{answer}")
        if evaluate(exercise) == evaluate(answer):
            correct.append(i)
        else:
            wrong.append(i)
    return correct, wrong


def main():
    expressions = generate_expressions(10, 10)
    with open('Exercises.txt', 'w') as f:
        for expression in expressions:
            f.write(expression + ' =\n')
    with open('Answers.txt', 'w') as f:
        for expression in expressions:
            f.write(str(evaluate(expression)) + '\n')
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-n', type=int, help='number of exercises')
    # parser.add_argument('-r', type=int, help='range of values')
    # parser.add_argument('-e', type=str, help='exercise file')
    # parser.add_argument('-a', type=str, help='answer file')
    # args = parser.parse_args()
    #
    # if args.r is None and args.n is None and args.e is None and args.a is None:
    #     print("请输入参数")
    #     print("-n<题目数>")
    #     print("-r<数值范围>")
    #     print("-e<练习文件名>")
    #     print("-a<答案文件名>")
    #     return
    # elif args.r is None and args.n is not None or args.r is not None and args.n is None:
    #     print("-n<题目数>与-r<数值范围>需要同时出现")
    #     return
    # elif args.e is None and args.a is not None or args.e is not None and args.a is None:
    #     print("-e<练习文件名>与-a<答案文件名>需要同时出现")
    #     return
    # elif args.n is not None and args.r is not None:
    #     expressions = generate_expressions(args.n, args.r)
    #     with open('Exercises.txt', 'w') as f:
    #         for expression in expressions:
    #             f.write(expression + ' =\n')
    #     with open('Answers.txt', 'w') as f:
    #         for expression in expressions:
    #             f.write(str(evaluate(expression)) + '\n')
    #
    # if args.e is not None and args.a is not None:
    #     with open(args.e) as f:
    #         exercises = f.read().splitlines()
    #     with open(args.a) as f:
    #         answers = f.read().splitlines()
    #     correct, wrong = grade(exercises, answers)
    #     with open('Grade.txt', 'w') as f:
    #         f.write(f'Correct: {len(correct)} ({", ".join(map(str, correct))})\n')
    #         f.write(f'Wrong: {len(wrong)} ({", ".join(map(str, wrong))})\n')


if __name__ == '__main__':
    # cProfile.run('main()')
    main()