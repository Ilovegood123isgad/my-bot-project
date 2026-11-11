#!/bin/sh
# 验证 hello.sh 的两种输出：带名字参数和不带参数。
set -u

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
hello="$script_dir/hello.sh"
failures=0

assert_output() {
  expected=$1
  shift
  actual=$("$@" 2>&1)
  status=$?
  if [ "$status" -eq 0 ] && [ "$actual" = "$expected" ]; then
    printf 'PASS: %s -> %s\n' "$*" "$actual"
  else
    printf 'FAIL: %s -> expected "%s", got "%s" (exit %s)\n' \
      "$*" "$expected" "$actual" "$status" >&2
    failures=$((failures + 1))
  fi
}

assert_output "hello" "$hello"
assert_output "hello 小明" "$hello" 小明

if [ "$failures" -ne 0 ]; then
  printf 'FAILED: %s assertion(s) failed\n' "$failures" >&2
  exit 1
fi

echo "OK: all assertions passed"
