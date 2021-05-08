import pyparsing as pars

from cargo_json_fsa_fifteen import data_elements as b
from cargo_json_fsa_fifteen.oci import oci


movement_detail = (
    pars.Group(
        pars.Optional(
            b.carrier_code('carrier_code') +
            b.flight_number('flight_number')
        ) +
        b.slant_separator +
        pars.Optional(b.day)('day_of_discrepancy') +
        pars.Optional(b.month)('month_of_discrepancy') +
        b.time('actual_time_of_given_status_event') +
        b.slant_separator +
        b.airport_code('airport_code_of_discrepancy')
    )
)('movement_detail')


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


discrepancy_description = (
    pars.Group(
        b.slant_separator +
        b.discrepancy_code('description_code')
    )
)('discrepancy_description')


status_detail_dis = (
    pars.Group(
        pars.Literal('DIS')('status_code') +
        b.slant_separator +
        movement_detail +
        discrepancy_description +
        quantity_detail +
        b.crlf_separator +
        pars.Optional(oci)
    )
)('status_detail')