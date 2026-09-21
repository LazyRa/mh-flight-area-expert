# WorkBuddy Skills 合集

本仓库统一收集多个 WorkBuddy / Agent Skills 技能，每个技能放在各自独立的子文件夹中，互不干扰。

## 已收录技能

| 技能 | 说明 |
|---|---|
| [mh5001-2021-flight-area-standard](./mh5001-2021-flight-area-standard/) | 民用机场飞行区技术标准 MH5001-2021 主文 + 第一~第四修订案知识库（含 12 章摘要、术语表、评价流程、速查表与修订案覆盖登记） |

## 目录约定

```
workbuddy-skills/
├── README.md                        # 本文件（合集说明）
├── mh5001-2021-flight-area-standard/  # 技能 A（含 SKILL.md）
│   ├── SKILL.md
│   ├── chapters/
│   └── ...
└── <下一个技能>/                     # 技能 B（直接在此加子文件夹即可）
    └── SKILL.md
```

## 安装某个技能

克隆本仓库后，把对应技能的子文件夹（含其 `SKILL.md`）复制到 WorkBuddy 技能目录：

- Windows：`C:\Users\<用户名>\.workbuddy\skills\`
- macOS / Linux：`~/.workbuddy/skills/`

示例（安装 MH5001 技能）：

```bash
git clone https://github.com/LazyRa/workbuddy-skills.git
# 把 workbuddy-skills/mh5001-2021-flight-area-standard/ 复制到 ~/.workbuddy/skills/
```

重启 WorkBuddy 会话即可在技能列表中看到对应技能。

## 新增一个技能

1. 在本仓库根目录新建一个子文件夹（用技能 slug 命名，如 `my-new-skill/`）；
2. 放入 `SKILL.md` 及配套文件；
3. 在上方「已收录技能」表格补一行；
4. `git add -A && git commit && git push`。
