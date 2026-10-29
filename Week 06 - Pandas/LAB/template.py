"""AI and data science dataset-ingestion monitoring report."""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read the AI dataset-ingestion data.

df = pd.read_csv("ai_dataset_loads.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column showing how many expected rows were loaded.
#
#    A complete dataset is 100% or more. A dataset between 90% and 100% is
#    close to complete and anything below 90% needs investigation.

df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = df["percent"].apply(
    lambda percent: "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"
)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print the AI dataset report.
#    Typical   : filter to show only datasets that are not complete.
#    Excellent : group by status, save the report, and chart the status counts.

print(df)
print("\nRows needing attention:")
print(df[df["status"] != "OK"])
print("\nCounts by status:")
print(df["status"].value_counts())
df.to_csv("ai_dataset_load_report.csv", index=False)

df["status"].value_counts().plot(
    kind="bar",
    title="AI Dataset Ingestion Status",
    xlabel="Status",
    ylabel="Number of datasets",
)
plt.tight_layout()
plt.savefig("ai_dataset_load_status.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
