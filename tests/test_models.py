import pytest
from uuid import UUID
from datetime import datetime
from vindicta_foundation.models.base import VindictaModel
from vindicta_foundation.models.entropy import EntropyProof
from vindicta_foundation.models.economy import GasTankState

def test_vindicta_model_defaults() -> None:
    model = VindictaModel()
    assert isinstance(model.id, UUID)
    assert isinstance(model.created_at, datetime)
    assert model.updated_at is None

def test_entropy_proof_validation() -> None:
    # Valid SHA-256 hash
    valid_hash = "a" * 64
    proof = EntropyProof(seed_hash=valid_hash)
    assert proof.algorithm == "csprng"
    
    # Invalid hash
    with pytest.raises(ValueError):
        EntropyProof(seed_hash="short")

def test_gas_tank_state_logic() -> None:
    # Empty tank
    empty = GasTankState(balance_usd=0.0, limit_usd=10.0)
    assert empty.is_empty is True
    assert empty.is_low is True
    
    # Full tank
    full = GasTankState(balance_usd=10.0, limit_usd=10.0)
    assert full.is_empty is False
    assert full.is_low is False
    
    # Low tank (below 10%)
    low = GasTankState(balance_usd=0.9, limit_usd=10.0)
    assert low.is_low is True

