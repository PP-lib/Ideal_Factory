import plotly.graph_objects as go

# 年と人口（百万人） → 億人に変換
years = ['2025', '2035']
total_population = [280 / 100, 310 / 100]        # → 2.8億人, 3.1億人
middle_class = [100 / 100, 140 / 100]            # → 1.0億人, 1.4億人
high_income = [10 / 100, 18 / 100]               # → 0.1億人, 0.18億人

fig = go.Figure(data=[
    go.Bar(name='総人口', x=years, y=total_population, text=total_population, textposition='auto'),
    go.Bar(name='中間所得層人口', x=years, y=middle_class, text=middle_class, textposition='auto'),
    go.Bar(name='高級住宅層人口', x=years, y=high_income, text=high_income, textposition='auto')
])

fig.update_layout(
    title='インドネシアにおける人口カテゴリ別推移（2025 vs 2035）',
    xaxis_title='年',
    yaxis_title='人口（億人）',
    barmode='group',
    template='plotly_white'
)

# HTMLに出力（GitHub Pages対応）
fig.write_html("index.html")
