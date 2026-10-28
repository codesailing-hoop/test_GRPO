# 2026-10-28：从租服务器到训练环境检查

## 今天完成了什么

1. 查看单卡 GPU 服务器配置与按量价格。
2. 创建实例时遇到“当前主机存储库存已满”，更换主机后创建成功。
3. 最终租用的平台规格为 vGPU-48GB；驱动报告名称为 RTX 4090。
4. 通过 JupyterLab 终端检查 GPU、Python、PyTorch 和磁盘。
5. 创建 `grpo-code` 目录及 `data`、`models`、`outputs`、`logs` 子目录。
6. 创建复用系统包的虚拟环境，安装固定版本依赖并验证。

## 实际检查结果

```text
Python: 3.12.3
PyTorch: 2.8.0+cu128
PyTorch CUDA: 12.8
CUDA 可用: True
GPU: NVIDIA GeForce RTX 4090
显存: 47.37 GiB（PyTorch 报告）
计算能力: (8, 9)
支持 BF16: True
GPU 矩阵运算成功，结果形状: (256, 256)
```

固定依赖安装后的反馈：

```text
当前 Python: /root/autodl-tmp/grpo-code/.venv/bin/python
torch: 2.8.0+cu128
transformers: 4.56.2
datasets: 4.1.1
trl: 0.23.1
accelerate: 1.10.1
peft: 0.17.1
huggingface-hub: 0.35.3
GPU: NVIDIA GeForce RTX 4090
核心组件导入成功
No broken requirements found.
```

结果由学习者在远程服务器执行并反馈。尚未进行模型加载、生成、判题或 GRPO 更新。

## 今天理解的概念

- **显存与磁盘**：显存用于 GPU 计算，磁盘保存模型、数据和结果。
- **CUDA 两个版本**：`nvidia-smi` 显示驱动支持的最高版本，`torch.version.cuda` 显示 PyTorch 使用的版本，两者不要求相同。
- **BF16**：一种数值格式；相同数量的 BF16 数值所占空间是 FP32 的一半，但训练总显存还包含其他状态。
- **虚拟环境**：用于管理项目依赖；此次通过 `--system-site-packages` 复用镜像中的 PyTorch。
- **依赖检查的边界**：导入成功和 `pip check` 通过不代表完整训练已经验证。

## 下一步

- 保存完整环境快照。
- 检查 Hugging Face 访问情况，下载模型并记录 revision。
- 查看 DeepCoder 数据集的子集、划分、字段和测试格式。
- 在具备隔离判题环境后，测初始模型表现，再确定训练配置。

## 学习者补充

可在这里补充今天仍不理解的问题、操作心得和下一次要核实的内容。
