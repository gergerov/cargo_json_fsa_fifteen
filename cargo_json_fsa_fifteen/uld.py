import pyparsing as pars

from cargo_json_fsa_fifteen import data_elements as b

line_identifier = pars.Literal('ULD')
uld_identification = pars.Group(
    b.uld_type('uld_type') +
    b.uld_serial_number('uld_serial_number') +
    b.uld_owner_code('uld_owner_code')
)('uld_identification')

uld_position_information = pars.Group(
    b.hiphen_separator +
    b.uld_loading_indicator('uld_loading_indicator')
)('uld_position_information')

group_uld = pars.Group(
    b.slant_separator +
    uld_identification +
    pars.Optional(uld_position_information)
)
group_uld_row = pars.OneOrMore(group_uld)

uld_description = (
    line_identifier +
    pars.OneOrMore(
        group_uld_row +
        b.crlf_separator.suppress()
    )('uld_description')
)
