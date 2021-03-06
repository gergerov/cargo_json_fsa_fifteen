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
        b.day('day_of_scheduled_arrival') +
        b.month('month_of_scheduled_arrival') +
        b.time('actual_time_of_given_status_event') +
        pars.Optional(
            b.hiphen_separator +
            b.day_change_indicator_template('day_change_indicator')
        ) +
        b.slant_separator +
        b.airport_code('airport_code_of_arrival')
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


time_of_arrival_information = (
    pars.Group(
        b.slant_separator +
        b.type_of_time_indicator('type_of_time_indicator') +
        b.time('time') +
        pars.Optional(
            b.hiphen_separator +
            b.day_change_indicator_template('day_change_indicator')
        )
    )
)('time_of_arrival_information')



time_of_departure_information = (
    pars.Group(
        b.slant_separator +
        b.type_of_time_indicator('type_of_time_indicator') +
        b.time('time') +
        pars.Optional(
            b.hiphen_separator +
            b.day_change_indicator_template('day_change_indicator')
        )
    )
)('time_of_departure_information')



status_detail_rcf = (
    pars.Group(
        pars.Literal('RCF')('status_code') +
        b.slant_separator +
        movement_detail +
        quantity_detail +
        pars.Optional(time_of_departure_information) +
        pars.Optional(time_of_arrival_information) +
        b.crlf_separator +
        pars.Optional(oci)
    )
)('status_detail')