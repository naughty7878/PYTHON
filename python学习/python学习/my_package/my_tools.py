import random, re, time


def random_char(upper=True):
    if upper:
        t = random.randint(ord('A'), ord('Z'))
        return chr(t)
    else:
        t = random.randint(ord('a'), ord('z'))
        return chr(t)


def random_string(length):
    s = ''
    for j in range(length):
        s += random_char(random.choice([True, False]))
    return s


def yan_zheng_ma(length):
    return random_string(length)


def is_phone_number(phone):
    # 手机号
    result = re.match(r'^1\d{10}$', phone)
    if result is None:
        return False
    return True


def get_time():
    t = time.localtime()
    s = time.strftime('%Y-%m-%d %H:%M:%S', t)
    return s


def main():
    a = []
    for i in range(4):
        a.append(random_string(random.randint(3, 6)))
    return a

# print(main())
# print(yan_zheng_ma(8))
