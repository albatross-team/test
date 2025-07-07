import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("F1 퀄리파잉 데이터")

df = pd.DataFrame({
    '선수': ['노리스', '르끌레르', '피아스트리', '해밀턴', '조지 러셀'],
    '퀄리파잉': ['1:03.971', '1:4.492', '1:4.554', '1:4.582', '1:4.762'],
    'Q_ULTIMATE':['1:03.971', '1:4.490', '1:4.296', '1:4.511', '1:4.733']
})

st.dataframe(df)

st.scatter_chart(df.set_index('선수')['퀄리파잉'])
st.scatter_chart(df.set_index('선수')['Q_ULTIMATE'])

# matplotlib으로 그래프 합치기
fig, ax1 = plt.subplots()

x = ['NOR', 'LEC', 'PIA', 'HEM', 'RUS'] # 선수
y1 =[63.971, 64.490, 64.296, 64.511, 64.733]  # 퀄_얼티메이트
y2 =[322.5, 321.1, 322.7, 321.3, 320.3] # 스피드_랩 (KH/M)

ax1.plot(x, y1,'.', color='green' ,markersize=7, label = '퀄_얼티메이트')
ax1.set_xlabel('선수')
ax1.set_ylabel('Q_ULTIMATE(S)')
ax1.tick_params(axis='both', direction='in')

ax2 = ax1.twinx()
ax2.plot(x, y2, '.', color='deeppink', markersize=7, label = '스피드_랩 (KH/M)')
ax2.set_ylabel('SPEED_LAP (KH/M)')
ax2.tick_params(axis='y', direction='in')

# plt.show()
st.pyplot(fig)


# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# st.title("F1 퀄리파잉 데이터")

# def time_to_seconds(time_str):
#     if isinstance(time_str, str):
#         parts = time_str.split(':')
#         minutes = float(parts[0])
#         seconds = float(parts[1])
#         return minutes * 60 + seconds
#     return time_str 

# df = pd.DataFrame({
#     '선수': ['노리스', '르끌레르', '피아스트리', '해밀턴', '조지 러셀'],
#     '퀄리파잉': ['1:03.971', '1:04.492', '1:04.554', '1:04.582', '1:04.762'],
#     '퀄얼티메이트':['1:03.971', '1:04.490', '1:04.296', '1:04.511', '1:04.733'],
#     '스피드랩 (KH/M)': [322.5, 321.1, 322.7, 321.3, 320.3] 
# })


# df['퀄리파잉_초'] = df['퀄리파잉'].apply(time_to_seconds)
# df['퀄얼티메이트초'] = df['퀄얼티메이트'].apply(time_to_seconds)

# st.dataframe(df)

# st.subheader("Streamlit 기본 Scatter Chart")


# st.write("퀄리파잉 시간 (초):")
# st.scatter_chart(df.set_index('선수')['퀄리파잉초'])

# st.write("퀄얼티메이트 시간 (초):")
# st.scatter_chart(df.set_index('선수')['퀄얼티메이트초'])


# st.subheader("Matplotlib으로 퀄얼티메이트 시간과 스피드랩 합치기")


# fig, ax1 = plt.subplots(figsize=(10, 6)) 

# ax1.plot(df['선수'], df['퀄얼티메이트_초'], 'o-', color='green', markersize=7, label='퀄 얼티메이트 시간 (초)')
# ax1.set_xlabel('선수')
# ax1.set_ylabel('퀄 얼티메이트 시간 (초)', color='green')
# ax1.tickparams(axis='y', labelcolor='green')
# ax1.grid(True, linestyle='--', alpha=0.6) 


# ax2 = ax1.twinx()
# ax2.plot(df['선수'], df['스피드랩 (KH/M)'], 'x--', color='deeppink', markersize=7, label='스피드랩 (KH/M)')
# ax2.set_ylabel('스피드랩 (KH/M)', color='deeppink')
# ax2.tick_params(axis='y', labelcolor='deeppink')


# lines, labels = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# plt.title('선수별 퀄 얼티메이트 시간 및 스피드랩')
# fig.tight_layout()

# st.pyplot(fig)
