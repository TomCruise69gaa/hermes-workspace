from pathlib import Path

WORKSPACE_ROOT = Path(r"C:\Users\jaymo\hermes-workspace").resolve()

def validate_secure_path(user_path: str) -> Path:
    """Ensures target file paths remain strictly inside hermes-workspace."""
    target_path = (WORKSPACE_ROOT / user_path).resolve()
    if not target_path.is_relative_to(WORKSPACE_ROOT):
        raise PermissionError(f"Access denied: Path '{target_path}' is outside authorized boundaries.")
    return target_path
