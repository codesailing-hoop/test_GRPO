"""检查 GPU 与 GRPO 核心组件；在远程 GPU 环境运行，不执行生成的代码。"""

import sys
from importlib.metadata import version


def main():
    print("当前 Python:", sys.executable)
    print("Python 版本:", sys.version)
    for name in (
        "torch", "transformers", "datasets", "trl",
        "accelerate", "peft", "huggingface-hub",
    ):
        print(f"{name}: {version(name)}")

    import torch
    from datasets import load_dataset
    from peft import LoraConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import GRPOConfig, GRPOTrainer

    print("核心组件导入成功")
    if not torch.cuda.is_available():
        raise RuntimeError("当前环境无法使用 CUDA GPU，请检查镜像、驱动与设备分配。")

    properties = torch.cuda.get_device_properties(0)
    print("GPU:", torch.cuda.get_device_name(0))
    print("设备总显存 GiB:", round(properties.total_memory / 1024**3, 2))
    print("PyTorch CUDA:", torch.version.cuda)
    print("计算能力:", torch.cuda.get_device_capability(0))
    print("支持 BF16:", torch.cuda.is_bf16_supported())
    x = torch.randn(256, 256, device="cuda")
    y = x @ x
    torch.cuda.synchronize()
    print("GPU 矩阵运算成功，结果形状:", tuple(y.shape))


if __name__ == "__main__":
    main()
