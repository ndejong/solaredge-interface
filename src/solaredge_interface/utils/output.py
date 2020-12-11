
import json
import logging
from solaredge_interface.utils.json import JSONEncoderDateTime
from solaredge_interface import __output_format_default__ as OUTPUT_FORMAT_DEFAULT
from solaredge_interface.exceptions.SolarEdgeInterfaceException import SolarEdgeInterfaceException

logger = logging.getLogger(__name__)


def format_output(response, output_format=OUTPUT_FORMAT_DEFAULT):
    if type(output_format) is str:
        output_format = output_format.lower()
    if hasattr(response, 'data') and response.data and output_format == 'json':
        output_json(response.data)
    elif hasattr(response, 'pandas') and response.pandas is not None and output_format == 'pandas':
        output_pandas(response.pandas)
    elif hasattr(response, 'pandas') and response.pandas is not None and output_format == 'csv':
        output_csv(response.pandas)
    elif output_format not in ['json', 'pandas', 'csv']:
        raise SolarEdgeInterfaceException('Unknown output format requested: {}'.format(output_format))
    else:
        logging.warning('response.data is not available for output formatting, raw response data is provided')
        print(response.text)


def output_json(data):
    print(json.dumps(data, cls=JSONEncoderDateTime, indent='  '))


def output_pandas(pandas_dataframe):
    output_json(json.loads(pandas_dataframe.to_json()))


def output_csv(pandas_dataframe):
    print(pandas_dataframe.to_csv())
