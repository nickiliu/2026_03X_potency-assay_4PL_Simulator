# 2026_03X Potency Assay 4PL Simulator

## Disclaimer

This tool is intended solely for demonstrating general data-processing logic and for academic, educational, or research purposes. It is not intended for use in regulated decision-making or as a substitute for validated analytical methods.

---

## Project Overview

This interactive 4PL (Four-Parameter Logistic) fitting simulator was developed using real potency assay data generated on **July 16, 2026**.

In early-stage CMC development, experimental data are often limited. As a result, it can be difficult to predict how variations in individual data points may affect the final 4PL fitting results.

This simulator allows users to interactively adjust selected data points and immediately visualize the impact on the fitted curve and key parameters, including:

- Bottom
- Top
- LogEC50
- EC50
- Hill Slope
- R²

The purpose of this tool is to help users explore potential fitting outcomes and gain intuitive insight into parameter behavior under different data scenarios.

---

## Features

- Interactive 4PL curve fitting
- Real-time parameter recalculation
- Adjustable experimental data points using sliders
- Instant visualization of fitting results
- Dynamic display of:
  - Original data points
  - Fitted 4PL curve
- Automatic calculation of:
  - Bottom
  - Top
  - LogEC50
  - EC50
  - Hill Slope
  - R²
- Streamlit-based web application
- Suitable for exploratory analysis and potency assay evaluation

---

## How to Use

### Installation

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run 4PL_Fit_Simulator.py
```

### Usage

1. Launch the application.
2. Adjust the available sliders.
3. Review the updated 4PL parameters.
4. Observe the corresponding fitting curve and data points.
5. Use the results for exploratory analysis and educational purposes.

---

## Data Information

The current simulator uses **6 data points** for 4PL fitting:

- 4 points are fixed experimental values obtained from real assay data.
- 2 points are user-adjustable within predefined ranges.

This design allows users to investigate how limited changes in experimental results may influence 4PL fitting parameters and curve behavior.

---

# 2026_03X Potency Assay 4PL Simulator

## 免責事項

本ツールは、一般的なデータ処理ロジックの説明および学術・教育・研究目的のみに使用されるものです。規制対応や正式な解析結果として使用することを目的としていません。

---

## Project Overview

本シミュレーターは、**2026年7月16日に取得された実測データ**を基に作成された4PL（4パラメータロジスティック）フィッティングシミュレーターです。

CMC開発初期では実験データ数が限られていることが多く、個々のデータポイントの変化が4PLフィッティング結果にどのような影響を与えるかを事前に把握することは容易ではありません。

本ツールでは、指定されたデータポイントをインタラクティブに変更しながら、以下のパラメータの変化をリアルタイムで確認できます。

- Bottom
- Top
- LogEC50
- EC50
- Hill Slope
- R²

限られたデータ環境におけるフィッティング結果の傾向や想定結果を直感的に理解することを目的としています。

---

## Features

- インタラクティブな4PLフィッティング
- パラメータのリアルタイム再計算
- スライダーによるデータポイント調整
- フィッティング結果の即時反映
- 実測データ点および4PL曲線の同時表示
- Bottom、Top、LogEC50、EC50、Hill Slope、R²の自動算出
- StreamlitベースのWebアプリケーション
- Potency AssayおよびCMC検討用途に適用可能

---

## How to Use

### インストール

```bash
pip install -r requirements.txt
```

### 起動

```bash
streamlit run 4PL_Fit_Simulator.py
```

### 使用方法

1. アプリケーションを起動します。
2. スライダーで対象データを調整します。
3. 更新された4PLパラメータを確認します。
4. フィッティング曲線およびデータポイントの変化を確認します。
5. 結果を考察や教育目的に活用します。

---

## Data Information

本シミュレーターでは、計6点のデータを用いて4PLフィッティングを実施しています。

- 4点は実測値として固定
- 2点は指定範囲内でユーザーが調整可能

これにより、限られたデータ変動が4PLパラメータや曲線形状へ与える影響を視覚的に評価できます。

---

# 2026_03X Potency Assay 4PL Simulator

## 免责声明

本工具仅用于通用数据处理逻辑演示以及学术、教育和研究用途，不应用于法规申报、质量放行或替代经验证的分析方法。

---

## 项目概述（Project Overview）

本模拟器基于 **2026年7月16日获得的实际 Potency Assay 数据** 开发，用于进行4PL（四参数Logistic）曲线拟合模拟。

在CMC开发早期，实验数据通常较为有限，因此很难直观判断单个数据点变化会对最终4PL拟合结果产生何种影响。

本工具允许用户交互式调整指定数据点，并实时观察以下关键参数的变化：

- Bottom
- Top
- LogEC50
- EC50
- Hill Slope
- R²

帮助用户在实验数据有限的情况下，预览不同数据情景下可能出现的拟合趋势和结果。

---

## 功能特点（Features）

- 交互式4PL曲线拟合
- 参数实时计算与更新
- 支持通过滑块调整指定数据点
- 拟合结果即时可视化
- 动态显示：
  - 原始实验数据点
  - 4PL拟合曲线
- 自动计算：
  - Bottom
  - Top
  - LogEC50
  - EC50
  - Hill Slope
  - R²
- 基于 Streamlit 的网页应用
- 适用于 Potency Assay 与CMC相关探索分析

---

## 使用方法（How to Use）

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动程序

```bash
streamlit run 4PL_Fit_Simulator.py
```

### 使用流程

1. 启动应用程序。
2. 调整可编辑数据点对应的滑块。
3. 查看实时更新的4PL参数。
4. 观察拟合曲线和散点变化。
5. 将结果用于探索性分析、教学或研究用途。

---

## 数据说明（Data Information）

本模拟器使用共计6个数据点进行4PL拟合：

- 其中4个数据点为固定的实际实验数据
- 另外2个数据点可在预设范围内自由调整

用户可通过修改这两个数据点，观察有限数据变化对4PL参数及曲线形态的影响。
