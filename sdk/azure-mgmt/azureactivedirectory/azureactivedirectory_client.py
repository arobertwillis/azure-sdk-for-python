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
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.metrics_operations import MetricsOperations
from .operations.metric_definitions_operations import MetricDefinitionsOperations
from .operations.operations import Operations
from .operations.diagnostic_settings_operations import DiagnosticSettingsOperations
from .operations.diagnostic_settings_category_operations import DiagnosticSettingsCategoryOperations
from . import models


class azureactivedirectoryClientConfiguration(AzureConfiguration):
    """Configuration for azureactivedirectoryClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(azureactivedirectoryClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azureactivedirectory/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class azureactivedirectoryClient(SDKClient):
    """Azure Active Directory Client.

    :ivar config: Configuration for client.
    :vartype config: azureactivedirectoryClientConfiguration

    :ivar metrics: Metrics operations
    :vartype metrics: microsoft.aadiam.operations.MetricsOperations
    :ivar metric_definitions: MetricDefinitions operations
    :vartype metric_definitions: microsoft.aadiam.operations.MetricDefinitionsOperations
    :ivar operations: Operations operations
    :vartype operations: microsoft.aadiam.operations.Operations
    :ivar diagnostic_settings: DiagnosticSettings operations
    :vartype diagnostic_settings: microsoft.aadiam.operations.DiagnosticSettingsOperations
    :ivar diagnostic_settings_category: DiagnosticSettingsCategory operations
    :vartype diagnostic_settings_category: microsoft.aadiam.operations.DiagnosticSettingsCategoryOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = azureactivedirectoryClientConfiguration(credentials, base_url)
        super(azureactivedirectoryClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.metrics = MetricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metric_definitions = MetricDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.diagnostic_settings = DiagnosticSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.diagnostic_settings_category = DiagnosticSettingsCategoryOperations(
            self._client, self.config, self._serialize, self._deserialize)