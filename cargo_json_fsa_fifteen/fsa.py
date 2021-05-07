import pyparsing as pars

from cargo_json_fsa_fifteen.consignment_detail import consignment_detail
from cargo_json_fsa_fifteen.osi import osi
from cargo_json_fsa_fifteen.smi import standart_message_identification
from cargo_json_fsa_fifteen.status_detail import status_details
from cargo_json_fsa_fifteen.uld import uld_description

awbs = pars.Group(consignment_detail + pars.OneOrMore(status_details)('statuses'))

fsa_fifteen_pattern = (
    standart_message_identification +
    pars.OneOrMore(awbs)('awbs') +
    pars.Optional(uld_description) +
    pars.Optional(osi)
)

