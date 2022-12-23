import datetime

TARGET_YEAR = datetime.date.today().year
LICENSE_PREFIX = \
"""MIT License

Copyright (c) """

def update_license(lic: str, repo_name: str, target: int = TARGET_YEAR) -> str:
    real_lic = lic.removeprefix(LICENSE_PREFIX)
    year = real_lic.split()[0]
    license_suffix = real_lic.removeprefix(year)

    if year.isnumeric():
        if target < int(year):
            print(f"Year is already {target} in {repo_name}")
            return
        return f"{LICENSE_PREFIX}{year}-{target}{license_suffix}"
    else:
        years = year.split("-")
        if len(years) != 2:
            print(f"Invalid year format \"{year}\" in {repo_name}")
            return
        if years[0].isnumeric() and years[1].isnumeric():
            if int(years[1]) >= target:
                print(f"Year is already \"{years[1]}\" in {repo_name}")
                return
            return f"{LICENSE_PREFIX}{years[0]}-{target}{license_suffix}"
        print(f"Invalid year format \"{year}\" in {repo_name}")
        return
