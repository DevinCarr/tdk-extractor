# TDK Part Extractor

Extract graph data from characteristic graphs on TDK website.

Currently Supported Datasheets:

- [MLCC Commercial General](https://product.tdk.com/info/en/catalog/datasheets/mlcc_commercial_general_en.pdf)
  - Example: https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012JB1H155K125AB

## Install

```shell
pip install -r requirements.txt
```

## Usage

```shell
usage: main.py [-h] --input INPUT [--output OUTPUT]

Extract part values from part catalog

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    input file of part numbers (one per line)
  --output OUTPUT  output file (csv)
```

### Input file example:

```
C2012JB1H155K125AB
C2012JB1H225K085AB
C2012JB1H225K125AB
C2012JB1H335K125AB
```

### Output file example:

Columns:
- 1. Link
- 2. Part Number
- 3. Capacitance (uF)
- 4. Package
- 5. Voltage Rating
- 6-20. DC Bias for voltage range: 0, 1, 2, 4, 6.3, 10, 16, 25, 30, 35, 40, 50, 65, 80, 100
- 21-35. Temp Rise for current range: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5

|Link                                                                                    |Part Number       |Capacitance (uF)  |Package|Voltage Rating|DC Bias 0|DC Bias 1  |DC Bias 2  |DC Bias 4  |DC Bias 6.3|DC Bias 10 |DC Bias 16 |DC Bias 25 |DC Bias 30 |DC Bias 35 |DC Bias 40 |DC Bias 50 |DC Bias 65|DC Bias 80|DC Bias 100|Tmp 0.5|Tmp 1.0|Tmp 1.5|Tmp 2.0|Tmp 2.5|Tmp 3.0|Tmp 3.5|Tmp 4.0|Tmp 4.5|Tmp 5.0|Tmp 5.5|Tmp 6.0|Tmp 6.5|Tmp 7.0|Tmp 7.5|
|----------------------------------------------------------------------------------------|------------------|------------------|-------|--------------|---------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012JB1H155K125AB|C2012JB1H155K125AB|1.5               |2012   |50.0          |1.5e-06  |1.49664e-06|1.48861e-06|1.44097e-06|1.35796e-06|1.18475e-06|8.86517e-07|5.64361e-07|4.34771e-07|           |2.99763e-07|2.21521e-07|          |          |           |1.8    |7.2    |16.2   |       |       |       |       |       |       |       |       |       |       |       |       |
|https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012JB1H225K085AB|C2012JB1H225K085AB|2.1999999999999997|2012   |50.0          |2.2e-06  |           |2.17964e-06|2.02157e-06|1.77318e-06|1.35821e-06|8.45282e-07|4.76608e-07|           |3.08759e-07|           |2.03599e-07|          |          |           |1.3005 |5.1005 |11.552 |       |       |       |       |       |       |       |       |       |       |       |       |
|https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012JB1H225K125AB|C2012JB1H225K125AB|2.1999999999999997|2012   |50.0          |2.2e-06  |2.23793e-06|2.2121e-06 |2.13048e-06|1.99928e-06|1.73672e-06|1.29463e-06|8.27622e-07|6.45536e-07|           |4.44371e-07|3.30667e-07|          |          |           |1.152  |4.5125 |10.082 |17.8605|       |       |       |       |       |       |       |       |       |       |       |
|https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012JB1H335K125AB|C2012JB1H335K125AB|3.3               |2012   |50.0          |3.3e-06  |           |3.33545e-06|3.21203e-06|2.97336e-06|2.48292e-06|1.77374e-06|1.13399e-06|           |7.13854e-07|           |4.52581e-07|          |          |           |0.882  |3.528  |7.938  |14.112 |       |       |       |       |       |       |       |       |       |       |       |
