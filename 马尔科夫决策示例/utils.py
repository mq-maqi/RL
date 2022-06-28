def str_key(*args):
    """
    将 参 数 用"_"连 接 起 来 作 为 字 典 的 键， 需 注 意 参 数 本 身 可 能 会 是tuple或 者list型，
    比 如 类 似((a,b,c),d)的 形 式。
    :param args:
    :return:
    """
    new_arg = []
    for arg in args:
        if type(arg) in [tuple, list]:
            new_arg += [str(i) for i in arg]
        else:
            new_arg.append(str(arg))
    return "_".join(new_arg)


def set_dict(target_dict, value, *args):
    target_dict[str_key(*args)] = value


def set_prob(P, s, a, s1, p=1.0):  # 设 置 概 率 字 典
    set_dict(P, p, s, a, s1)


def get_prob(P, s, a, s1):  # 获 取 概 率 值
    return P.get(str_key(s, a, s1), 0)


def set_reward(R, s, a, r):  # 设 置 奖 励 值
    set_dict(R, r, s, a)


def get_reward(R, s, a):  # 获 取 奖 励 值
    return R.get(str_key(s, a), 0)


def display_dict(target_dict):  # 显 示 字 典 内 容
    for key in target_dict.keys():
        print("{}: {:.2f}".format(key, target_dict[key]))
        print("")


def set_value(V, s, v):  # 设 置 价 值 字 典
    set_dict(V, v, s)


def get_value(V, s):  # 获 取 价 值 字 典
    return V.get(str_key(s), 0)


def set_pi(Pi, s, a, p=0.5):  # 设 置 策 略 字 典
    set_dict(Pi, p, s, a)


def get_pi(Pi, s, a):  # 获 取 策 略 （概 率） 值
    return Pi.get(str_key(s, a), 0)
