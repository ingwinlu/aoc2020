import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = None

    _validator_hcl = re.compile(r"^#[a-f0-9]{6}$")

    @classmethod
    def from_segment(cls, segment):
        key_value_pairs = segment.split()
        kvs = map(lambda kv: kv.split(':'), key_value_pairs)
        kv_dict = dict(list(kvs))
        try:
            return cls(**kv_dict)
        except TypeError:
            return None

    def _validate_byr(self):
        byr = int(self.byr)
        return byr >= 1920 and byr <= 2002

    def _validate_iyr(self):
        iyr = int(self.iyr)
        return iyr >= 2010 and iyr <= 2020

    def _validate_eyr(self):
        eyr = int(self.eyr)
        return eyr >= 2020 and eyr <= 2030

    def _validate_hgt(self):
        if self.hgt.endswith('cm'):
            h = int(self.hgt[:-2])
            return h >= 150 and h <= 193
        elif self.hgt.endswith('in'):
            h = int(self.hgt[:-2])
            return h >= 59 and h <= 76
        return False

    def _validate_hcl(self):
        return self._validator_hcl.fullmatch(self.hcl) is not None

    def _validate_ecl(self):
        return self.ecl in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]

    def _validate_pid(self):
        return self.pid.isnumeric() and len(self.pid) == 9

    def validate(self):
        """
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
        """
        return all([
            self._validate_byr(),
            self._validate_iyr(),
            self._validate_eyr(),
            self._validate_hgt(),
            self._validate_hcl(),
            self._validate_ecl(),
            self._validate_pid()
        ])


def parse():
    passport_segments = open('input.txt').read().split('\n\n')
    passports_incl_none = map(Passport.from_segment, passport_segments)
    passports = list(filter(None.__ne__, passports_incl_none))
    return passports


def task1():
    passports = parse()
    return len(passports)


def task2():
    passports = parse()
    valid = list(filter(lambda passport: passport.validate(), passports))
    return len(valid)


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
