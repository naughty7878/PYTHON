import os
import qianfan

# 【推荐】使用安全认证AK/SK鉴权，通过环境变量初始化认证信息
# 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
os.environ["QIANFAN_ACCESS_KEY"] = "ccc54a8f56624f95b3fc6cce0f6e7113"
os.environ["QIANFAN_SECRET_KEY"] = "b532b0e2d39b438ba6862118ea573fd6"

chat_comp = qianfan.ChatCompletion()

# 指定特定模型
resp = chat_comp.do(model='ERNIE-3.5-8K', messages=[{
    "role": "user",
    "content": "python是什么"
}])

print(resp)
print(resp.code)
print(resp.headers)
print(resp.body)
print(resp.body['result'])
