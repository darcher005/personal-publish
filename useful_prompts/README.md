# useful_prompts

用来约束 AI 编码行为的核心规则文件（`AGENTS.md` / `CLAUDE.md` 形态），拿来即用。

## 文件清单

| 文件 | 来源 | 协议 | 解决什么问题 |
|---|---|---|---|
| [`karpathy-CLAUDE.md`](karpathy-CLAUDE.md) | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | ⚠️ 上游未声明许可证 | 让 AI 先想再写：别乱假设、别过度设计、改动要外科手术式、用可验证目标驱动 |
| [`ponytail-AGENTS.md`](ponytail-AGENTS.md) | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT | 让 AI 像"最懒的资深开发"：写代码前先爬七级决策阶梯，能复用/标准库/原生特性解决的就绝不新写 |
| [`ponytail-LICENSE`](ponytail-LICENSE) | 同上 | MIT | ponytail 的许可证全文（MIT 协议要求分发时随附） |

## 两者的区别与关系

- **karpathy-CLAUDE.md** 偏「过程纪律」：思考方式、改动边界、验收标准。出自 Andrej Karpathy 对 LLM 编码常见失误的观察。
- **ponytail-AGENTS.md** 偏「产出抑制」：一条明确的优先级阶梯，把"能不能不写"放在"怎么写"前面。
- **互补，不冲突**：可以两个一起用。karpathy 管"怎么想"，ponytail 管"写多少"。

## 怎么用

把对应文件拷到你目标项目的**根目录**，改名为宿主能识别的规则文件名即可：

| 宿主 | 目标文件名 |
|---|---|
| Claude Code | `CLAUDE.md` |
| 通用 / Codex / OpenCode | `AGENTS.md` |
| Cursor | `.cursor/rules/<name>.mdc` |
| Windsurf | `.windsurf/rules/<name>.md` |
| Cline | `.clinerules/<name>.md` |
| GitHub Copilot（编辑器） | `.github/copilot-instructions.md` |

两个文件也可以直接合并成一个 `AGENTS.md`（两份内容没有重复条目）。

## 溯源

本目录内容为对应上游仓库 `main` 分支的快照式拷贝，拷贝时间与源提交如下：

| 来源仓库 | 提交 |
|---|---|
| `multica-ai/andrej-karpathy-skills` | `2c606141936f` |
| `DietrichGebert/ponytail` | `e3ba2aa6f1e6` |

上游更新很快（ponytail 尤甚），需要最新版请回源仓库取。

## 版权说明

- ponytail 为 MIT 协议，已随附许可证全文，保留原作者署名。
- **`karpathy-CLAUDE.md` 的上游仓库未声明任何许可证**，严格来说默认"保留所有权利"。此处仅作个人学习用途的备份留存；如需在公开项目或商业场景使用，请先回上游确认授权。若介意，可直接删除该文件（保留 `ponytail-AGENTS.md` 即可，后者授权明确）。
