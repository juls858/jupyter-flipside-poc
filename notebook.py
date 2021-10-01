# %%
import pandas as pd

pd.options.plotting.backend = "plotly"
# %% [markdown]
"""
# Get Data From Flipside API
"""
# %%
api = "https://api.flipsidecrypto.com/api/v2/queries/00880fc5-94d5-46ce-8e23-734a79ae1237/data/latest"
# %% [markdown]
"""
Create Dataframe
"""
# %%
df = pd.read_json(api)
# %% [markdown]
"""
Preview data
"""
# %%
df.head()
# %% [markdown]
"""
Create plot
"""
# %% [markdown]
"""
Verify data we have today's data
"""
# %%
df["DATE"].max()
# %%
df.plot.line(
    x="DATE", y="N_TRANSACTION", title="Matic – Daily Transactions (Last 30 Days)"
)

# %%
