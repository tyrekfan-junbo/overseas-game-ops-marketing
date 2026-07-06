# 海外手游运营营销 Skill

这是一个用于海外手游运营、发行、买量和调研报告制作的 Codex/Agent Skill。

它把一整套工作流程沉淀为可复用方法：搜索信息、来源归档、竞品研究、广告素材拆解、官方社媒运营分析、买量测试、渠道上架、运营数据指标、调研报告和公开包交付。

## 适用场景

- 为新手游项目制定海外发行和运营方案
- 分析用户填写的竞品游戏广告素材、官方社媒和买量打法
- 建立广告素材样本库、视频帧素材库、来源归档和样本表
- 拆解 Meta、TikTok、YouTube、X、Reddit、Facebook、Instagram 等渠道内容
- 设计 UA 买量测试方案、素材测试表和投放计划
- 明确 CPI、CTR、CVR、CPA、ROI、ROAS、留存、LTV 等运营指标和研发埋点需求
- 生成调研报告、营销方案、图表、来源附录和可外发静态包

默认按**移动端手游海外发行**处理。Steam/PC 资料默认归为 `Later`，除非项目已经进入 PC/Steam 阶段。

## 安装方式

将仓库克隆到本地 skill 目录：

```powershell
git clone https://github.com/tyrekfan-junbo/overseas-game-ops-marketing.git C:\Users\admin\.codex\skills\overseas-game-ops-marketing
```

重启 Codex 后，可用下面的方式触发：

```text
Use $overseas-game-ops-marketing to build an overseas mobile game operations plan.
```

## 快速创建项目工作区

```powershell
python C:\Users\admin\.codex\skills\overseas-game-ops-marketing\scripts\init_ops_workspace.py "My Mobile Game" --out "D:\GameOps" --stage "first production" --competitors "Competitor Game A,Competitor Game B" --regions "US,JP,KR"
```

生成内容包括：

- `project_brief.md`
- `samples/source_inventory.csv`
- `samples/creative_samples.csv`
- `samples/social_ops_samples.csv`
- `samples/ua_test_plan.csv`
- `samples/ops_metrics_requirements.csv`
- `samples/report_sources.csv`
- `sources/`
- `charts/`
- `reports/`
- `exports/public_package/`

## 核心工作流

1. **产品与阶段判断**  
   明确项目处于 `first production`、`alpha/beta`、`pre-OB/OB` 还是 `version ops`。

2. **来源归档**  
   优先读取本地归档，再补充实时搜索。所有结论都要能追溯到 URL、本地文件、截图、视频帧、CSV/JSON 或图表。

3. **竞品与素材拆解**  
   按 `P0/P1/P2/Later` 分类素材，提取 Hook、首帧承诺、冲突、CTA、落地页承接、真实玩法风险和用户情绪风险。

4. **官方社媒运营分析**  
   将 X、Instagram、Facebook、TikTok、YouTube、Reddit/Discord 拆成不同运营职责和内容栏目。

5. **UA 买量与数据需求**  
   将素材假设转化为测试单元，并明确 CTR、CPI、CVR、CPA、ROAS、留存、LTV、评论风险等指标。

6. **报告与公开包交付**  
   输出最终读者版本报告，不写过程痕迹；同步 HTML、图表、来源附录、CSV/JSON 和公开包。

## 可直接复制的买量数据分析 Prompt

这段 Prompt 可直接用于让 AI 分析广告投放数据，适合贴在报表、CSV、Excel 数据之后使用。

```text
请你扮演一名游戏买量优化师，基于下面这份投放数据，帮我完成4件事：

第一，计算核心指标：CTR、CPC、CPM、CVR、CPA、付费率、ROAS。

第二，找出表现最好和最差的 Campaign、国家和素材。

第三，判断主要问题出现在点击、转化、付费还是回收。

第四，给出下一步优化动作，分成“立即处理 / 继续观察 / 需要补数据验证”。

注意：不能只看单一指标，要结合消耗量、转化量、样本量和 ROI/ROAS 一起判断。
```

建议输入数据至少包含：

- Campaign
- 国家 / 地区
- 素材 ID 或素材名称
- 展示量
- 点击量
- 消耗
- 安装量或注册量
- 付费人数
- 付费金额 / 收入

如果数据缺少收入、付费人数、安装量等关键字段，需要先标记为“需要补数据验证”，不要强行得出 ROAS 或付费率结论。

## 目录结构

```text
.
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── metrics-and-tracking.md
│   ├── report-style.md
│   ├── sample-schemas.md
│   └── workflow-detail.md
├── scripts/
│   └── init_ops_workspace.py
└── test-prompts.json
```

## 重要边界

- 不把竞品 CPI、ROI、ROAS、留存或 LTV 当成本游戏真实数据。
- 不把 Steam/PC 素材混入当前移动端首发判断。
- 不在正式报告中写工具运行过程、修改痕迹或开发日志。
- 不用 CPI 单独判断素材质量。
- 不发布无法本地打开、来源缺失或编码损坏的公开包。

## 许可证

当前仓库未声明开源许可证。对外复用或二次发布前，请先补充明确 LICENSE。
