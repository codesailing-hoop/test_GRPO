# DeepCoder 0.5B GRPO 学习记录

从租用 GPU 服务器开始，逐步学习使用 DeepCoder-Preview-Dataset 对 0.5B 代码模型进行 GRPO 强化学习。记录实际操作、遇到的问题和验证结果，逐步形成可复现的教学项目。

> 当前阶段：服务器与 Python 依赖检查通过。尚未下载模型和数据，尚未开始训练，也没有训练效果结论。更新日期：2026-10-28。

## 实验目标

- 初始模型：[`Qwen/Qwen2.5-Coder-0.5B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-Coder-0.5B-Instruct)。
- 数据来源：[`agentica-org/DeepCoder-Preview-Dataset`](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset)。
- 框架：PyTorch、Transformers、TRL；生成语言以 Python 为起点。
- 学习闭环：题目 → 多个候选程序 → 隔离执行测试 → 奖励 → GRPO 更新 → 独立评估。
- 首轮先验证小规模流程，再根据实测成本和奖励信号决定训练规模。

这是一份个人学习与实验记录，不是 DeepCoder 官方模型的完整复现。是否使用 LoRA、序列长度、组内生成数量和奖励细节将在基线评估后确定。

## 进度

- [x] 租用单卡 GPU 实例并创建项目目录。
- [x] 检查 GPU、BF16 支持和小规模矩阵运算。
- [x] 创建复用系统 PyTorch 的虚拟环境。
- [x] 安装固定版本核心依赖，导入检查与 `pip check` 通过。
- [ ] 下载模型和数据，记录具体 revision。
- [ ] 检查数据字段、测试用例格式、重复题及训练/评估划分。
- [ ] 建立隔离判题环境并验证正确、错误、超时等情况。
- [ ] 评估初始模型，检查是否存在可学习的组内奖励差异。
- [ ] 完成 GRPO 小规模训练、保存与恢复。
- [ ] 在固定评估条件下比较训练前后结果。
- [ ] 整理教学说明和可复现实验报告。

## 已验证的服务器环境

以下来自学习者在远程服务器执行命令后的反馈，不是本地自动检测结果。

| 项目 | 记录 |
|---|---|
| 平台规格 | AutoDL，vGPU-48GB，单卡 |
| 驱动报告的 GPU 名称 | NVIDIA GeForce RTX 4090 |
| `nvidia-smi` 总显存 | 49140 MiB |
| PyTorch 报告的设备总显存 | 47.37 GiB |
| 计算能力 / BF16 | 8.9 / 支持 |
| Python | 3.12.3 |
| PyTorch / CUDA runtime | 2.8.0+cu128 / 12.8 |
| 驱动 / 驱动报告的最高 CUDA 版本 | 595.71.05 / 13.2 |
| 系统盘 / 数据盘 | 30G / 50G |

平台规格与驱动名称仅按观测记录，不据此推断底层硬件改造或资源独占方式。小运算成功不等于完整训练的稳定性和性能已经验证。

## 文件导航

- [环境配置步骤](SETUP.md)
- [2026-10-28 学习日志](LEARNING_LOG.md)
- [实验记录模板](EXPERIMENT_TEMPLATE.md)
- [固定核心依赖](requirements.txt)
- [环境检查脚本](check_environment.py)

## 使用范围

当前仓库只提供准备阶段的文档和检查脚本，没有可直接启动的 GRPO 训练程序。后续每完成一个阶段，再提交对应代码和实际结果。

原始数据、模型权重、检查点、缓存和连接凭据不提交到 Git。模型与数据的使用、再分发遵循各自上游条款。

## 参考资料

- [TRL 0.23.1 GRPOTrainer](https://huggingface.co/docs/trl/v0.23.1/grpo_trainer)
- [TRL 0.23.1 依赖声明](https://github.com/huggingface/trl/blob/v0.23.1/setup.cfg)
- [AutoDL 快速开始](https://www.autodl.com/docs/quick_start/)
- [PyTorch 历史版本安装说明](https://pytorch.org/get-started/previous-versions/)
