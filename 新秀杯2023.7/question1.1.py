# ！/usr/bin/nev python
# -*-coding:utf8-*-

import pandas as pd

# 读取数据
df = pd.read_excel(r'F:\Mathematical Modeling\新秀杯2023.7\B题：智慧医疗下的中医诊断\肺纤维化数据.xls',sheet_name='data1')

# 检验前5行数据是否引用正确
# print(df.head(5))

grouped = df.groupby(['中医诊断', '证型规范'])

for key, group in grouped:
    # 将逗号分隔的症状拆分成一个症状列表
    symptoms = []
    for symptoms_str in group['症状']:
        # print(symptoms_str)
        symptoms_split = symptoms_str.split('，')
        for symptom in symptoms_split:
            symptoms.append(symptom.strip())
    # 去除重复的症状并打印结果
    unique_symptoms = list(set(symptoms))
    print(f"中医诊断：{key[0]}, 证型规范：{key[1]}，对应症状：{unique_symptoms}")

