# mini_inference/sampling_generate.py

import torch


def generate_sampled(
    input_ids: torch.Tensor,
    model,
    max_new_tokens: int,
    temperature: float = 1.0,
    top_k: int | None = None,
    top_p: float | None = None,
    eos_token_id: int | None = None,
) -> torch.Tensor:
    
    raise NotImplementedError(
        "Not yet implemented"
    )