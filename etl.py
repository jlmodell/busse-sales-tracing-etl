from models import Tracing, Rep, Distributor
import os
import pandas as pd

unc_fp = os.path.join(r"\\busse", r"sales tracings\\")

MONTH = "October"
YYYY = "2022"

sheet = f"{MONTH} {YYYY}"
hs_sheet = "original"

house = os.path.join(unc_fp, "bussba9t.xlsm")
medline = os.path.join(
    unc_fp, "Raw Tracings", "Medline Tracings", "MEDLINE_OCT_2022.xlsx"
)
cardinal = os.path.join(unc_fp, "Cardinal.xlsm")
mckesson = os.path.join(unc_fp, "MGM.xlsm")
ndc = os.path.join(unc_fp, "NDC.xlsm")
owensminor = os.path.join(unc_fp, "om.xlsm")
concordance = os.path.join(unc_fp, "concordance.xlsm")
henryschein = os.path.join(
    unc_fp, "Henry Schein", f"HS Rebates {MONTH.upper()} {YYYY}.xlsm"
)

files = [house, medline, cardinal, mckesson, ndc, owensminor, concordance, henryschein]

if __name__ == "__main__":
    df = pd.read_excel(house, sheet_name=sheet)
