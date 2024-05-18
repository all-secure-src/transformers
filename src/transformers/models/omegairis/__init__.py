from typing import TYPE_CHECKING

from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_torch_available, is_vision_available


_import_structure = {"configuration_omegairis": ["OmegaIrisConfig"]}


try:
    if not is_vision_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["image_processing_omegairis"] = ["OmegaIrisImageProcessor"]


try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_omegairis"] = [
        "OmegaIrisForConditionalGeneration",
        "OmegaIrisPreTrainedModel",
        "OmegaIrisModel",
    ]
    _import_structure["processing_omegairis"] = ["OmegaIrisProcessor"]

if TYPE_CHECKING:
    from .configuration_omegairis import OmegaIrisConfig

    try:
        if not is_vision_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .image_processing_omegairis import OmegaIrisImageProcessor

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_omegairis import (
            OmegaIrisForConditionalGeneration,
            OmegaIrisModel,
            OmegaIrisPreTrainedModel,
        )
        from .processing_omegairis import OmegaIrisProcessor


else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure)
