import pandas as pd  

# 读取Excel文件  
df = pd.read_excel('1.xlsx')  # 请替换为您的Excel文件名  

# 填充空的"所属世界"值(用前一个非空值填充)  
df['所属世界'] = df['所属世界'].fillna(method='ffill')  

# 获取所有唯一的"所属世界"值  
worlds = df['所属世界'].unique()  

# 打开文件准备写入  
with open('zombies.md', 'w', encoding='utf-8') as f:  
    # 为每个"所属世界"生成Markdown  
    for world in worlds:  
        f.write(f"### {world}\n")  
        f.write("| 中文名 | 对应类型 | 备注 |\n")  
        f.write("| ----------- | ----------- | ----------- |\n")  
        
        # 筛选当前"所属世界"的所有僵尸  
        world_df = df[df['所属世界'] == world]  
        
        # 为该世界的每个僵尸生成表格行  
        for _, row in world_df.iterrows():  
            chinese_name = row['中文名']  
            zombie_type = row['Zombietype英文名']  
            note = row['僵尸备注'] if pd.notna(row['僵尸备注']) else ''  
            f.write(f"| {chinese_name} | {zombie_type} | {note} |\n")  
        
        f.write("\n")  # 在每个世界之间添加一个空行  

print("Markdown已生成并保存到 zombies.md 文件中。")  