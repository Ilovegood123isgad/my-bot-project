# 项目约定（Code conventions）

这份文档是本仓库的**硬性约定**。任何提交在 review 时都按它检查。

## 1. 公共 API 的入口

- 公共函数通过 `stats` 模块暴露：调用方写 `from stats import percentile`。
- 允许重构内部布局（例如拆成包），但 `from stats import <name>` 必须继续可用。
- 每个模块必须定义 `__all__`，列出它对外暴露的名字。

## 2. 类型标注

所有公共函数的参数和返回值都必须有类型标注，使用 `list[float]` 这类内置泛型（本仓库 Python ≥ 3.9）。

## 3. 文档字符串

使用 reST 风格，包含一段摘要 + 字段列表：

```python
def percentile(values: list[float], p: float) -> float:
    """按线性插值计算第 p 百分位数。

    :param values: 非空的数值序列。
    :param p: 百分位，取值 0 到 100（含端点）。
    :return: 插值得到的百分位数。
    :raises ValueError: values 为空，或 p 不在 [0, 100] 内。
    """
```

## 4. 错误处理

- 非法输入一律抛 `ValueError`。
- 消息里必须带上函数名，例如 `"percentile() needs at least one value"`。

## 5. 测试

- 测试文件命名为 `test_*.py`，使用 `unittest`。
- **已有测试描述的是契约，不允许为了让新代码通过而修改它们。** 新行为请新增测试文件。
- 运行方式：`python3 test_stats.py`、`python3 test_<新模块>.py`。

## 6. 命令行

```
python3 stats.py <number> [<number> ...]
```

输出格式固定为：

```
count=<n> mean=<m> median=<d> spread=<s>
```

数值保留两位小数。改命令行行为时同步更新 README。

## 7. 提交

- 一个提交只做一件事。
- 提交信息用英文祈使句，首行不超过 72 字符。
