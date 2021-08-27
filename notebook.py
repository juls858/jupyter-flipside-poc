# %%
import pandas as pd

# %% [markdown]
"""
# Get Data From Flipside API
"""
# %%
api = "https://api.flipsidecrypto.com/api/v2/queries/882af4ed-5981-4815-b74c-f06a3ed2c9e6/data/latest"
# %% [markdown]
"""
Create Dataframe
"""
# %%
df = pd.read_json(api)
df["BLOCK_HOUR"] = pd.to_datetime(df["BLOCK_HOUR"])
# %% [markdown]
"""
Preview data
"""
# %%
df.head()
# %% [markdown]
"""
Check latest record
"""
# %%
df["BLOCK_HOUR"].max()
# %%
_ = df.set_index("BLOCK_HOUR").plot.line(title="Amount Transferred By Hour")
