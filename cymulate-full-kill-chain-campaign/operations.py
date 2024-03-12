"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import requests
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError
from requests import exceptions as req_exceptions

logger = get_logger('cymulate-full-kill-chain-campaign')

error_msgs = {
    400: 'Bad/Invalid Request',
    401: 'Unauthorized: Invalid credentials or token provided failed to authorize',
    403: 'Access Denied',
    404: 'Not Found',
    500: 'Internal Server Error',
    503: 'Service Unavailable'
}


class CymulateCART:
    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.API_VERSION = '/v1'
        self.verify_ssl = config.get('verify_ssl')
        self.headers = {"Content-Type": "application/json", "x-token": config.get('apiKey')}

    def make_rest_call(self, endpoint='', params={}, payload=None, method='GET'):
        params = {k: v for k, v in params.items() if v is not None and v != ''}
        service_endpoint = '{0}{1}{2}'.format(self.server_url, self.API_VERSION, endpoint)
        logger.error('API Request Endpoint: {0}'.format(service_endpoint))
        logger.error('API Request Params: {0}'.format(params))
        logger.error('API Request Payload: {0}'.format(payload))
        try:
            response = requests.request(method, service_endpoint, data=payload, headers=self.headers, params=None,
                                        verify=self.verify_ssl)
            logger.error('API Response Status Code: {0}'.format(response.status_code))
            logger.error('API Response: {0}'.format(response.text))
            if response.ok:
                json_resp = response.json()
                if 'data' in json_resp:
                    return json_resp.get('data')
                else:
                    return json_resp
            else:
                if error_msgs.get(response.status_code):
                    raise ConnectorError('{0}: {1}'.format(error_msgs.get(response.status_code), response.text))
                else:
                    raise ConnectorError('{0}: '.format(response.text))
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))


def convert_datetime(input_datetime, only_date=False):
    dt_object = datetime.strptime(input_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
    if only_date:
        output_datetime = dt_object.strftime('%Y-%m-%d')
    else:
        output_datetime = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    return output_datetime


def get_campaign_report(config, params):
    cart = CymulateCART(config)
    return cart.make_rest_call('/apt-wrapper/attacks', params=params)


def get_campaign_assessments_ids(config, params):
    cart = CymulateCART(config)
    return cart.make_rest_call('/apt-wrapper/ids', params=params)


def get_technical_report_for_specific_assessment(config, params):
    cart = CymulateCART(config)
    assessment_id = params.get('assessment_id')
    return cart.make_rest_call(f'/apt-wrapper/attack/technical/{assessment_id}')


def launch_campaign_assessment(config, params):
    cart = CymulateCART(config)
    template_id = params.get('templateID')
    schedule = params.get('schedule')
    schedule_loop = params.get('scheduleLoop', '')
    payload = {
        "templateID": template_id,
        "schedule": convert_datetime(schedule),
        "scheduleLoop": schedule_loop.replace(' ', '-').lower()
    }
    return cart.make_rest_call('/apt-wrapper/start/', payload=payload, method='POST')


def stop_campaign_assessment(config, params):
    cart = CymulateCART(config)
    return cart.make_rest_call('/apt-wrapper/stop/', params=params, method='POST')


def get_campaign_assessment_history(config, params):
    cart = CymulateCART(config)
    from_date = params.get('fromDate')
    if from_date:
        params['fromDate'] = convert_datetime(from_date, only_date=True)
    to_date = params.get('toDate')
    if to_date:
        params['toDate'] = convert_datetime(from_date, only_date=True)
    return cart.make_rest_call('/apt-wrapper/history/get-ids/', params=params)


def get_specific_campaign_assessment_report(config, params):
    cart = CymulateCART(config)
    assessment_id = params.pop('id', '')
    return cart.make_rest_call(f'/apt-wrapper/history/technical/{assessment_id}', params=params)


def get_campaign_assessment_status(config, params):
    cart = CymulateCART(config)
    return cart.make_rest_call('/apt-wrapper/status/', params=params)


def get_campaign_templates(config, params):
    cart = CymulateCART(config)
    return cart.make_rest_call('/apt-wrapper/templates/')


def test_connectivity(config):
    try:
        get_campaign_templates(config, {})
    except Exception as err:
        raise ConnectorError(str(err))


operations = {
    'get_campaign_report': get_campaign_report,
    'get_campaign_assessments_ids': get_campaign_assessments_ids,
    'get_technical_report_for_specific_assessment': get_technical_report_for_specific_assessment,
    'launch_campaign_assessment': launch_campaign_assessment,
    'stop_campaign_assessment': stop_campaign_assessment,
    'get_campaign_assessment_history': get_campaign_assessment_history,
    'get_specific_campaign_assessment_report': get_specific_campaign_assessment_report,
    'get_campaign_assessment_status': get_campaign_assessment_status,
    'get_campaign_templates': get_campaign_templates

}
