import pyparsing as pars

from cargo_json_fsa_fifteen import \
    man, dep, rcf, bkd, rcs, \
    rct, pre, trm, tfd, nfd, \
    awd, ccd, dlv, dis, crc, \
    foh, awr, arr, tgc, ddl

status_details = pars.Group(
    man.status_detail_man ^
    dep.status_detail_dep ^
    rcf.status_detail_rcf ^
    bkd.status_detail_bkd ^
    rcs.status_detail_rcs ^
    rct.status_detail_rct ^
    pre.status_detail_pre ^
    trm.status_detail_trm ^
    tfd.status_detail_tfd ^
    nfd.status_detail_nfd ^
    awd.status_detail_awd ^
    ccd.status_detail_ccd ^
    dlv.status_detail_dlv ^
    dis.status_detail_dis ^
    crc.status_detail_crc ^
    foh.status_detail_foh ^
    awr.status_detail_awr ^
    arr.status_detail_arr ^
    tgc.status_detail_tgc ^
    ddl.status_detail_dll
)