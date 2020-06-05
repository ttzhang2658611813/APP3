import yaml

# with open("./data.yaml", "r", encoding="utf-8") as f:
#     data = yaml.safe_load(f)
#     print("类型", type(data))
#     print("值", data)

#
data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
with open("./www.yml","a") as f:
    yaml.safe_dump(data,f,encoding='utf-8',allow_unicode=True)