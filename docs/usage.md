# stats 使用文档

本文说明 `stats.py` 的命令行用法、公共 API 和测试运行方式。代码风格和提交约定见 [conventions.md](conventions.md)。

## 环境要求

- Python 3.9 或更高版本（见 [conventions.md](conventions.md)）。
- 只使用 Python 标准库，不需要安装第三方依赖。
- 下面的命令都在仓库根目录执行。

## 命令行用法

### 基本用法

```
python3 stats.py <number> [<number> ...]
```

至少传入一个数字，可以传入多个。每个参数都交给 `float()` 解析，因此整数、小数、负数和科学计数法（如 `1e3`）都可以。

命令行没有选项开关；任何参数都会被当作数字解析，例如 `--help` 不是受支持的选项，会解析失败并以退出码 2 结束。

### 输出格式

成功时在标准输出打印一行摘要，格式固定为：

```
count=<n> mean=<m> median=<d> spread=<s>
```

| 字段 | 含义 | 格式 |
| --- | --- | --- |
| `count` | 参数个数 | 整数，不补小数 |
| `mean` | 算术平均值 | 保留两位小数 |
| `median` | 中位数 | 保留两位小数 |
| `spread` | 极差（最大值减最小值） | 保留两位小数 |

三个小数值都用 `:.2f` 格式化，输出中字段之间各有一个空格。

### 退出码

| 退出码 | 含义 |
| --- | --- |
| `0` | 成功，已打印摘要 |
| `2` | 用法错误，未打印摘要 |

用法错误有两种，错误信息都写到标准错误：

| 情形 | 标准错误输出 |
| --- | --- |
| 没有提供参数 | `usage: python3 stats.py <number> [<number> ...]` |
| 有参数不能解析为数字 | `every argument must be a number` |

只要有任意一个参数无法解析为数字，整个命令就失败，不会输出部分结果。

脚本通过 `raise SystemExit(main(sys.argv[1:]))` 启动，因此进程退出码就是 `main` 的返回值。

### 示例

```
$ python3 stats.py 1 2 3 4
count=4 mean=2.50 median=2.50 spread=3.00

$ python3 stats.py 7
count=1 mean=7.00 median=7.00 spread=0.00

$ python3 stats.py
usage: python3 stats.py <number> [<number> ...]

$ python3 stats.py 3 oops
every argument must be a number
```

后两个示例的提示信息输出到标准错误，退出码都是 2。

## 公共 API

公共函数都从 `stats` 模块导入：

```python
from stats import main, mean, median, spread, summarize
```

签名中的类型标注用于说明用法，Python 运行时不会检查，传入整数列表同样可用。

### `mean`

```python
mean(values: list[float]) -> float
```

- 参数 `values`：非空的数值序列。
- 返回：算术平均值 `sum(values) / len(values)`。
- 异常：`values` 为空时抛出 `ValueError`，消息为 `mean() needs at least one value`。

示例：`mean([1, 2, 3, 4])` 返回 `2.5`。

### `median`

```python
median(values: list[float]) -> float
```

- 参数 `values`：非空的数值序列，顺序不限；函数会先排序，不会修改传入的列表。
- 返回：中位数。元素个数为奇数时取排序后的中间值；为偶数时取中间两个值的平均值。
- 异常：`values` 为空时抛出 `ValueError`，消息为 `median() needs at least one value`。

示例：`median([3, 1, 2])` 返回 `2`，`median([1, 2, 3, 4])` 返回 `2.5`，`median([10, 2, 8, 4])` 返回 `6`。

### `spread`

```python
spread(values: list[float]) -> float
```

- 参数 `values`：非空的数值序列。
- 返回：极差，即 `max(values) - min(values)`；只有一个元素时返回 `0`。
- 异常：`values` 为空时抛出 `ValueError`，消息为 `spread() needs at least one value`。

示例：`spread([4, 1, 9])` 返回 `8`，`spread([5])` 返回 `0`。

### `summarize`

```python
summarize(values: list[float]) -> str
```

- 参数 `values`：非空的数值序列。
- 返回：与命令行输出格式相同的一行字符串 `count=<n> mean=<m> median=<d> spread=<s>`，其中 `count` 是元素个数，其余三个值保留两位小数。
- 异常：`values` 为空时抛出 `ValueError`，消息为 `mean() needs at least one value`；该异常由内部调用的 `mean()` 抛出。

示例：`summarize([1, 2, 3, 4])` 返回 `"count=4 mean=2.50 median=2.50 spread=3.00"`。

### `main`

```python
main(argv: list[str]) -> int
```

- 参数 `argv`：命令行参数列表，不含程序名；命令行入口传入的是 `sys.argv[1:]`。
- 返回：`int` 退出码。`0` 表示成功，`2` 表示用法错误。
- 行为：
  - `argv` 非空且每个元素都能解析为数字时，把 `summarize(values)` 打印到标准输出并返回 `0`。
  - `argv` 为空时，把用法提示打印到标准错误并返回 `2`。
  - 有元素无法解析为数字时，把 `every argument must be a number` 打印到标准错误并返回 `2`。
- 异常：对 `list[str]` 输入，用法错误通过返回值 `2` 表示，不会抛出异常。

示例：`main(["1", "2", "3", "4"])` 打印 `count=4 mean=2.50 median=2.50 spread=3.00` 并返回 `0`；`main([])` 和 `main(["3", "oops"])` 都返回 `2`。

## 运行测试

在仓库根目录执行：

```
python3 test_stats.py
```

- 测试使用标准库 `unittest`，当前包含 12 个测试用例。
- 全部通过时退出码为 `0`，输出以 `OK` 结尾；有失败时退出码非 `0`，并给出失败详情。
- 测试输出写到标准错误，这是 `unittest` 的默认行为。

按 [conventions.md](conventions.md) 的约定，测试文件命名为 `test_*.py`；已有测试描述的是契约，不应为了让新代码通过而修改，新行为请新增测试文件 `test_<新模块>.py`，并用 `python3 test_<新模块>.py` 运行。
