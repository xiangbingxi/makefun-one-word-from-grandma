# HANDOFF — One Word From Grandma

- 比赛：u-0xkianno-one-word-from-grandma-f04bed16（$5，截止北京时间 2026-11-27 03:05）
- 比赛页：https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16
- 仓库名：makefun-one-word-from-grandma

## 做法

- 拉 kit 解包，读 RULES.txt / competition.yaml 确认：程序写
  `/output/entry.txt`，UTF-8、1–30 字符、非空白；本场盲轮评比，
  评委两两比较，选更搞笑、更像奶奶会发的那个词。
- `main.py` 亲手写了两版：第一版只写词并跑通；第二版是真正的改进——
  写完后把 `/output/entry.txt` 读回来逐字节比对 ENTRY，一字不差
  才算成功，否则报错退出（exit 1）。
- 文案是用户让 GPT 写好、亲口说照原样交的，一字不改：`Knowitall`。
- `main.py` 不读外部文件、不联网，只写 `/output/entry.txt`。

## 文案 / 字符数

- 文案：`Knowitall`
- 字符数：9（1–30 字符门槛内）
- 字节数：9（纯 ASCII，UTF-8 无尾随换行）
- sha256：`4798706554ae2e0520d76699983b7a4ba494367d2b2b5d6ec629a179a7fb33f2`

## 校验结果

- 第一版 main.py：运行成功，输出 9 字节 `Knowitall`，无尾随换行。
- 第二版 main.py：连续跑两次，两次输出 `cmp` 逐字节一致。
- `prompt.txt`（9 字节）与 entry 输出逐字节一致。
- 注意：本机 `/output/entry.txt` 是多场投稿共用的路径，校验期间曾被
  其他场次的输出覆盖过一次；上面两次运行的比对是在同一条命令内
  写完即取、即比对的，结果可信。正式提交时以密封环境里跑出的
  `/output/entry.txt` 为准。

## 文件清单（repo/ 内 6 个文件）

- `main.py`（811 字节）
- `LICENSE`（MIT，含 SPDX-License-Identifier: MIT 行，1099 字节）
- `README.md`（投稿说明 + 比赛页链接 + 三枚官方徽章，1111 字节）
- `prompt.txt`（文案原文单行，9 字节）
- `.makefun/owner.json`（钱包 6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx，57 字节）
- `HANDOFF.md`（本文件）

未提交、未建 GitHub 仓、未碰 bundle。
