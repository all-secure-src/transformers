from typing import TYPE_CHECKING

from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_flax_available, is_torch_available


_import_structure = {
    "configuration_omegamaize": ["OmegaMaizeConfig"],
}

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_omegamaize"] = [
        "OmegaMaizeForCausalLM",
        "OmegaMaizeModel",
        "OmegaMaizePreTrainedModel",
        "OmegaMaizeForSequenceClassification",
    ]

try:
    if not is_flax_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_flax_omegamaize"] = [
        "FlaxOmegaMaizeForCausalLM",
        "FlaxOmegaMaizeModel",
        "FlaxOmegaMaizePreTrainedModel",
    ]


if TYPE_CHECKING:
    from .configuration_omegamaize import OmegaMaizeConfig

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_omegamaize import (
            OmegaMaizeForCausalLM,
            OmegaMaizeForSequenceClassification,
            OmegaMaizeModel,
            OmegaMaizePreTrainedModel,
        )

    try:
        if not is_flax_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_flax_omegamaize import (
            FlaxOmegaMaizeForCausalLM,
            FlaxOmegaMaizeModel,
            FlaxOmegaMaizePreTrainedModel,
        )


else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
