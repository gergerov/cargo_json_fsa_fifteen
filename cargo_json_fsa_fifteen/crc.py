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
        pars.Optional(b.carrier_code)('carrier_code') +
        pars.Optional(b.flight_number)('flight_number') +
        b.slant_separator +
        pars.Optional(b.day)('day_of_scheduled_departure') +
        pars.Optional(b.month)('month_of_scheduled_departure') +
        b.slant_separator +
        b.airport_code('airport_code_of_departure') +
        b.airport_code('airport_code_of_arrival')
    )
)('movement_detail')


reporting_detail = (
    pars.Group(
        b.day('day_of_scheduled_departure') +
        b.month('month_of_scheduled_departure') +
        b.time('actual_time_of_given_status_event') +
        b.slant_separator +
        b.airport_code('airport_code_of_reporting')
    )
)('movement_detail')


status_detail_crc = (
    pars.Group(
        pars.Literal('CRC')('status_code') +
        b.slant_separator +
        reporting_detail +
        quantity_detail +
        pars.Optional(
            b.slant_separator +
            movement_detail
        ) +
        b.crlf_separator +
        pars.Optional(oci)
    )
)('status_detail')