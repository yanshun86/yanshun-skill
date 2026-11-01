# yanshun-skill

[![skills.sh](https://skills.sh/b/yanshun86/yanshun-skill)](https://skills.sh/b/yanshun86/yanshun-skill)
[![Version](https://img.shields.io/badge/version-0.1.0-2563EB.svg)](VERSION)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-16A34A.svg)](LICENSE)

言顺的经营判断工具箱。三个判断，可安装到 78 个 Agent 里直接用。

作者：言顺 · GitHub [@yanshun86](https://github.com/yanshun86) · X [@GYanshun53764](https://x.com/GYanshun53764)

---

## 这是什么

三个判断卡，来自一线的操盘和亏损，不是理论：

- 三年 358 单、644 万回款、峰值 40 人，**亏掉约 100 万**
- 3 个人、8 个月、**300 万以上毛利**，无应收款
- 0 → 2.5 亿 GMV，然后提前 316 天识别风险，**被欠薪 88,491 元**

这些卡是踩过之后留下的对照表。它们只做一件事：

> **把「我感觉不对劲」，变成「我知道该问哪三个问题」。**

没有课程，没有社群，没有后续销售。

---

## 适合谁

如果你符合下面任意一条，这套东西对你有用：

| 你是谁 | 你现在的状态 |
|:--|:--|
| **中小企业主 / 老板**（5–50 人，年流水 200 万–2000 万） | 有订单、有业务，但算不清这个月到底赚没赚 |
| **一人公司 / 自由职业者** | 每天很忙，忙的每一件都不会被拒绝，就是没有人付钱 |
| **创始人 / COO / 运营负责人** | 手上有一条在亏的业务，不敢停，也说不清在等什么信号 |
| **刚经历亏损的人** | 反复「再撑一下」，但说不出具体的积极信号是什么 |
| **商业顾问 / 教练 / 投资人** | 需要一套标准问题，快速判断别人的项目该不该继续 |

**一个共同点：你已经知道有问题，只是不知道该问什么。**

---

## 不适合谁

说实话，下面这些情况别装，装了也没用：

- 想找**商业计划书、定价方案、增长策略、财务测算**的人 —— 这工具只判断，不出方案
- 还没有任何业务、想从零找方向的人 —— 判断工具判断不了「做什么」，只能判断「要不要继续做」
- 需要**法务、财税、医疗**专业判断的人 —— 超出范围
- 想找流量投放、私域运营、内容模板的人 —— 这里没有

---

## 你会遇到什么问题，对应哪个工具

### 一、这个项目还要不要继续？

> 「我知道该停了，但已经投了这么多。」
> 「再撑一个月看看。」
> 「换别人早就撤了，我是不是太执拗？」

**用 `/ys-stop-loss`** —— 止损判断三问。

它帮你区分两件事：**你是在坚持，还是在重复错误。**

三问问完，你会得到一个指向动作的判断：继续、停、或者再用 X 周验证一件具体的事。

---

### 二、一直在做，做了很多，就是没结果

> 「我发了 100 条内容，一个询单都没有。」
> 「每天都在忙，但没有任何一件事推动生意。」
> 「我不知道问题出在内容、产品还是渠道。」

**用 `/ys-safe-vs-key`** —— 安全动作 vs 关键动作。

它帮你找出那个**唯一能让事情发生变化、但可能被拒绝**的动作。

大多数时候答案很具体：你回避的是报价，或者你回避的是给某个人打电话。

---

### 三、有业务有订单，账上却越来越紧

> 「这个月流水不错，怎么账上还是没钱？」
> 「工资开始晚发几天了。」
> 「我开始用信用卡补公司账户。」

**用 `/ys-cashflow-signals`** —— 现金流断裂前的中早期信号。

五个信号逐条对照，判断你现在处于**投入期**还是**消耗期**。

命中 2–3 条 = 需要在 30 天内做决定。命中 4–5 条 = 已经在断裂边缘。

---

## 预计带来什么帮助

**会得到：**

- 30 分钟内，把一个模糊的「不对劲」变成三个具体问题
- 一个指向动作的判断，不是一堆分析
- 在**还有余力的时候**做决定，而不是在断裂之后

**不会得到：**

- 商业计划书、定价方案、增长策略
- 「你一定行」「相信自己」这类话
- 替代你做决定 —— 判断给你，决定还是你下

> 这套东西的价值不在于它多聪明，在于它**不再让你合理化**。
> 你公司垮掉之前，信号出现过很多次。你都看见了，然后告诉自己「下个月就好了」。

---

## 安装

终端需要能运行 `npx`。

```bash
npx -y skills add yanshun86/yanshun-skill -g --all
```

- `-g` 全局安装（用户级）
- `--all` 装到本机所有支持的 Agent

**只装到某一个 Agent**，用 `-a` 指定：

```bash
npx -y skills add yanshun86/yanshun-skill -g -a claude-code
```

**想先看有什么，不装**：

```bash
npx -y skills add yanshun86/yanshun-skill -l
```

---

## 适配哪些 Agent

基于 `skills` CLI 的官方支持列表（78 个），已实测可装。

### 主流 Agent

| Agent | 安装标识 |
|:--|:--|
| **Claude Code** | `claude-code` |
| **Codex** | `codex` |
| **Cursor** | `cursor` |
| **Windsurf** | `windsurf` |
| **Cline** | `cline` |
| **Roo Code** | `roo` |
| **Gemini CLI** | `gemini-cli` |
| **GitHub Copilot** | `github-copilot` |
| **OpenCode** | `opencode` |
| **Warp** | `warp` |
| **Zed** | `zed` |
| **Kiro CLI** | `kiro-cli` |
| **Grok Build** | `grok` |
| **Amp / Replit** | `amp` / `replit` |

### 国内 Agent

| Agent | 安装标识 |
|:--|:--|
| **通义灵码（Lingma）** | `lingma` |
| **Qwen Code** | `qwen-code` |
| **Trae（字节）** | `trae` |
| **Trae CN** | `trae-cn` |
| **Qoder（阿里）** | `qoder` |
| **Qoder CN** | `qoder-cn` |
| **CodeBuddy（腾讯）** | `codebuddy` |
| **iFlow CLI（心流）** | `iflow-cli` |
| **Kimi Code CLI** | `kimi-code-cli` |
| **MiniMax Code** | `minimax-code` |
| **CodeArts Agent（华为）** | `codearts-agent` |
| **ZCode** | `zcode` |
| **Zencoder / Zenflow** | `zencoder` / `zenflow` |

### 其他

`AiderDesk` · `Antigravity` · `AstrBot` · `Augment` · `Continue` · `Crush` · `Devin` · `Droid` · `Goose` · `Junie` · `Kilo Code` · `OpenClaw` · `OpenHands` · `Qoder` · `Tabnine CLI` · `Trae` · `Neovate` · `Pochi` …… 共 78 个。

> Eve 和 PromptScript 不支持全局安装，只能装到单个项目目录。

---

## 如何使用

装完之后，在 Agent 对话里输入：

```
/ys
```

**直接把你的情况说出来，不用先选工具。**

比如：

> 我做了八个月的一条业务线，一直在亏，但我不敢停，因为停了这几个人怎么办。

`/ys` 会判断该用哪个工具，然后当场开始问。

---

### 也可以直接调用某个工具

| 输入 | 作用 |
|:--|:--|
| `/ys` | 不知道选哪个，先走这里 |
| `/ys-stop-loss` | 止损判断三问 |
| `/ys-safe-vs-key` | 安全动作 vs 关键动作 |
| `/ys-cashflow-signals` | 现金流断裂前的五个信号 |

---

### 它怎么问你

**一次问一个问题，不给你一张问卷。**

信息不够时，只问最影响判断的那一个。

需要你提供具体事实：**持续多久、亏了多少、发生了什么信号、谁在做什么**。

模糊的回答会被追问，比如「还好」「差不多」——这类回答在这套工具里不算答案。

---

## 更新

```bash
npx -y skills update -g
```

---

## 目录

```
skills/
  ys/                      主入口，负责选出该用哪个判断
  ys-stop-loss/            止损判断三问
  ys-safe-vs-key/          安全动作 vs 关键动作
  ys-cashflow-signals/     现金流断裂前的中早期信号
```

---

## 一句话

> 你不是不知道问题在哪。
>
> 你是知道，然后告诉自己再撑一下。
>
> 这三个工具不替你做决定，只负责让你没法再合理化。

---

## 版本

见 [VERSION](VERSION)。

## 许可证

[CC BY-NC 4.0](LICENSE) —— 可自由使用、修改、分发，不可商用。
