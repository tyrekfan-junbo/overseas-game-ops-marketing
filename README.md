# Overseas Game Ops Marketing Skill

[中文版本 / Chinese README](README.zh-CN.md)

一个用于海外手游运营发行工作的 Codex/Agent Skill。

它把“竞品调研、广告素材拆解、官方社媒分析、买量测试、渠道上架、运营数据需求、调研报告和公开包交付”沉淀成一套可复用流程，适合从一个新手游项目开始搭建海外运营方案。

## 适用场景

- 制定海外手游发行或运营方案
- 分析用户填写的竞品游戏素材和官方社媒
- 建立广告素材样本库、视频帧拆解、P0/P1/P2/Later 优先级体系
- 规划 X、Facebook、Instagram、TikTok、YouTube、Reddit 等社媒内容
- 设计 UA 买量测试方案、素材测试表、投放计划
- 明确 CPI、ROI、ROAS、留存、LTV 等运营指标和研发埋点需求
- 生成调研报告、营销方案、来源归档、图表和可外发静态包

默认按**移动端手游海外发行**处理，Steam/PC 信息默认归为 `Later`，除非当前项目明确进入 PC/Steam 阶段。

## 安装

把仓库复制到本地 skill 目录：

```powershell
git clone https://github.com/tyrekfan-junbo/overseas-game-ops-marketing.git C:\Users\admin\.codex\skills\overseas-game-ops-marketing
```

重启 Codex 后即可通过下面的方式触发：

```text
Use $overseas-game-ops-marketing to build an overseas mobile game operations plan.
```

## 快速开始

为一个新游戏项目创建标准工作区：

```powershell
python C:\Users\admin\.codex\skills\overseas-game-ops-marketing\scripts\init_ops_workspace.py "My Mobile Game" --out "D:\GameOps" --stage "first production" --competitors "Competitor Game A,Competitor Game B" --regions "US,JP,KR"
```

脚本会生成：

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

## 工作流

1. **产品和阶段判断**  
   明确项目当前处于 first production、alpha/beta、pre-OB/OB 或 version ops。

2. **来源归档**  
   先使用本地资料，再补充最新网络搜索；所有结论需要能追溯到 URL、本地文件、截图、视频帧、CSV/JSON 或图表。

3. **竞品和素材拆解**  
   按 P0/P1/P2/Later 分类素材，提取 Hook、首帧承诺、冲突、CTA、落地页承接和风险。

4. **官方社媒分析**  
   将 X、Instagram、Facebook、TikTok、YouTube、Reddit/Discord 拆成不同运营职责和内容栏目。

5. **UA 和数据需求**  
   将素材假设转化为测试单元，并明确 CPI、留存、ROAS/LTV、评论风险等指标。

6. **报告和公开包**  
   输出最终读者版本报告，不写过程痕迹；同步 HTML、图表、来源附录、CSV/JSON 和公开包。

## 目录结构

```text
.
├── SKILL.md
├── README.md
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
- 不在正式报告里写工具运行过程、修改痕迹或开发日志。
- 不用 CPI 单独判断素材质量。
- 不发布无法本地打开、来源缺失或编码损坏的公开包。

## 许可

当前仓库未声明开源许可证。对外复用或二次发布前，请先补充明确 LICENSE。
