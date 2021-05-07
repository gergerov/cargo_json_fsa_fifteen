import pyparsing as pars

from cargo_json_fsa_fifteen import data_elements as b

osi_details = pars.Group(
    b.slant_separator +
    b.other_service_information('other_service_information') +
    b.crlf_separator
)

#
# osi = (
#     pars.Group(
#         pars.Literal('OSI') +
#         pars.OneOrMore(osi_details)('osi_details')
#     )
# )#('other_service_information')
osi = (
    pars.Literal('OSI') +
    pars.OneOrMore(
        osi_details
    )('osi_details')
)
