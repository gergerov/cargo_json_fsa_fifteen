import pyparsing as pars

from cargo_json_fsa_fifteen import data_elements as b

awb_identification = (
    pars.Group(
        b.airline_prefix('airline_prefix') +
        b.hiphen_separator +
        b.awb_serial_number('awb_serial_number')
    )
)('awb_identification')


awb_origin_and_destination = (
    pars.Group(
        pars.Optional(
            b.airport_code('airport_code_of_origin') +
            b.airport_code('airport_code_of_destination')
        )
    )
)('awb_origin_and_destination')


quantity_detail = (
    pars.Group(
        b.slant_separator +
        b.shipment_description_code('shipment_description_code') +
        b.number_of_pieces('number_of_pieces') +
        pars.Optional(
                (b.weight_code)('weight_code') +
                (b.weight)('weight')
            )
    )
)('quantity_detail')


total_consigment_pieces = (
    pars.Group(
        b.shipment_description_code('shipment_description_code') +
        b.number_of_pieces('number_of_pieces')
    )
)('total_consigment_peices')


consignment_detail = (
    pars.Group(
        awb_identification +
        awb_origin_and_destination +
        quantity_detail +
        pars.Optional(total_consigment_pieces) +
        b.crlf_separator
    )
)('consignment_detail')