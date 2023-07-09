# MIT License
#
# Copyright (c) 2018 Omidiora Samuel, samparsky@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from blockchainetl.jobs.exporters.composite_item_exporter import CompositeItemExporter
from blockchainetl.jobs.exporters.s3_item_exporter import S3ItemExporter

BLOCK_FIELDS_TO_EXPORT = [
    'hash',
    'size',
    'stripped_size',
    'weight',
    'number',
    'version',
    'merkle_root',
    'timestamp',
    'nonce',
    'bits',
    'coinbase_param',
    'transaction_count'
]

TRANSACTION_FIELDS_TO_EXPORT = [
    'hash',
    'size',
    'virtual_size',
    'version',
    'lock_time',
    'block_number',
    'block_hash',
    'block_timestamp',
    'is_coinbase',
    'index',

    'inputs',
    'outputs',

    'input_count',
    'output_count',
    'input_value',
    'output_value',
    'fee'
]


def blocks_and_transactions_item_exporter(blocks_output=None, transactions_output=None, output=None):
    filename_mapping = {}
    field_mapping = {}

    if blocks_output is not None:
        filename_mapping['block'] = blocks_output
        field_mapping['block'] = BLOCK_FIELDS_TO_EXPORT

    if transactions_output is not None:
        filename_mapping['transaction'] = transactions_output
        field_mapping['transaction'] = TRANSACTION_FIELDS_TO_EXPORT

    if output is not None and output.startswith('s3://'):
        return S3ItemExporter(
            output=output,
            filename_mapping=filename_mapping,
            field_mapping=field_mapping
        )


    return CompositeItemExporter(
        filename_mapping=filename_mapping,
        field_mapping=field_mapping
    )
