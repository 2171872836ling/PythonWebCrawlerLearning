import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
# 修改文件路径为原始字符串
file_path = 'student_habits_performance.csv'
try:
    df = pd.read_csv(file_path)
    print('数据加载成功')
    print(df.info())
    print(df.describe())
except FileNotFoundError:
    print(f'未找到文件: {file_path}')

# 图1: 每日学习时间直方图
plt.figure(figsize=(5, 3))
plt.hist(df['study_hours_per_day'], bins=20, color='skyblue', edgecolor='black')
plt.title('每日学习时间分布')
plt.xlabel('每日学习时间 (小时)')
plt.ylabel('学生数量')
plt.tight_layout()
plt.savefig('study_hours_histogram.png')
plt.show()

# 图5: 学生年龄与每日学习时间横向条形图
age_study_df = df.dropna(subset=['age', 'study_hours_per_day'])
age_study_avg = age_study_df.groupby('age')['study_hours_per_day'].mean().reset_index()

plt.figure(figsize=(3, 3))
# 使用 plt.barh 绘制横向条形图
plt.barh(age_study_avg['age'], age_study_avg['study_hours_per_day'], color='pink')
plt.title('学生年龄与每日学习时间条形图')
# 交换 x 轴和 y 轴的标签
plt.ylabel('学生年龄')
plt.xlabel('平均每日学习时间 (小时)')
plt.xticks([0, 1, 2, 3, 4])
plt.tight_layout()
plt.savefig('age_study_hours_bar_horizontal.png')
plt.show()

# 图2: 考试成绩与每日学习时间散点图
plt.figure(figsize=(5, 3))
sampled_df = df.iloc[::5]
plt.scatter(sampled_df['study_hours_per_day'], sampled_df['exam_score'], alpha=0.5, color='orange')
plt.title('考试成绩与每日学习时间关系')
plt.xlabel('每日学习时间 (小时)')
plt.ylabel('考试成绩')
plt.tight_layout()
plt.savefig('exam_score_vs_study_hours.png')
plt.show()

# 图3: 不同性别的平均考试成绩柱状图
gender_avg_score = df.groupby('gender')['exam_score'].mean().round(2)
plt.figure(figsize=(4, 3))
ax = gender_avg_score.plot(kind='bar', color=['#66b3ff','#99ff99'])
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')
plt.title('不同性别的平均考试成绩', fontsize=14)
plt.xlabel('性别', fontsize=12)
plt.ylabel('平均考试成绩', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('gender_avg_score.png')
plt.show()

# 图4: 睡眠时间分布箱线图
plt.figure(figsize=(5, 3))
box = plt.boxplot(df['sleep_hours'], showfliers=True, patch_artist=True)
# 设置箱体颜色
for patch in box['boxes']:
    patch.set_facecolor('lightblue')
medians = [median.get_ydata()[0] for median in box['medians']]
plt.text(1.1, medians[0], f'中位数: {medians[0]:.2f}', va='center')
plt.title('睡眠时间分布箱线图')
plt.ylabel('睡眠时间 (小时)')
plt.tight_layout()
plt.savefig('sleep_hours_boxplot.png')
plt.show()



# 图6: 心理健康评分与考试成绩的回归分析图
plt.figure(figsize=(5, 3))
sampled_data = df.iloc[::5]
sns.regplot(x='mental_health_rating', y='exam_score', data=sampled_data, scatter_kws={'alpha': 0.5})
plt.title('心理健康评分与考试成绩的回归分析')
plt.xlabel('心理健康评分')
plt.ylabel('考试成绩')
plt.tight_layout()
plt.savefig('mental_health_vs_exam_score.png')
plt.show()



#图7： 课堂出勤率与学生成绩折线图
sampled_df = df.dropna(subset=['attendance_percentage', 'exam_score']).iloc[::30]
sampled_df = sampled_df.sort_values(by='attendance_percentage')
grouped_data = sampled_df.groupby('attendance_percentage')['exam_score'].mean().reset_index()
plt.figure(figsize=(8, 5), dpi=300)
plt.plot(grouped_data['attendance_percentage'], grouped_data['exam_score'], marker='o')
plt.title('课堂出勤率与学生成绩关系')
plt.xlabel('出勤率百分比')
plt.xticks(rotation=45)
plt.ylabel('平均考试成绩')
plt.grid(True)
plt.savefig('attendance_vs_score.png', bbox_inches='tight')
plt.show()

# 图8: 学生兼职是否饼图
part_time_counts = df['part_time_job'].value_counts()
plt.figure(figsize=(3, 3))
plt.pie(part_time_counts, labels=part_time_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('学生是否兼职')
plt.axis('equal')  # 保证饼图是圆形
plt.tight_layout()
plt.savefig('part_time_job_pie.png')
plt.show()

# 图9: 学生兼职与考试成绩的热力图
# 假设 part_time_job 是分类变量，需要转换为数值类型
if df['part_time_job'].dtype == 'object':
    df['part_time_job'] = df['part_time_job'].astype('category').cat.codes

# 计算相关性矩阵
correlation_matrix = df[['part_time_job', 'exam_score']].corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('学生兼职与考试成绩的热力图')
plt.tight_layout()
plt.savefig('part_time_job_exam_score_heatmap.png')
plt.show()


# 图10: 每日社交媒体时间与学生成绩的气泡图
plt.figure(figsize=(4, 3))
# 假设数据集中有 'social_media_time' 和 'exam_score' 列
# 使用 'study_hours_per_day' 作为气泡大小
# 减少数据量，每隔 5 行取一行数据
sampled_df = df.iloc[::10]
# 处理缺失值
valid_df = sampled_df.dropna(subset=['social_media_hours', 'exam_score', 'study_hours_per_day'])
bubble_size = valid_df['study_hours_per_day'] * 50
plt.scatter(valid_df['social_media_hours'], valid_df['exam_score'], s=bubble_size, alpha=0.5, color='orange')
plt.title('每日社交媒体时间与学生成绩的气泡图')
plt.xlabel('每日社交媒体时间 (小时)')
plt.ylabel('学生成绩')
plt.tight_layout()
plt.savefig('social_media_exam_score_bubble.png')
plt.show()

fig = Figure()
canvas = FigureCanvas(fig)
renderer = canvas.get_renderer()
width, height = fig.canvas.get_width_height()
plt.close(fig)






