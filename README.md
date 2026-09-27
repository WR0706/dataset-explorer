# dataset-explorer
A lightweight tool for automated descriptive statistics and visualization for data science EDA.

## 功能 - 支持终端描述性统计
- 自动识别数据类型（数值、类别、文本）
- 输出数值列统计（均值、中位数、标准差、缺失率等）
- 输出类别列统计（唯一值、众数、Top-N 频次）
- 终端 Rich 彩色表格美化输出
  
## 安装
pip install -e .

## 使用
python -m dsv examples/sample.csv
