# 项目 C · 学习大纲流水线

## 目标

输入主题，得到可放进 README 的 Markdown 大纲。

## 材料（项目上下文）

- 主题：如「AI Agent 入门」  
- 读者：初学者  
- 要点数量：5～8 条  

## 启用角色（Cast）

| 顺序 | 角色 | 卡 |
|------|------|----|
| 1 | 研究员 | [researcher](../04-roles/researcher.md) |
| 2 | 编辑 | [editor](../04-roles/editor.md) |

**不新建** `outline_agent`。大纲能力来自两个角色的组合。

## 编排

```
researcher（输出 bullets JSON） → editor（输出 Markdown 大纲）
```

中间必须是 JSON schema，不要用散文交接。

## 验收

1. 打印两段角色的原始输出（便于调试）  
2. 终稿有层级标题，并保留待确认问题（若有）  

## 可迁移

同一对角色：

- 主题改成「LangGraph 入门」→ 新大纲项目  
- 编辑的文稿类型改成「周报」→ 调研周报项目  

动的是**项目上下文**，不是角色本体。
