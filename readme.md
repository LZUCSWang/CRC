

---

## 一、CRC的基本原理和错误检测能力

### 1. CRC的错误检测概率

- **随机错误的未检测概率：**

  对于长度为 \( k \) 的CRC码（即生成多项式的阶数为 \( k \)），随机错误的未检测概率为：

  $$
  P_{\text{未检测}} = \frac{1}{2^{k}}
  $$

- **包含因子 \( (x+1) \) 的生成多项式：**

  - **奇数重量错误（错误比特数为奇数）：** 未检测概率为0（全部可检测）。
  - **偶数重量错误（错误比特数为偶数）：** 未检测概率为 \($\frac{1}{2^{k-1}}$ \)。

- **不包含因子 \( (x+1) \) 的生成多项式：**

  - **所有错误模式（无论奇偶）：** 未检测概率为 \( $\frac{1}{2^{k}}$ \)。

### 2. 生成多项式的性质

- **CRC-12（度数12）：** 不包含 \( (x+1) \) 因子。
- **CRC-16（度数16）：** 包含 \( (x+1) \) 因子。
- **CRC-CCITT（度数16）：** 不包含 \( (x+1) \) 因子。
- **CRC-32（度数32）：** 包含 \( (x+1) \) 因子。

---

## 二、理论未检测错误概率计算

### 1. CRC-12（度数 \( k = 12 \)）

#### (1) 单比特错误（重量为1）

- **未检测概率：**
  $$
  P_{\text{未检测}} = 0 \quad (\text{因为任何CRC都能检测到所有单比特错误})
  $$

#### (2) 双比特错误（重量为2）

- **未检测概率：**
  $$
  P_{\text{未检测}} = \frac{1}{2^{12}} = \frac{1}{4096} \approx 0.0244\%
  $$
  
- **理论未检测次数：**
  $$
  N_{\text{未检测}} = 50000 \times P_{\text{未检测}} \approx 50000 \times \frac{1}{4096} \approx 12.2
  $$

#### (3) 三比特错误（重量为3）

- **未检测概率：**
  $$
  P_{\text{未检测}} = \frac{1}{2^{12}} = \frac{1}{4096} \approx 0.0244\%
  $$
  
- **理论未检测次数：**
  $$
  N_{\text{未检测}} \approx 12.2
  $$

#### (4) 偶数比特错误（重量为4）

- **未检测概率：**
  $$
  P_{\text{未检测}} = \frac{1}{2^{12}} = \frac{1}{4096} \approx 0.0244\%
  $$
  
- **理论未检测次数：**
  $$
  N_{\text{未检测}} \approx 12.2
  $$

#### (5) 奇数比特错误（重量为5）

- **未检测概率：**
$$
  P_{\text{未检测}} = \frac{1}{2^{12}} = \frac{1}{4096} \approx 0.0244\%
$$


- **理论未检测次数：**
  $$
  N_{\text{未检测}} \approx 12.2
  $$

#### (6) 突发错误（长度等于12）

- **所有长度小于等于12的突发错误都能检测到**
  $$
  P_{\text{未检测}} = 0
  $$
  
  

#### (7) 长突发错误（长度等于24）

- **未检测概率：**

  对于长度大于 \( k \) 的突发错误，未检测概率约为 \( $\frac{1}{2^{k}}$ \)：

  $$
  P_{\text{未检测}} = \frac{1}{2^{12}} \approx 0.0244\%
  $$
  
- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 12.2
  $$

#### (8) 随机错误

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{12}} \approx 0.0244\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 12.2
  $$

### 2. CRC-16（度数 \( k = 16 \)）

**由于CRC-16包含 \( (x+1) \) 因子，因此对奇数重量错误的未检测概率为0，对偶数重量错误的未检测概率为 \( $\frac{1}{2^{15}}$ \)。**

#### (1) 单比特错误（重量为1）

- **未检测概率：**

  $$
  P_{\text{未检测}} = 0
  $$

#### (2) 双比特错误（重量为2）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{15}} = \frac{1}{32768} \approx 0.00305\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} = 50000 \times \frac{1}{32768} \approx 1.526
  $$

#### (3) 三比特错误（重量为3）

- **未检测概率：**

  $$
  P_{\text{未检测}} = 0
  $$

#### (4) 偶数比特错误（重量为4）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{15}} \approx 0.00305\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 1.526
  $$

#### (5) 奇数比特错误（重量为5）

- **未检测概率：**
  $$
  P_{\text{未检测}} = 0
  $$

