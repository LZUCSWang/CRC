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
