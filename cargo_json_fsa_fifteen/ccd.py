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
        b.day('day_of_clearance') +
        b.month('month_of_clearance') +
        b.time('actual_time_of_givan_status_event') +
        b.slant_separator +
        b.airport_code('airport_code_of_clearance')
    )
)('movement_detail')


status_detail_ccd = (
    pars.Group(
        pars.Literal('CCD')('status_code') +
        b.slant_separator +
        movement_detail +
        quantity_detail +
        b.crlf_separator +
        pars.Optional(oci)
    )
)('status_detail')