# 项目 D · 大纲 + 审查（演示角色复用）

## 目标

在项目 C 基础上增加质量门禁：成稿须过审查员。

## 材料

同项目 C，另加检查清单：

- 是否适合初学者  
- 是否冒充事实  
- 结构是否只有一层废话标题  

## 启用角色（Cast）

```
researcher → editor → reviewer
```

审查员卡：[reviewer](../04-roles/reviewer.md)

注意：`reviewer` 也可原样用于「审查 PR」「审查客服话术」——这就是**角色跨项目**。

## 编排

1. 研究员出 JSON  
2. 编辑出 Markdown  
3. 审查员出 `verdict` + `issues`  
4. 若 `request_changes`，可让编辑按 issues 改一版（最多 1 轮，防抬杠）  

## 验收

- 终局有审查 JSON  
- 高优先级问题为零，或明文列出仍未解决项  

## 你应体会到的节奏

```
角色库稳定（04-roles）
    ↑ 复用
项目剧本变（本文件只改 Cast 与材料）
```
