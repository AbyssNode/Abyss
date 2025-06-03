# data_fetch_status.py

def get_status_report(fetch_logs):
    """
    Analyzes logs from external fetch jobs and reports failures or delays.
    """
    report = {"success": 0, "fail": 0}
    for log in fetch_logs:
        if log['status'] == "success":
            report['success'] += 1
        else:
            report['fail'] += 1
    return report
