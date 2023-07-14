import pygsheets
from typing import List


class GoogleTable:
    def __init__(
        self, credence_file: str = "", googlesheet_id: str = ""
    ) -> None:
        self.credence_file: str = credence_file
        self.googlesheet_id: str = googlesheet_id

        self.client = pygsheets.authorize(
            service_file=self.credence_file)

    def _get_worksheet(self) -> pygsheets.Worksheet:
        spreadsheet = self.client.open_by_key(self.googlesheet_id)
        return spreadsheet.sheet1

    def get_notifications(self) -> List[pygsheets.Cell]:
        values = self._get_worksheet().range('A:E')

        res = []

        for value in values:
            if value[0].value == '':
                break
            res.append(value)

        return res[1:]

    def get_notifications_by_tel_id(self, tel_id: str) -> List[pygsheets.Cell]:
        notifications = self.get_notifications()
        res = []

        for notification in notifications:
            if notification[0].value == tel_id:
                res.append(notification)

        return res
