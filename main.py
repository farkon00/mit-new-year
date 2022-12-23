import github

from github import Github

from config import *

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

def main():
    gh = Github(GITHUB_ACCESS_TOKEN)

    for repo in gh.get_user().get_repos():
        try:
            file = repo.get_contents("LICENSE")
            lic = file.decoded_content.decode().replace('\r\n', '\n')
            if not lic.startswith(LICENSE_PREFIX):
                print(f"{repo.full_name} has wrong license format. Skipping")
                continue
            new_lic = update_license(lic, repo.full_name)
            if new_lic is None:
                print(f"{repo.full_name} wasn't processed successfully. Skipping")
                continue
            try:
                repo.update_file(file.path, COMMIT_MESSAGE, new_lic, file.sha)
            except Exception:
                print(f"{repo.full_name}, failed to commit changes.")    
            print(f"{repo.full_name} was processed successfully.")
        except github.UnknownObjectException: # File not found
            print(f"{repo.full_name} doesn't have a file called \"LICENSE\". Skipping")


if __name__ == "__main__":
    main()