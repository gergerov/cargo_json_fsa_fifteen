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


transferred_from_detail = (
    pars.Group(
        b.slant_separator +
        b.carrier_code('carrier_code_transferring_carrier') +
        pars.Optional(
            b.slant_separator + b.name('name')
        )
    )
)('transferred_from_detail')


transfer_reference = (
    pars.Group(
        b.slant_separator +
        b.transfer_manifest_number('transfer_manifest_number')
    )
)('transfer_reference')


movement_detail = (
    pars.Group(
        b.carrier_code('carrier_code_receiving_carrier') +
            b.slant_separator +
        b.day('day_of_transfer') +
        b.month('month_of_transfer') +
        b.time('actual_time_of_givan_status_event') +
        b.slant_separator +
        b.airport_code('airport_code_of_transfer')
    )
)('movement_detail')


status_detail_tfd = (
    pars.Group(
        pars.Literal('TFD')('status_code') +
        b.slant_separator +
        movement_detail +
        quantity_detail +
        pars.Optional(transfer_reference) +
        pars.Optional(
            b.crlf_separator +
            transferred_from_detail
        ) +
        b.crlf_separator +
        pars.Optional(oci)
    )
)('status_detail')