import plotly.graph_objs as go

from bitcoin.utils import get_cached_data

# Load data
halving_data = get_cached_data()

# Create figure
fig = go.Figure()

# Add line trace
fig.add_trace(go.Scatter(
    x=halving_data['date'], 
    y=halving_data['block'], 
    mode='lines', 
    name='Block Height',
))

# Add markers for each date
fig.add_trace(go.Scatter(
    x=halving_data['date'], 
    y=halving_data['block'], 
    mode='markers', 
    name='Halving Date', 
    marker=dict(color='red', size=8),
))

# Add vertical dotted lines for each date
for i, date in enumerate(halving_data['date']):
    # Add shape for line
    fig.add_shape(
        type='line', 
        x0=date, 
        y0=0, 
        x1=date, 
        y1=halving_data['block'].max(),
        line=dict(color='red', width=1, dash='dot'),
    )

    # Add annotation for date
    fig.add_annotation(
        x=date, 
        y=-0.1 * halving_data['block'].max(), 
        text=halving_data['date'].iloc[i].strftime('%b %d, %Y'),
        showarrow=False,
    )

# Set layout
fig.update_layout(title='Bitcoin Halving Forecast', xaxis_title='Date', yaxis_title='Block Height')
fig.update_xaxes(showticklabels=False)