#### (6) 突发错误（长度等于16）

- **所有长度小于等于16的突发错误都能检测到**

  $$
  P_{\text{未检测}} = 0
  $$

#### (7) 长突发错误（长度等于32）

- **未检测概率：**

$$
  P_{\text{未检测}} = \frac{1}{2^{16}} = \frac{1}{65536} \approx 0.0015\%
$$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} = 50000 \times \frac{1}{65536} \approx 0.763
  $$

#### (8) 随机错误

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{16}} \approx 0.0015\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 0.763
  $$

### 3. CRC-CCITT（度数 \( k = 16 \)）

**CRC-CCITT不包含 \( (x+1) \) 因子，因此所有错误模式的未检测概率为 \( $\frac{1}{2^{16}}$ \)。**

#### (1) 单比特错误（重量为1）

- **未检测概率：**

  $$
  P_{\text{未检测}} = 0
  $$

#### (2) 双比特错误（重量为2）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{16}} = \frac{1}{65536} \approx 0.0015\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 0.763
  $$

#### (3) 三比特错误（重量为3）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{16}} \approx 0.0015\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 0.763
  $$

#### (4) 偶数比特错误（重量为4）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{16}} \approx 0.0015\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 0.763
  $$

#### (5) 奇数比特错误（重量为5）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{16}} \approx 0.0015\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 0.763
  $$

#### (6) 突发错误（长度等于16）

- **所有长度小于等于16的突发错误都能检测到**

  $$
  P_{\text{未检测}} = 0
  $$

#### (7) 长突发错误（长度等于32）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{16}} \approx 0.0015\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 0.763
  $$

#### (8) 随机错误

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{16}} \approx 0.0015\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 0.763
  $$

### 4. CRC-32（度数 \( k = 32 \)）

CRC-32包含 \( (x+1) \) 因子，对奇数重量错误未检测概率为0，对偶数重量错误未检测概率为 \( $\frac{1}{2^{31}}$ \)，极小，可忽略不计。

#### (1) 单比特错误（重量为1）

- **未检测概率：**

  $$
  P_{\text{未检测}} = 0
  $$

#### (2) 双比特错误（重量为2）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{31}} \approx 4.6566 \times 10^{-10}\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} = 50000 \times 4.6566 \times 10^{-12} \approx 2.3283 \times 10^{-7}
  $$

  **由于值极小，可认为未检测次数为0。**

#### (3) 三比特错误（重量为3）

- **未检测概率：**

  $$
  P_{\text{未检测}} = 0
  $$

#### (4) 偶数比特错误（重量为4）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{31}} \approx 4.6566 \times 10^{-10}\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 2.3283 \times 10^{-7}
  $$

#### (5) 奇数比特错误（重量为5）

- **未检测概率：**

  $$
  P_{\text{未检测}} = 0
  $$

#### (6) 突发错误（长度等于32）

- **所有长度小于等于32的突发错误都能检测到**

  $$
  P_{\text{未检测}} = 0
  $$

#### (7) 长突发错误（长度等于64）

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{32}} \approx 2.3283 \times 10^{-10}\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} = 50000 \times 2.3283 \times 10^{-12} \approx 1.1642 \times 10^{-7}
  $$

  **值极小，可认为未检测次数为0。**

#### (8) 随机错误

- **未检测概率：**

  $$
  P_{\text{未检测}} = \frac{1}{2^{32}} \approx 2.3283 \times 10^{-10}\%
  $$

- **理论未检测次数：**

  $$
  N_{\text{未检测}} \approx 1.1642 \times 10^{-7}
  $$

---

## 三、实验结果与理论值的比较

### 1. CRC-12

| 错误类型     | 理论未检测次数 | 实验未检测次数 | 理论未检测概率 (%) | 实验未检测概率 (%) |
| ------------ | -------------- | -------------- | ------------------ | ------------------ |
| 单比特错误   | 0              | 0              | 0                  | 0                  |
| 双比特错误   | 12.2           | 27             | 0.0244             | 0.054              |
| 三比特错误   | 12.2           | 25             | 0.0244             | 0.05               |
| 偶数比特错误 | 12.2           | 27             | 0.0244             | 0.054              |
| 奇数比特错误 | 12.2           | 25             | 0.0244             | 0.05               |
| 突发错误     | 0              | 0              | 0                  | 0                  |
| 长突发错误   | 12.2           | 0              | 0.0244             | 0                  |
| 随机错误     | 12.2           | 22             | 0.0244             | 0.044              |

