import csv, random
from my_package import my_tools

lista = []


def ramdom_info(n=100):
    subjects = ['python', 'java', 'c++', 'html']
    names = []
    for i in range(n // len(subjects)):
        name = my_tools.random_string(random.randint(3, 6))
        names.append(name)
    for i in range(n):
        subject = random.choice(subjects)
        score = random.randint(50, 100)
        lista.append([random.choice(names), subject, score])


def average():
    with open('data.csv', mode='r', encoding='utf-8') as f:
        # context = f.read()
        # print(context)
        cf = csv.reader(f)
        head = next(cf)  # 获取表头
        print('表头:', head)
        scores = []
        for i in cf:
            if len(i) == 0:
                continue
            print(i)
            scores.append(int(i[2]))
        return sum(scores) / len(scores)


def make_datas():
    with open('data.csv', mode='a', newline='', encoding='utf-8') as f:
        cf = csv.writer(f)
        # cf.writerow(['tom', 'c', '50'])
        ramdom_info()
        cf.writerows(lista)


# make_datas()
result = average()
print('大家的平均分是', round(result, 2))


