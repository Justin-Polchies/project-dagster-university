import dagster as dg


class AdhocRequestConfig(dg.Config):
    filename: str
    borough: str
    start_date: str
    end_date: str