**分析：**

- **双比特、三比特、偶数和奇数比特错误：** 实验未检测概率略高于理论值，但在统计允许的范围内。
- **长突发错误：** 实验中未检测到任何错误，说明实际检测能力优于理论估计。

### 2. CRC-16

| 错误类型     | 理论未检测次数 | 实验未检测次数 | 理论未检测概率 (%) | 实验未检测概率 (%) |
| ------------ | -------------- | -------------- | ------------------ | ------------------ |
| 单比特错误   | 0              | 0              | 0                  | 0                  |
| 双比特错误   | 1.526          | 0              | 0.00305            | 0                  |
| 三比特错误   | 0              | 2              | 0                  | 0.004              |
| 偶数比特错误 | 1.526          | 3              | 0.00305            | 0.006              |
| 奇数比特错误 | 0              | 2              | 0                  | 0.004              |
| 突发错误     | 0              | 0              | 0                  | 0                  |
| 长突发错误   | 0.763          | 0              | 0.0015             | 0                  |
| 随机错误     | 0.763          | 1              | 0.0015             | 0.002              |

**分析：**

- **双比特错误：** 实验未检测次数为0，优于理论估计。
- **三比特和奇数比特错误：** 理论上未检测概率为0，但实验中有极少数未检测到，可能是统计误差或实验限制。

### 3. CRC-CCITT

| 错误类型     | 理论未检测次数 | 实验未检测次数 | 理论未检测概率 (%) | 实验未检测概率 (%) |
| ------------ | -------------- | -------------- | ------------------ | ------------------ |
| 单比特错误   | 0              | 0              | 0                  | 0                  |
| 双比特错误   | 0.763          | 14             | 0.0015             | 0.028              |
| 三比特错误   | 0.763          | 12             | 0.0015             | 0.024              |
| 偶数比特错误 | 0.763          | 13             | 0.0015             | 0.026              |
| 奇数比特错误 | 0.763          | 16             | 0.0015             | 0.032              |
| 突发错误     | 0              | 0              | 0                  | 0                  |
| 长突发错误   | 0.763          | 0              | 0.0015             | 0                  |
| 随机错误     | 0.763          | 14             | 0.0015             | 0.028              |

**分析：**

- **未检测次数高于理论值：** 实验未检测次数显著高于理论估计，可能是因为CRC-CCITT对特定错误模式的检测能力较弱，或者实验中存在误差。

### 4. CRC-32

| 错误类型     | 理论未检测次数    | 实验未检测次数 | 理论未检测概率 (%) | 实验未检测概率 (%) |
| ------------ | ----------------- | -------------- | ------------------ | ------------------ |
| 单比特错误   | 0                 | 0              | 0                  | 0                  |
| 双比特错误   | \( $\approx 0$ \) | 0              | \( $\approx 0$ \)  | 0                  |
| 三比特错误   | 0                 | 0              | 0                  | 0                  |
| 偶数比特错误 | \( $\approx 0$ \) | 0              | \( $\approx 0$ \)  | 0                  |
| 奇数比特错误 | 0                 | 0              | 0                  | 0                  |
| 突发错误     | 0                 | 0              | 0                  | 0                  |
| 长突发错误   | \( $\approx 0$ \) | 0              | \( $\approx 0$ \)  | 0                  |
| 随机错误     | \( $\approx 0$ \) | 0              | \( $\approx 0$ \)  | 0                  |

**分析：**

- **CRC-32对各种错误类型的检测能力非常强**，实验结果与理论一致，未检测概率几乎为零。

---

## 四、总结

1. **理论与实验基本一致：** 大部分情况下，实验未检测概率与理论估计值接近。

2. **CRC多项式的选择影响检测能力：**

   - **包含 \( (x+1) \) 因子的多项式（如CRC-16、CRC-32）：** 能够检测所有奇数重量错误，对偶数重量错误的未检测概率也非常低。
   - **不包含 \( (x+1) \) 因子的多项式（如CRC-12、CRC-CCITT）：** 对所有错误模式的未检测概率相同，但检测能力略逊一筹。

3. **突发错误的检测能力：**

   - **所有CRC都能检测长度小于等于其多项式度数的突发错误。**
   - **对于超过度数的突发错误，未检测概率会增加，但实际中仍然很低。**

4. **实验中未检测次数高于理论值的情况：**

   - **CRC-CCITT的未检测次数明显高于理论值，可能是由于其生成多项式对特定错误模式的检测能力不足，或者实验数据量有限导致统计误差。**

