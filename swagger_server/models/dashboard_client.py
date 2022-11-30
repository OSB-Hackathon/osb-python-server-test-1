# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DashboardClient(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, secret: str=None, redirect_uri: str=None):  # noqa: E501
        """DashboardClient - a model defined in Swagger

        :param id: The id of this DashboardClient.  # noqa: E501
        :type id: str
        :param secret: The secret of this DashboardClient.  # noqa: E501
        :type secret: str
        :param redirect_uri: The redirect_uri of this DashboardClient.  # noqa: E501
        :type redirect_uri: str
        """
        self.swagger_types = {
            'id': str,
            'secret': str,
            'redirect_uri': str
        }

        self.attribute_map = {
            'id': 'id',
            'secret': 'secret',
            'redirect_uri': 'redirect_uri'
        }
        self._id = id
        self._secret = secret
        self._redirect_uri = redirect_uri

    @classmethod
    def from_dict(cls, dikt) -> 'DashboardClient':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DashboardClient of this DashboardClient.  # noqa: E501
        :rtype: DashboardClient
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this DashboardClient.


        :return: The id of this DashboardClient.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this DashboardClient.


        :param id: The id of this DashboardClient.
        :type id: str
        """

        self._id = id

    @property
    def secret(self) -> str:
        """Gets the secret of this DashboardClient.


        :return: The secret of this DashboardClient.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret: str):
        """Sets the secret of this DashboardClient.


        :param secret: The secret of this DashboardClient.
        :type secret: str
        """

        self._secret = secret

    @property
    def redirect_uri(self) -> str:
        """Gets the redirect_uri of this DashboardClient.


        :return: The redirect_uri of this DashboardClient.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri: str):
        """Sets the redirect_uri of this DashboardClient.


        :param redirect_uri: The redirect_uri of this DashboardClient.
        :type redirect_uri: str
        """

        self._redirect_uri = redirect_uri
