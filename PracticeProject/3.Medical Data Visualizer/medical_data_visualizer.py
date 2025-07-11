import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3.Medical Data Visualizer
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.copy()
    df_cat = pd.melt(
        df_cat,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
    )


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar',
        height=5,
        aspect=1.2
    )

    # 8

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.copy()
    # 过滤异常值
    df_heat = df_heat[
        (df_heat['ap_lo'] <= df_heat['ap_hi']) &
        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
        (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
        (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
        (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
        ]
    # 重置索引
    df_heat = df_heat.reset_index(drop=True)


    # 12
    # 计算相关系数
    corr = df_heat.corr()

    # 13
    # 生成上三角的掩码
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    # Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    # 绘制热图
    sns.heatmap(
        corr,
        mask=mask,  # 应用掩码
        annot=True,  # 显示相关系数值
        fmt=".2f",  # 保留两位小数
        cmap="coolwarm",  # 颜色方案
        square=True,  # 使每个单元格为正方形
        linewidths=.5,  # 单元格之间的线宽
        cbar_kws={"shrink": .8},  # 调整颜色条大小
        ax=ax  # 指定绘图的轴
    )

    # 16
    fig.savefig('heatmap.png')
    return fig