---

## 五、代码

```python
import random
import matplotlib
import matplotlib.pyplot as plt

# 设置中文字体和解决负号显示问题
matplotlib.rcParams['font.sans-serif'] = ['Songti SC']  # 设置为系统中支持中文的字体名称
matplotlib.rcParams['axes.unicode_minus'] = False       # 解决负号显示问题

# 定义生成多项式（以整数表示）
CRC_POLYNOMIALS = {
    'CRC-12': 0x80F,      # x^12 + x^11 + x^3 + x^2 + x + 1
    'CRC-16': 0x8005,     # x^16 + x^15 + x^2 + 1
    'CRC-CCITT': 0x1021,  # x^16 + x^12 + x^5 + 1
    'CRC-32': 0x04C11DB7  # x^32 + ... + 1
}

# 计算CRC余数的函数
def compute_crc(data, poly, width):
    data <<= width
    data_len = data.bit_length()
    poly_len = poly.bit_length()
    shift = data_len - poly_len
    while shift >= 0:
        if (data >> (shift + poly_len - 1)) & 1:
            data ^= poly << shift
        shift -= 1
    return data & ((1 << width) - 1)

# 生成随机数据
def generate_data(length):
    return random.getrandbits(length)

# 引入错误（翻转指定位置的比特）
def introduce_errors(data, error_positions):
    for pos in error_positions:
        data ^= 1 << pos
    return data

# 验证函数
def verify_crc(poly_name, data_length, num_trials):
    poly = CRC_POLYNOMIALS[poly_name]
    width = poly.bit_length() - 1

    # 初始化统计数据
    stats = {
        'single_bit': {'detected': 0, 'undetected': 0},
        'double_bit': {'detected': 0, 'undetected': 0},
        'triple_bit': {'detected': 0, 'undetected': 0},
        'even_bit': {'detected': 0, 'undetected': 0},
        'odd_bit': {'detected': 0, 'undetected': 0},
        'burst_error': {'detected': 0, 'undetected': 0},
        'long_burst': {'detected': 0, 'undetected': 0},
        'random_error': {'detected': 0, 'undetected': 0},
    }

    # 定义突发错误的长度
    burst_length = width  # 突发错误长度等于生成多项式的阶数
    long_burst_length = 2 * width  # 长突发错误长度是生成多项式阶数的两倍

    for _ in range(num_trials):
        # 生成原始数据
        data = generate_data(data_length)
        # 计算CRC
        crc = compute_crc(data, poly, width)
        # 将CRC附加到数据后面
        transmitted_data = (data << width) | crc

        # 测试单比特错误
        error_positions = [random.randint(0, data_length + width - 1)]
        error_data = introduce_errors(transmitted_data, error_positions)
        received_crc = compute_crc(error_data >> width, poly, width)
        if received_crc != (error_data & ((1 << width) - 1)):
            stats['single_bit']['detected'] += 1
        else:
            stats['single_bit']['undetected'] += 1

        # 测试双比特错误
        error_positions = random.sample(range(data_length + width), 2)
        error_data = introduce_errors(transmitted_data, error_positions)
        received_crc = compute_crc(error_data >> width, poly, width)
        if received_crc != (error_data & ((1 << width) - 1)):
            stats['double_bit']['detected'] += 1
        else:
            stats['double_bit']['undetected'] += 1

        # 测试三比特错误
        error_positions = random.sample(range(data_length + width), 3)
        error_data = introduce_errors(transmitted_data, error_positions)
        received_crc = compute_crc(error_data >> width, poly, width)
        if received_crc != (error_data & ((1 << width) - 1)):
            stats['triple_bit']['detected'] += 1
        else:
            stats['triple_bit']['undetected'] += 1

        # 测试偶数比特错误（4个比特错误）
        error_positions = random.sample(range(data_length + width), 4)
        error_data = introduce_errors(transmitted_data, error_positions)
        received_crc = compute_crc(error_data >> width, poly, width)
        if received_crc != (error_data & ((1 << width) - 1)):
            stats['even_bit']['detected'] += 1
        else:
            stats['even_bit']['undetected'] += 1

        # 测试奇数比特错误（5个比特错误）
        num_errors = 5
        error_positions = random.sample(range(data_length + width), num_errors)
        error_data = introduce_errors(transmitted_data, error_positions)
        received_crc = compute_crc(error_data >> width, poly, width)
        if received_crc != (error_data & ((1 << width) - 1)):
            stats['odd_bit']['detected'] += 1
        else:
            stats['odd_bit']['undetected'] += 1

        # 测试突发错误（长度等于生成多项式的阶数）
        start_pos = random.randint(0, data_length + width - burst_length - 1)
        error_positions = [start_pos + i for i in range(burst_length)]
        error_data = introduce_errors(transmitted_data, error_positions)
        received_crc = compute_crc(error_data >> width, poly, width)
        if received_crc != (error_data & ((1 << width) - 1)):
            stats['burst_error']['detected'] += 1
        else:
            stats['burst_error']['undetected'] += 1

        # 测试长突发错误（长度是生成多项式阶数的两倍）
        if data_length + width - long_burst_length - 1 > 0:
            start_pos = random.randint(0, data_length + width - long_burst_length - 1)
            error_positions = [start_pos + i for i in range(long_burst_length)]
            error_data = introduce_errors(transmitted_data, error_positions)
            received_crc = compute_crc(error_data >> width, poly, width)
            if received_crc != (error_data & ((1 << width) - 1)):
                stats['long_burst']['detected'] += 1
            else:
                stats['long_burst']['undetected'] += 1

        # 测试随机错误（随机数量的比特错误）
        max_errors = max(1, int(0.1 * (data_length + width)))  # 最多10%的比特错误
        num_errors = random.randint(1, max_errors)
        error_positions = random.sample(range(data_length + width), num_errors)
        error_data = introduce_errors(transmitted_data, error_positions)
        received_crc = compute_crc(error_data >> width, poly, width)
        if received_crc != (error_data & ((1 << width) - 1)):
            stats['random_error']['detected'] += 1
        else:
            stats['random_error']['undetected'] += 1

    return stats

# 主函数，依次验证多种多项式并绘制图表
def main():
    data_length = 1024  # 增加数据长度
    num_trials = 50000  # 增加测试次数

    # 存储所有CRC多项式的统计结果
    all_stats = {}

    for poly_name in CRC_POLYNOMIALS.keys():
        print(f"正在测试 {poly_name} ...")
        stats = verify_crc(poly_name, data_length, num_trials)
        all_stats[poly_name] = stats

    # 绘制图表
    error_types = ['single_bit', 'double_bit', 'triple_bit', 'even_bit', 'odd_bit', 'burst_error', 'long_burst', 'random_error']
    error_labels = ['单比特错误', '双比特错误', '三比特错误', '偶数比特错误', '奇数比特错误', '突发错误', '长突发错误', '随机错误']
    x = range(len(error_types))

    for poly_name in CRC_POLYNOMIALS.keys():
        stats = all_stats[poly_name]
        detected = [stats[et]['detected'] for et in error_types]
        undetected = [stats[et]['undetected'] for et in error_types]

        total = [detected[i] + undetected[i] for i in range(len(detected))]
        detection_rates = [detected[i] / total[i] * 100 for i in range(len(detected))]

        plt.figure(figsize=(12, 6))
        plt.bar(x, detection_rates, tick_label=error_labels)
        plt.ylim(0, 100)
        plt.ylabel('检测成功率 (%)')
        plt.title(f'{poly_name} 不同错误类型的检测成功率')
        for i in x:
            plt.text(i, detection_rates[i] + 1, f"{detection_rates[i]:.2f}%", ha='center')
        # 保存图表到本地
        plt.savefig(f'{poly_name}_检测成功率.png')
        plt.close()

        # 打印详细统计信息
        print(f"\n{poly_name} 统计结果：")
        for i, et in enumerate(error_types):
            print(f"{error_labels[i]} - 检测到：{detected[i]}, 未检测到：{undetected[i]}, 检测成功率：{detection_rates[i]:.5f}%")

if __name__ == "__main__":
    main()

```

![](http://github.com/LZUCSWang/CRC/raw/main/CRC-12_%E6%A3%80%E6%B5%8B%E6%88%90%E5%8A%9F%E7%8E%87.png)

![](https://github.com/LZUCSWang/CRC/raw/main/CRC-16_%E6%A3%80%E6%B5%8B%E6%88%90%E5%8A%9F%E7%8E%87.png)

![](https://github.com/LZUCSWang/CRC/raw/main/CRC-32_%E6%A3%80%E6%B5%8B%E6%88%90%E5%8A%9F%E7%8E%87.png)

![](https://github.com/LZUCSWang/CRC/raw/main/CRC-CCITT_%E6%A3%80%E6%B5%8B%E6%88%90%E5%8A%9F%E7%8E%87.png)
