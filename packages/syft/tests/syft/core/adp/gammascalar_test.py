# syft absolute
from syft.core.adp.entity import Entity
from syft.core.adp.scalar.gamma_scalar import GammaScalar


def test_scalar() -> None:
    bob = GammaScalar(
        value=1, min_val=-2, max_val=2, entity=Entity(name="Bob"), prime=3
    )
    alice = GammaScalar(
        value=1, min_val=-1, max_val=1, entity=Entity(name="Alice"), prime=5
    )
    bob + alice
    bob - alice
    bob * alice
