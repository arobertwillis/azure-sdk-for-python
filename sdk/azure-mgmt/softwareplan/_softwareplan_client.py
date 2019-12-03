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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import softwareplanClientConfiguration
from .operations import SoftwarePlanOperations
from .operations import HybridUseBenefitOperations
from .operations import HybridUseBenefitRevisionOperations
from .operations import Operations
from . import models


class softwareplanClient(SDKClient):
    """Azure software plans let users create and manage licenses for various software used in Azure.

    :ivar config: Configuration for client.
    :vartype config: softwareplanClientConfiguration

    :ivar software_plan: SoftwarePlan operations
    :vartype software_plan: microsoft.softwareplan.operations.SoftwarePlanOperations
    :ivar hybrid_use_benefit: HybridUseBenefit operations
    :vartype hybrid_use_benefit: microsoft.softwareplan.operations.HybridUseBenefitOperations
    :ivar hybrid_use_benefit_revision: HybridUseBenefitRevision operations
    :vartype hybrid_use_benefit_revision: microsoft.softwareplan.operations.HybridUseBenefitRevisionOperations
    :ivar operations: Operations operations
    :vartype operations: microsoft.softwareplan.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = softwareplanClientConfiguration(credentials, subscription_id, base_url)
        super(softwareplanClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-06-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.software_plan = SoftwarePlanOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hybrid_use_benefit = HybridUseBenefitOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hybrid_use_benefit_revision = HybridUseBenefitRevisionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
