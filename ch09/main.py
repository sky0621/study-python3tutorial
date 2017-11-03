from ch09.ok import OkStatus
from ch09.status_code import StatusCode

if __name__ == "__main__":
    sc = StatusCode()
    sc.description()

    print("==============")
    ok = OkStatus()
    ok.description()