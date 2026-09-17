import torch
import time

def sync_device(device):
    if device.type == "mps":
        torch.mps.synchronize()
    elif device.type == "cuda":
        torch.cuda.synchronize(device)


def generate_batched(
    input_ids: torch.Tensor,
    attention_mask: torch.Tensor,
    model,
    max_new_tokens: int,
    eos_token_id: int | None,
    pad_token_id: int,
    temperature=0.0,
    top_k=None,
    top_p=None,
) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Returns
    -------
    output_ids:
        [B, prompt_width + steps] padded tensor. Rows that stopped keep their
        EOS in the sequence, and every later slot of that row is PAD.

    generated_lengths:
        [B] int64. How many *valid* tokens each request produced. EOS and the
        post-stop PAD slots are never counted, so this is the number of tokens
        the caller is allowed to show the user.
    """
    
    raise NotImplementedError(
        "Not yet implemented"
    )