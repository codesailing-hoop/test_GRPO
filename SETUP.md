# 环境准备

## 已验证的路径

实验运行在远程 Linux GPU 服务器。以下命令不要在本地 macOS 中执行。已使用镜像中的 Python 3.12.3 和 PyTorch 2.8.0+cu128；系统发行版尚待记录。

项目目录：`/root/autodl-tmp/grpo-code`。模型、数据和训练输出放在数据盘。

```bash
mkdir -p /root/autodl-tmp/grpo-code/{data,models,outputs,logs}
cd /root/autodl-tmp/grpo-code
python -m venv --system-site-packages .venv
source .venv/bin/activate
which python
```

`--system-site-packages` 复用镜像已有的 PyTorch，也会使系统中的其他 Python 包可见。因此这不是完全隔离的环境；复现时应同时记录镜像和系统包。

每次新开终端，重新执行：

```bash
cd /root/autodl-tmp/grpo-code
source .venv/bin/activate
```

## 安装与检查

将仓库中的 `requirements.txt` 放到项目目录后执行：

```bash
python -m pip install --no-cache-dir -r requirements.txt
python -m pip check
```

此配置以镜像中已有 `torch==2.8.0+cu128` 为前提。如果从全新 Linux 环境安装，需要先参考 [PyTorch 官方说明](https://pytorch.org/get-started/previous-versions/#v280)，从对应 CUDA wheel 源安装 PyTorch。

如果已将 `check_environment.py` 复制到项目目录，可以执行：

```bash
python check_environment.py
```

该脚本用于将前期手工检查整理为可重复运行的步骤。初次成功检查来自学习者手动执行的等价命令；此仓库脚本尚待在服务器运行。

## 保存完整环境快照

核心依赖已固定；传递依赖尚未形成完整锁定。下一步可在服务器执行以下命令，将实际安装状态留存到本地日志目录：

```bash
python -m pip freeze > logs/environment-freeze.txt
python -m pip check > logs/pip-check.txt
```

日志目录默认不提交。公开分享环境快照前检查其中是否存在私人路径、私有软件源或其他个人配置。

## 数据与实验约束

- 检查数据集的配置与 split，不能把测试划分并入训练。
- 在筛题和调参前固定独立评估集合，并检查重复题。
- 在执行任何模型生成程序前，先实现隔离判题与时间、进程、内存限制。仅使用 Python `subprocess` 和 timeout 并不构成完整隔离。
- 记录模型与数据 revision、随机种子、采样参数、训练步数和评估条件。
- AutoDL 普通容器实例不支持内部运行 Docker，判题方案须单独验证可用的隔离方式。

这些是后续实施步骤，目前尚未完成。
