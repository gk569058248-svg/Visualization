import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# 设置环境变量，避免PIL错误
# os.environ['STREAMLIT_WATCHER_TYPE'] = 'none'

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

st.title("生成磁场强度随时间变化图")
upload_file = st.file_uploader("上传数据文件", type=["txt"])
if upload_file:
    df = pd.read_csv(upload_file, sep=r'\s+', skiprows=1, header=None, encoding='gbk')
    time = df[0]
    mag = df[1]
    fig, ax = plt.subplots()
    ax.plot(time, mag)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Magnetic Field Intensity (pT)")
    ax.set_title("Time VS. Magnetic Field Intensity")
    st.pyplot(fig)
