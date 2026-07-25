# 04 · 角色库（可复用）

这里只定义 **角色（Role）**，不绑定具体项目。

项目去 [05-projects](../05-projects/) 里「选用角色 + 填项目上下文」。

## 节奏提醒

```
角色卡（本目录） → 项目剧本（05-projects） → 运行
```

## 角色清单

| 角色 | 文件 | 一句话职责 |
|------|------|------------|
| 图书管理员 | [librarian.md](./librarian.md) | 只读笔记并引用回答 |
| Git 分析员 | [git-analyst.md](./git-analyst.md) | 只读 git，总结变更 |
| 研究员 | [researcher.md](./researcher.md) | 收集要点，输出 JSON |
| 编辑 | [editor.md](./editor.md) | 把要点编成结构化文稿 |
| 审查员 | [reviewer.md](./reviewer.md) | 挑错与风险，不直接改产物 |

## 角色卡必备字段

每张卡都按同一模板，方便换项目时只改「项目上下文」：

1. **职责**（做什么 / 不做什么）  
2. **工具权限**  
3. **输入**  
4. **输出**（最好有 schema）  
5. **停止条件**  

## 怎么用到项目里

```text
项目：学习大纲
启用角色：researcher → editor
项目上下文：主题=「AI Agent 入门」，语言=中文，读者=初学者
```

不要新建 `outline_agent`。  
复用 `researcher` + `editor`，只换主题即可去做「周报大纲」「课程大纲」。
