from ch09.status_code import StatusCode


class OkStatus(StatusCode):
    def __init__(self):
        super().__init__()
        print("200")

    def description(self):
        print("OK")