import os
import qianfan


def gpt(question):
    # 【推荐】使用安全认证AK/SK鉴权，通过环境变量初始化认证信息
    # 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
    os.environ["QIANFAN_ACCESS_KEY"] = "xxx"
    os.environ["QIANFAN_SECRET_KEY"] = "xxx"

    chat_comp = qianfan.ChatCompletion()

    print('question', question)
    # 指定特定模型
    resp = chat_comp.do(model='ERNIE-3.5-8K', messages=[{
        "role": "user",
        "content": question
    }])
    print(resp)
    print(resp.code)
    print(resp.headers)
    print(resp.body)
    return resp.body['result']


# result = gpt('你好')
# print(result)
