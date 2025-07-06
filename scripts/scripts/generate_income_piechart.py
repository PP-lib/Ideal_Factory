import plotly.graph_objects as go

def generate_income_piechart(output_path="pie_income_distribution_2025.html"):
    """
    インドネシアにおける2025年の所得層別人口構成（億人）のパイチャートを生成し、HTMLで保存する
    """
    # データ（億人）
    labels = ['低所得者層', '中級所得層', '高級所得層']
    values = [1.8, 1.0, 0.1]  # 総人口約2.9億人

    # パイチャート作成
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        textinfo='label+percent',
        hole=0.3
    )])

    # レイアウト
    fig.update_layout(
        title='インドネシアにおける所得層の構成比（2025年・人口ベース）'
    )

    # HTML出力
    fig.write_html(output_path)
    print(f"✅ パイチャートを出力しました → {output_path}")


if __name__ == "__main__":
    generate_income_piechart()
