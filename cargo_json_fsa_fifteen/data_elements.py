import pyparsing as pars


message_type_version_number = pars.Word(pars.nums)
status_code = pars.Word(pars.alphas, exact=3)
airline_prefix = pars.Word(pars.nums, exact=3)
hiphen_separator = pars.Word('-',exact=1)
awb_serial_number = pars.Word(pars.nums, exact=8)
airport_city_code = pars.Word(pars.alphas, exact=3)
carrier_code = pars.Word(pars.alphanums, exact=2)
slant_separator = pars.Word('/', exact=1)
crlf_separator = pars.Word('|', exact=1)
day = pars.Word(pars.nums, exact=2)
month = pars.Word(pars.alphas, exact=3)
airport_code = pars.Word(pars.alphas, exact=3)
shipment_description_code = pars.Word('TP', exact=1)
number_of_pieces = pars.Word(pars.nums, min=1, max=4)
weight_code = pars.Word('KL', exact=1)
weight = pars.Word(pars.nums + '.', min=1, max=7)
type_of_time_indicator = pars.Word('AES', exact=1)
time = pars.Word(pars.nums, exact=4)
day_change_indicator_template = pars.Word('ABCDIFGHIJKLPNST', exact=1)
other_service_information = pars.Word(pars.alphanums + ' .-,=:', min=1, max=65)
iso_country_code = pars.Word(pars.alphas, exact=2)
information_identifier = pars.Word(pars.alphas, exact=3)
csr_control_information_identifier = pars.Word(pars.alphas, min=1, max=2)
scsr_information = pars.Word(pars.alphanums + ' .,=*-', min=1, max=35)
volume_code = pars.Word('CFMI', exact=2)
volume_amount = pars.Word(pars.nums + '.', min=1, max=9)
density_indicator = pars.Word('DG', exact=2)
density_group = pars.Word(pars.nums, min=1, max=2)

uld_type = pars.Combine(
    pars.Word(pars.alphas, exact=1) +
    pars.Word(pars.alphanums, exact=2)
)
uld_owner_code = pars.Word(pars.alphanums, exact=2)
uld_serial_number = pars.Combine(
    pars.Word(pars.alphanums, exact=1) +
    pars.Word(pars.nums, exact=3) +
    pars.Optional(pars.Word(pars.nums, exact=1))
)
uld_loading_indicator = pars.Word(pars.alphas, exact=1)
flight_number = pars.Combine(
    pars.Word(pars.nums, exact=3)
    + pars.Optional(pars.Word(pars.nums, exact=1))
    + pars.Optional(pars.Word(pars.alphas, exact=1))
)



