from typing import TYPE_CHECKING

from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_torch_available, is_vision_available

_import_structure = {
    "configuration_omegasparkvision": ["OmegaSparkVisionConfig"],
    "processing_omegasparkvision": ["OmegaSparkVisionProcessor"],
}


try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_omegasparkvision"] = [
        "OmegaSparkVisionForConditionalGeneration",
        "OmegaSparkVisionPreTrainedModel",
    ]

try:
    if not is_vision_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["image_processing_omegasparkvision"] = ["OmegaSparkVisionImageProcessor"]


if TYPE_CHECKING:
    from .configuration_omegasparkvision import OmegaSparkVisionConfig
    from .processing_omegasparkvision import OmegaSparkVisionProcessor

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_omegasparkvision import (
            OmegaSparkVisionForConditionalGeneration,
            OmegaSparkVisionPreTrainedModel,
        )

    try:
        if not is_vision_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .image_processing_omegasparkvision import OmegaSparkVisionImageProcessor


else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure)
