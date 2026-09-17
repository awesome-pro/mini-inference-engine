import torch


def generate_cached(
    input_ids: torch.Tensor,
    model,
    max_new_tokens: int,
    eos_token_id: int | None = None,
) -> torch.Tensor:
    
    raise NotImplementedError(
        "not yet implemented"
    )