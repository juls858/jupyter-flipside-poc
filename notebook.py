# %%
%%html
<script>
    // AUTORUN ALL CELLS ON NOTEBOOK-LOAD!
    require(
        ['base/js/namespace', 'jquery'], 
        function(jupyter, $) {
            $(jupyter.events).on("kernel_ready.Kernel", function () {
                console.log("Auto-running all cells-below...");
                jupyter.actions.call('jupyter-notebook:run-all-cells-below');
                jupyter.notebook.scroll_to_top();
                jupyter.actions.call('jupyter-notebook:save-notebook');                
                
            });
        });
        
        $( document ).ready(function(){
        code_shown=false;
        $('div.input').hide()});
    
    
</script>
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
