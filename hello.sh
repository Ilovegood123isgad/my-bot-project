#!/bin/sh
# 输出 hello；带名字参数时输出 hello <名字>。
if [ -n "${1:-}" ]; then
  echo "hello $1"
else
  echo hello
fi
