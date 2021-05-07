import pyparsing as pars

from cargo_json_fsa_fifteen import data_elements as b

standart_message_identification = (
    pars.Group(
        (pars.Word('FSUA'))('standart_message_identifier') +
            b.slant_separator +
        (b.message_type_version_number)('message_type_version_number') +
            b.crlf_separator
    )
)('standart_message_identification')
