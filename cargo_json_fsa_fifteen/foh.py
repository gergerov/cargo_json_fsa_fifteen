import pyparsing as pars

from cargo_json_fsa_fifteen import data_elements as b
from cargo_json_fsa_fifteen.oci import oci


quantity_detail = (
    pars.Group(
        b.slant_separator +
        b.shipment_description_code('shipment_description_code') +
        b.number_of_pieces('number_of_pieces') +
        pars.Optional(
            b.weight_code('weight_code') +
            b.weight('weight')
        )
    )
)('quantity_detail')


movement_detail = (
    pars.Group(
        b.day('day_of_receipt')+
        b.month('month_of_receipt') +
        b.time('actual_time_of_given_status_event') +
        b.slant_separator +
        b.airport_code('airport_code_of_receipt')
    )
)('movement_detail')


density_group = pars.Group(
    b.density_indicator +
    b.density_group
)('density_group')

volume_detail = pars.Group(
    b.volume_code('volume_code') +
    b.volume_amount('volume_amount')
)('volume_detail')

received_from_detail = (
    pars.Group(
        b.slant_separator + b.name('name')
    )
)('received_from_detail')


status_detail_foh = (
    pars.Group(
        pars.Literal('FOH')('status_code') +
        b.slant_separator +
        movement_detail +
        quantity_detail +
        pars.Optional(received_from_detail) +
        b.crlf_separator +
        pars.Optional(b.slant_separator + volume_detail + b.crlf_separator) +
        pars.Optional(b.slant_separator + density_group + b.crlf_separator) +
        pars.Optional(oci)
    )
)('status_detail')