import pyparsing as pars

from cargo_json_fsa_fifteen import man, dep, rcf, bkd

status_details = pars.Group(
    man.status_detail_man ^
    dep.status_detail_dep ^
    rcf.status_detail_rcf ^
    bkd.status_detail_bkd
)