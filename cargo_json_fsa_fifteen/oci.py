import pyparsing as pars

from cargo_json_fsa_fifteen import data_elements as b

line_identifier = pars.Literal('OCI')
oci_group = pars.Group(
    b.slant_separator +
    pars.Optional(b.iso_country_code)('iso_country_code') +
    b.slant_separator +
    pars.Optional(b.information_identifier)('information_identifier') +
    b.slant_separator +
    pars.Optional(b.csr_control_information_identifier)
    ('custom_security_and_regulatory_control_information_identifier') +
    b.slant_separator +
    b.scsr_information
    ('supplementary_customs_security_and_regulatory_control_information') +
    b.crlf_separator
)

oci = pars.OneOrMore(
    line_identifier.suppress() +
    pars.OneOrMore(oci_group)
)('other_customs_security_and_regulatory_information')

#
# oci_test_msg = 'OCI/FR/IMP/M/07FR9876AB88901235|' \
#                '//HWB/I/ABCD12345678|'
#
#
# parse_result = oci.parseString(oci_test_msg)
# from pprint import pprint as print
# print(parse_result.asDict())
