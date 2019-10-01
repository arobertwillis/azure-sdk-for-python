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

from msrest.serialization import Model


class IdentityProviderUpdateParameters(Model):
    """Parameters supplied to update Identity Provider.

    :param type: Identity Provider Type identifier. Possible values include:
     'facebook', 'google', 'microsoft', 'twitter', 'aad', 'aadB2C'
    :type type: str or ~azure.mgmt.apimanagement.models.IdentityProviderType
    :param signin_tenant: The TenantId to use instead of Common when logging
     into Active Directory
    :type signin_tenant: str
    :param allowed_tenants: List of Allowed Tenants when configuring Azure
     Active Directory login.
    :type allowed_tenants: list[str]
    :param authority: OpenID Connect discovery endpoint hostname for AAD or
     AAD B2C.
    :type authority: str
    :param signup_policy_name: Signup Policy Name. Only applies to AAD B2C
     Identity Provider.
    :type signup_policy_name: str
    :param signin_policy_name: Signin Policy Name. Only applies to AAD B2C
     Identity Provider.
    :type signin_policy_name: str
    :param profile_editing_policy_name: Profile Editing Policy Name. Only
     applies to AAD B2C Identity Provider.
    :type profile_editing_policy_name: str
    :param password_reset_policy_name: Password Reset Policy Name. Only
     applies to AAD B2C Identity Provider.
    :type password_reset_policy_name: str
    :param client_id: Client Id of the Application in the external Identity
     Provider. It is App ID for Facebook login, Client ID for Google login, App
     ID for Microsoft.
    :type client_id: str
    :param client_secret: Client secret of the Application in external
     Identity Provider, used to authenticate login request. For example, it is
     App Secret for Facebook login, API Key for Google login, Public Key for
     Microsoft.
    :type client_secret: str
    """

    _validation = {
        'allowed_tenants': {'max_items': 32},
        'signup_policy_name': {'min_length': 1},
        'signin_policy_name': {'min_length': 1},
        'profile_editing_policy_name': {'min_length': 1},
        'password_reset_policy_name': {'min_length': 1},
        'client_id': {'min_length': 1},
        'client_secret': {'min_length': 1},
    }

    _attribute_map = {
        'type': {'key': 'properties.type', 'type': 'str'},
        'signin_tenant': {'key': 'properties.signinTenant', 'type': 'str'},
        'allowed_tenants': {'key': 'properties.allowedTenants', 'type': '[str]'},
        'authority': {'key': 'properties.authority', 'type': 'str'},
        'signup_policy_name': {'key': 'properties.signupPolicyName', 'type': 'str'},
        'signin_policy_name': {'key': 'properties.signinPolicyName', 'type': 'str'},
        'profile_editing_policy_name': {'key': 'properties.profileEditingPolicyName', 'type': 'str'},
        'password_reset_policy_name': {'key': 'properties.passwordResetPolicyName', 'type': 'str'},
        'client_id': {'key': 'properties.clientId', 'type': 'str'},
        'client_secret': {'key': 'properties.clientSecret', 'type': 'str'},
    }

    def __init__(self, *, type=None, signin_tenant: str=None, allowed_tenants=None, authority: str=None, signup_policy_name: str=None, signin_policy_name: str=None, profile_editing_policy_name: str=None, password_reset_policy_name: str=None, client_id: str=None, client_secret: str=None, **kwargs) -> None:
        super(IdentityProviderUpdateParameters, self).__init__(**kwargs)
        self.type = type
        self.signin_tenant = signin_tenant
        self.allowed_tenants = allowed_tenants
        self.authority = authority
        self.signup_policy_name = signup_policy_name
        self.signin_policy_name = signin_policy_name
        self.profile_editing_policy_name = profile_editing_policy_name
        self.password_reset_policy_name = password_reset_policy_name
        self.client_id = client_id
        self.client_secret = client_secret
