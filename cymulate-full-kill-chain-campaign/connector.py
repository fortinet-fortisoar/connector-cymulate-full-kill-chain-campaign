"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from connectors.core.connector import Connector, get_logger, ConnectorError

from .operations import operations, test_connectivity

logger = get_logger('cymulate-full-kill-chain-campaign')


class CymulateCARTConnector(Connector):
    def execute(self, config, operation, params, **kwargs):
        logger.debug('Running Operation: {}'.format(operation))
        try:
            operation = operations.get(operation)
            return operation(config, params)
        except Exception as err:
            logger.error('{}'.format(err))
            raise ConnectorError('{}'.format(err))

    def check_health(self, config):
        return test_connectivity(config)
