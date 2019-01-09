import time


class PublicUtils(object):

    @classmethod
    def get_chn_date(cls, str_time_stamp, formatter="%Y-%m-%d %H:%M:%S"):
        time_obj = time.strptime(str_time_stamp, formatter)
        year = time_obj.tm_year
        month = time_obj.tm_mon
        day = time_obj.tm_mday
        hour = time_obj.tm_hour
        minute = time_obj.tm_min
        return year + "年" + month + "月" + day + "日 " + hour + ":" + minute
