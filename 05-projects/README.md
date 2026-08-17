# 05 · 练习剧本（用角色来拼）

> 这里的「项目」是 **学习用练习剧本**，不是真实业务产品。  
> 本仓没有具体产品要交付；练习目的是：**用可复用角色拼场景**。

剧本**不再各自养一只大 Agent**。  
每个剧本只写三件事：**目标、材料、启用哪些角色**。

角色定义见 [04-roles](../04-roles/)。

## 练习清单

| 练习剧本 | 启用角色 | 你练什么 |
|----------|----------|----------|
| [A 知识库问答](./a-knowledge-qa.md) | `librarian` | 单角色 + 剧本材料 |
| [B 仓库变更摘要](./b-repo-digest.md) | `git-analyst` | 同一思路，换工具场景 |
| [C 学习大纲流水线](./c-outline-pipeline.md) | `researcher` → `editor` | 多角色组装 |
| [D 大纲加审查](./d-outline-with-review.md) | `researcher` → `editor` → `reviewer` | 跨场景复用审查员 |

## 项目说明书模板

```markdown
# 项目：xxx
## 目标
## 材料（上下文）
## 启用角色（Cast）
## 编排（谁先谁后）
## 验收
```

## 和旧习惯的差别

| 旧（按项目拆 Agent） | 新（按角色拆） |
|----------------------|----------------|
| `notes_agent` | 项目 A + 角色 `librarian` |
| `git_agent` | 项目 B + 角色 `git-analyst` |
| `outline_agent` | 项目 C + `researcher` + `editor` |

换题时优先问：**能否复用已有角色，只改项目上下文？**
