import DAL.db as d

dta = d.DB()


def get_all_stats_data():
    return dta.execute_select_query("final_output")


def get_student():
    return dta.execute_select_query("final_output", params1=("is_student = 'TRUE'"))


def get_province(_p: str):
    return dta.execute_select_query("final_output", params={'prov_name': _p})


def get_lfstatus(_num: str):
    return dta.execute_select_query("final_output", params={'lfsstat': _num})

