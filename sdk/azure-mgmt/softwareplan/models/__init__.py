# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import Error, ErrorException
    from ._models_py3 import HybridUseBenefitModel
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationResponse
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AzureEntityResource
    from ._models import Error, ErrorException
    from ._models import HybridUseBenefitModel
    from ._models import OperationDisplay
    from ._models import OperationResponse
    from ._models import ProxyResource
    from ._models import Resource
    from ._models import Sku
    from ._models import TrackedResource
from ._paged_models import HybridUseBenefitModelPaged
from ._paged_models import OperationResponsePaged
from ._softwareplan_client_enums import (
    ErrorCode,
    ProvisioningState,
)

__all__ = [
    'AzureEntityResource',
    'Error', 'ErrorException',
    'HybridUseBenefitModel',
    'OperationDisplay',
    'OperationResponse',
    'ProxyResource',
    'Resource',
    'Sku',
    'TrackedResource',
    'HybridUseBenefitModelPaged',
    'OperationResponsePaged',
    'ErrorCode',
    'ProvisioningState',
]
