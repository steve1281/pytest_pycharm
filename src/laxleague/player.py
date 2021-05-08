import csv
from dataclasses import dataclass, field
from typing import List, Iterable, Optional

from laxleague.guardian import Guardian


@dataclass
class Player:
    first_name: str
    last_name: str
    guardians: List[Guardian] = field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians.append(guardian)

    def add_guardians(self, guardians: Iterable[Guardian]):
        self.guardians.extend(guardians)

    @property
    def primary_guardian(self) -> Optional[Guardian]:
        return self.guardians[0] if self.guardians else None

    def load_guardian_file(self, path):
        with open(path, newline='') as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                self.guardians.append(Guardian(*row))

    def write_guardians_file(self, path):
        with open(path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for g in self.guardians:
                writer.writerow([g.first_name, g.last_name])


