# 常见问题（FAQ）

本文回答使用本仓库时最常见的三个问题。完整命令行与 API 说明见 [usage.md](usage.md)，代码规范和提交约定见 [conventions.md](conventions.md)。

## 1. 怎么运行测试？

在仓库根目录运行全部 `test_*.py` 测试文件：

```sh
make test
```

`make test` 会依次运行每个测试文件，例如 `python3 test_stats.py`。`hello.sh` 的两种输出由单独的脚本验证：

```sh
./test.sh
```

运行环境需要 Python 3.9 或更高版本，只依赖标准库。已有测试描述的是契约，不要为了让新代码通过而修改；新行为请新增 `test_<模块>.py`。

## 2. 怎么在命令行计算一组数字的统计量？

至少传入一个数字，其余参数可以继续追加：

```sh
$ python3 stats.py 1 2 3 4
count=4 mean=2.50 median=2.50 spread=3.00

$ python3 stats.py 7
count=1 mean=7.00 median=7.00 spread=0.00
```

输出固定为 `count=<n> mean=<m> median=<d> spread=<s>`，三个小数保留两位。没有参数或某个参数无法解析为数字时，命令会把提示写到标准错误，并以退出码 `2` 结束。查看版本用 `python3 stats.py --version`。

## 3. 怎么在 Python 代码里调用这些函数、计算百分位数？

公共函数都从 `stats` 模块导入：

```python
from stats import mean, median, percentile, spread, summarize

mean([1, 2, 3, 4])          # 2.5
percentile([1, 2, 3, 4], 25)  # 1.75
summarize([1, 2, 3, 4])     # "count=4 mean=2.50 median=2.50 spread=3.00"
```

`percentile(values, p)` 使用线性插值，`p` 的取值范围是 0 到 100（含端点）。空列表、`p` 越界或其他非法输入会抛出 `ValueError`，错误消息中带有函数名。`stats` 是公共入口，内部实现拆分后 `from stats import <name>` 仍然可用。
